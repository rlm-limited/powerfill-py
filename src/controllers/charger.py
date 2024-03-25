from controllers.database import DBController
from models import ConnectorStatusModel, ChargeBoxModel
from sqlalchemy.exc import NoResultFound
from sqlalchemy import desc
from exceptions import ChargeBoxDoesNotExistError, ChargeBoxConnectorDoesNotExistError
from enum import Enum
from typing import Any, List, Optional
import time


class ConnectorStates(Enum):
    AVAILABLE = "Available"
    FINISHING = "Finishing"
    CHARGING = "Charging"
    PREPARING = "Preparing"
    FAULTED = "Faulted"
    SUSPENDEDEVSE = "SuspendedEVSE"
    

class ChargeBoxController:

    def __init__(self, database : DBController) -> None:
        self.database = database
    
    def get_all_chargeboxes(self, only_accepted : Optional[bool] = False) -> List[ChargeBoxModel]:
        return self.database.query(ChargeBoxModel)

    def get_charge_box_with_id(self, charge_box_id : int) -> ChargeBoxModel:
        try:
            return self.database.query(ChargeBoxModel, charge_box_id=charge_box_id, one_or_none=True)
        except NoResultFound as err:
            raise ChargeBoxDoesNotExistError('ChargeBox Does Not Exist in Database')

    def get_connector_status(self, connector_pk : int, buffer : float = 10.0) -> ConnectorStates:
        try:
            time.sleep(buffer)
            status =  self.database.query(ConnectorStatusModel, connector_pk=connector_pk, order_by=desc(ConnectorStatusModel.status_timestamp), first=True)
            return ConnectorStates(value=status.status)      
        except NoResultFound as err:
            raise ChargeBoxConnectorDoesNotExistError('ChargeBox Connector Does Not Exist in Database')

    def get_connector_status_with_chargebox_id(self, charge_box_id : str, connector_id : Optional[int] = None) -> ConnectorStates:
        charge_box_obj = self.get_charge_box_with_id(charge_box_id=charge_box_id)
        return self.get_connector_status(connector_pk=charge_box_obj.connector_id_to_pk_dict[connector_id])


  
    

