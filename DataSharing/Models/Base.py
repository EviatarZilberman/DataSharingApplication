from datetime import datetime
from Interface.IPyMongoDb import IPyMongoDb
from bson.objectid import ObjectId

class Base(IPyMongoDb):
    m_internal_id = ObjectId()
    m_created_at = datetime.now()
    
    def __init__(self):
        self.m_internal_id = ObjectId()
        self.m_created_at = datetime.now()
        
    def to_dict(self):
        pass
    
    @staticmethod
    def from_dict(dictionary):
        pass

