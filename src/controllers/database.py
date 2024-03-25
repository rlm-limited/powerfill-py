from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError, IntegrityError, MultipleResultsFound, NoResultFound
from sqlalchemy.ext.declarative import declarative_base as Base
from sqlalchemy import desc
from typing import Optional, Any, List, Union



class DBController:
    connected : bool = False
    
    def __init__(self, database_url : str, echo : bool = False) -> None:
        engine = create_engine(database_url, echo=echo)
        try:
            engine.connect()
            self.connected = True
        except OperationalError:
            raise OperationalError("Invalid Database URL; Could not connect to database!")
        finally:
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def query(self, model : Base, limit : Optional[int] = None, one_or_none : bool = False, first : Optional[bool] = False, order_by : Optional[Any] = None, **kwargs) -> Union[Base, List[Base]]:
        try:
            with self.SessionLocal() as session:
                query = session.query(model).filter_by(**kwargs).order_by(order_by).limit(limit)
                if one_or_none:
                    return query.one()
                if first:
                    return query.first()
                return query.all()
        except NoResultFound as err:
            raise NoResultFound("No Result Found")

    def exists(self, model : Base, **kwargs) -> Base:
        try:
            with self.SessionLocal() as session:
                query = session.query(model).filter_by(**kwargs)
                return query.scalar()
        except MultipleResultsFound as err:
            raise MultipleResultsFound("Multiple Results Found", params=query, orig=err)

    def get(self, model : Base, pk : Any) -> Base:
        with self.SessionLocal() as session:
            return session.get(model, pk).one()

    def add(self, model : Base) -> Base:
        with self.SessionLocal() as session:
            try:
                session.add(model)
                session.commit()
                return model
            except IntegrityError as err:
                session.rollback()
                raise IntegrityError("OCPPTag Already Exists!", params=model , orig=err)

        




