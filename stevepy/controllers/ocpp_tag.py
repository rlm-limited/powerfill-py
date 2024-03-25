from datetime import datetime
from typing import Optional, List, Union
from models import OcppTagModel
from controllers.database import DBController
from exceptions import OCPPTagAlreadyExistsError, OCPPTagDoesNotExistError
from sqlalchemy.exc import IntegrityError, NoResultFound




class OCPPTagController:
    def __init__(self, database : Union[DBController, str]) -> None:
        if type(database) == DBController:
            self.database = database
        elif type(database) == str:
            self.database = DBController(database)
        else:
            raise TypeError('Invalid Database Type')

    def create_tag(self , id_tag: str, parent_id_tag: Optional[int] = None, expiry_date : Optional[datetime]  = None, note : Optional[str]  = None, max_active_transaction_count : int = 1) -> OcppTagModel:
        try:
            tag =  OcppTagModel(id_tag=id_tag, parent_id_tag=parent_id_tag, expiry_date=expiry_date, max_active_transaction_count=max_active_transaction_count, note=note)
            return OcppTagModel(**self.database.add(tag).__dict__)
        except IntegrityError:
            raise OCPPTagAlreadyExistsError('OCPPTag Already Exist in Database')

    def get_all_tags(self, limit : Optional[int] = None) -> List[OcppTagModel]:
        return self.database.query(OcppTagModel, limit=limit)

    def get_tag_with_id(self, id_tag : str) -> OcppTagModel:
        try:
            tag = self.database.query(OcppTagModel, id_tag=id_tag, one_or_none=True)
            return tag
        except NoResultFound:
            raise OCPPTagDoesNotExistError('OCPPTag Does Not Exist in Database')
    
    def get_or_create_tag(self, id_tag : str) -> OcppTagModel:
        try:
            tag = self.get_tag_with_id(id_tag=id_tag)
            return tag
        except OCPPTagDoesNotExistError:
            tag = self.create_tag(id_tag=id_tag)
            return tag
        