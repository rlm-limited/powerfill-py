import unittest
import logging
from controllers.database import DBController
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import select


class BasicDBTest(unittest.TestCase):
    db = DBController(database_url="mariadb+mariadbconnector://steve:changeme@ev.meshpower.co.rw:3306/stevedb")

    def test_valid_db_crendetials(self):
        self.assertTrue(self.db.connected, True)

    def test_auto_map_db(self):
        map = self.db.map_db()
        self.assertIsInstance(map, automap_base)
    
    def test_db_models(self):
        self.assertEqual(len(self.db.models), 11)

    def test_db_query_method(self):
        test_query = select(self.db.models.user)
        result = self.db.query(test_query)
        pass



