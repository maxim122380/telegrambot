from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer , primary_key=True)
    name = Column(String)
    balance = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, balance={self.balance})>"
    
class Database:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///base.db")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def get_user(self, id):
        return self.session.query(User).filter_by(id=id).first()
    
    def register(self, id, name):
        user = User(id=id, name=name, balance=0)
        self.session.add(user)
        self.session.commit()
        return True
    
    def update_balance(self, id, balance, status):
        user = self.get_user(id)
        balance = float(balance)
        if user:
            if status:
                user.balance += balance
            else:
                user.balance -= balance
            
            self.session.commit()
            return user.balance
        else:
            return None
    
    def get_balance(self, id):
        user = self.get_user(id)
        return user.balance
        
    def __del__(self):
        self.session.close()
        