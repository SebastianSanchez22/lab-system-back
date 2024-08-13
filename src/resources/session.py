from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.engine import URL
from src.config.constants import SCHEMA


class Database(object):
    __instance = None
    session = None

    def __new__(cls, *args, **kwargs):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance
    
    def __init__(self, credentials: dict):
        if self.session is None:
            url = URL(
                drivername=credentials["drivername"],
                username=credentials["username"],
                password=credentials["password"],
                host=credentials["host"],
                port=credentials["port"],
                database=credentials["database"]
            )
            self.session = self._create_session(url)

    def _create_session(self, url: URL):
        engine = create_engine(url, poolclass=NullPool)
        metadata = MetaData()
        metadata.reflect(bind=engine, schema=SCHEMA)
        Session = sessionmaker(bind=engine)
        return Session()
    
    def __del__(self):
        if self.session:
            self.session.close()
            self.session = None

    def get_all(self, **kwargs):
        try:
            return self.session.query(**kwargs).all()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_one(self, **kwargs):
        try:
            return self.session.query(**kwargs).first()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def add_one(self, **kwargs):
        try:
            self.session.add(kwargs["item"])
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def update_one(self, **kwargs):
        try:
            old_data = self.session.get(kwargs["table"], kwargs["id"])
            for key, value in kwargs["data"].items():
                setattr(old_data, key, value)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def delete_one(self, **kwargs):
        try:
            self.session.delete(kwargs["item"])
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def disable_one(self, **kwargs):
        try:
            old_data = self.session.get(kwargs["table"], kwargs["id"])
            setattr(old_data, "disabled", True)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e