import email
from Models.Base import Base

class User(Base):
    m_username = None
    m_first_name = None
    m_last_name = None
    m_email = None
    m_password = None
    m_private_folders: list = None
    m_shared_folders: list = None
    
    def __init__(self):
        pass
    
    def __init__(self, id, user_name, c_date, f_name, l_name, password, p_folders, s_folders):
        self.m_internal_id = id
        self.m_created_at = c_date
        self.m_username = user_name
        self.m_first_name = f_name
        self.m_last_name = l_name
        self.m_email = email
        self.m_password = password
        self.m_private_folders = p_folders
        self.m_shared_folders = s_folders
        
    def __init__(self, id, user_name, c_date, f_name, l_name, password):
        self.m_internal_id = id
        self.m_created_at = c_date
        self.m_username = user_name
        self.m_first_name = f_name
        self.m_last_name = l_name
        self.m_email = email
        self.m_password = password
        

    def to_dict(self):
        return {"_id": str(self.m_internal_id), "created_at": str(self.m_created_at),"username": self.m_username, "first_name": self.m_first_name, "last_name": self.m_last_name, "email": self.m_email, "private_folder": self.m_private_folders, "shared_folders": self.m_shared_folders }
        
        @staticmethod
        def from_dict(dictionary):
            return { 
                User(dictionary["id"], dictionary["creation_date"], dictionary["username"],
                     dictionary["first_name"], dictionary["last_name"], dictionary["dassword"],
                    dictionary["private_folders"], dictionary["shared_folders"]) 
                }


