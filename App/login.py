import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker , declarative_base

# Base de datos simulada
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String,unique=False,nullable=False)

class UserManager:
    def __init__(self, session):
        self.session = session

    def create_user(self, username, email, password):
        user = User(username=username, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user
    
    def login(self,password,email):
        user = self.session.query(User).filter_by(email=email).first() 
        if user != None:
            if user.password == password:
                return f"Bienvenido {user.username}"
            else:
                return "Usuario o Contrasenia Incorrectos."
        else:    
            return "Usuario o Contrasenia Incorrectosas" ## Damos un mensaje generico esto como buena practica de seguridad