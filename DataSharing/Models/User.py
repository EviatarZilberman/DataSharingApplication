from typing_extensions import override
from Base import Base

class User(Base, object):
    m_first_name = None
    m_last_name = None
    m_email = None
    m_password = None
    m_private_folders: list = None
    m_shared_folders: list = None
    
    def __init__(self):
        pass
    
    def __init__(self, id, creation_date):
        

        def to_dict(self):
            return {"_id": str(self.m_internal_id), "created_at": str(self.m_created_at), "first_name": self.m_first_name, "last_name": self.m_last_name, "email": self.m_email, "private_folder": self.m_private_folders, "shared_folders": self.m_shared_folders }
    
        def from_dict(self):
            return { User() }


