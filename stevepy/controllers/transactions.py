from typing import Optional, List, Union, Any
from controllers.database import DBController
from controllers.charger import ChargeBoxController, ConnectorStates
from controllers.ocpp_tag import OCPPTagController
from exceptions import ChargeBoxConnectorNotAvailableError, OCPPTagDoesNotExistError, InvalidWebRequestReturnCode, RequestTimeoutError, HTTPConnectionError, UnableToFindTransactionError, RemoteStartFailedError, RemoteStopFailedError
from sqlalchemy.exc import NoResultFound
import requests
from requests.exceptions import Timeout, ConnectionError
from models import TransactionModel
from datetime import datetime, timedelta


class TransactionsController:
    def __init__(self, database : Union[DBController, str], steve_url : str) -> None:
        if type(database) == DBController:
            self.database = database
        elif type(database) == str:
            self.database = DBController(database)
        else:
            raise TypeError('Invalid Database Type')
        self.steve_url = steve_url
        self.chargebox = ChargeBoxController(self.database)
        self.ocpp_tag = OCPPTagController(self.database)

    
    def get_all_transactions(self, limit : Optional[int] = None, only_active : Optional[bool] = False) -> List[TransactionModel]:
        transactions = self.database.query(TransactionModel, limit=limit, )
        return transactions

    def get_transaction_with_pk(self, transaction_pk : int) -> TransactionModel:
        try:
            return self.database.get(TransactionModel, pk=transaction_pk)
        except NoResultFound:
            raise UnableToFindTransactionError(f'Unable to find transaction with Primary Key: {transaction_pk}')

    def get_active_transaction_with_id_tag(self, id_tag : str) -> Union[TransactionModel, Any]:
        try:
            return self.database.query(TransactionModel, id_tag=id_tag, stop_timestamp=None, one_or_none=True)
        except NoResultFound:
            raise UnableToFindTransactionError(f'Unable to find transaction with id_tag: {id_tag}')
        

    async def remote_start(self, charge_box_id : str, connector_id : int, id_tag : str, energy_kwh : Optional[float] = None):
        try:
            #Pre-Check to see if Charger is Available on the Connector Level
            tag = await self.ocpp_tag.get_tag_with_id(id_tag=id_tag)
            charge_box = await self.chargebox.get_charge_box_with_id(charge_box_id=charge_box_id)

            pre_charge_box_status = self.chargebox.get_connector_status_with_chargebox_id(charge_box_id=charge_box.charge_box_id, connector_id=connector_id)

            if pre_charge_box_status != ConnectorStates.AVAILABLE:
                raise ChargeBoxConnectorNotAvailableError('Charger is not available on this connector')
            
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            payload = f'chargePointSelectList=JSON%3B{charge_box.charge_box_id}%3B-&idTag={tag.id_tag}&connectorId={connector_id}'
            response = requests.post(url='http://ev.meshpower.co.rw:8180/steve/manager/operations/v1.6/RemoteStartTransaction', data=payload, headers=headers, allow_redirects=False, timeout=100)

            if response.status_code != 302:
                raise InvalidWebRequestReturnCode(f'Invalid Web Request Return Code: {response.status_code}')
            
            #Check if the connect is Preparing Mode
            post_charge_box_status = self.chargebox.get_connector_status(charge_box.connector_id_to_pk_dict[connector_id], buffer=10)

            if post_charge_box_status!= ConnectorStates.PREPARING:
                raise RemoteStartFailedError(f'Remote Start Failed: {charge_box.charge_box_id}')
            
            #transaction = self.get_active_transaction_with_id_tag(id_tag=tag.id_tag)

            
        except ConnectionError as err:
            raise HTTPConnectionError('HTTP Connection Error')
        except Timeout as err:
            raise RequestTimeoutError('Time Out Error')
        except OCPPTagDoesNotExistError as err:
            raise OCPPTagDoesNotExistError("OCPP Tag Does Not Exist in Database")


    async def remote_stop(self, transaction_id : int, charge_box_id : str):
        try: 
            charge_box = await self.chargebox.get_charge_box_with_id(charge_box_id=charge_box_id)
            transaction = await self.get_transaction_with_pk(transaction_pk=transaction_id)
            payload = {
                'transactionId' : f'{transaction.transaction_pk}',
                'chargePointSelectList' : f'JSON%3B{charge_box.charge_box_id}%3B-'
                }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url='http://ev.meshpower.co.rw:8180/steve/manager/operations/v1.6/RemoteStartTransaction', data=payload, headers=headers, allow_redirects=False)

            if response.status_code != 302:
                raise InvalidWebRequestReturnCode(f'Invalid Web Request Return Code: {response.status_code}')
            
            #connector_state = ChargeBoxController.get_connector_status(connector_id=connector_id)



        except ConnectionError:
            raise requests.exceptions.ConnectionError('')
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout('')
        finally:
            pass


    

    
    

