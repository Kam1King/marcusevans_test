from schemas import *

class UserOperation:
    def __init__(self,db_conn,username):
        self.db_conn = db_conn
        self.username = username


    def login(self):
        return self.db_conn.query(User).filter(User.email == self.username).first()