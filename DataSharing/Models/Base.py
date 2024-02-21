from datetime import datetime
from PyMongoDb import IPyMongoDb
from bson.objectid import ObjectId

class Base(IPyMongoDb, object):
    m_internal_id = ObjectId()
    m_created_at = datetime.now()
    

