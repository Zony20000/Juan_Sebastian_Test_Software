import pytest
#Importaciones para el uso de sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker , declarative_base

# Base de datos simulada
Base = declarative_base()

# Dentro de la clase user se esta heredando de base que es el resultado de una funcion de sql alchemy
class User(Base):
    # Se establece el nombre de la tabla
    __tablename__ = 'users'
    #La estructura es similar a una bd, en lo respectivo a la declaracion de variables
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String,unique=False,nullable=False)

#Ahora la clase manager se encarga del manejo de los datos, realizando una encapsulacion donde solo la clase padre es quien declara los datos y en este caso esta es la unica que maneja las opciones con los datos
class UserManager:
    def __init__(self, session):
        self.session = session
    # La funcion solicita los datos que se establecieron en class User 
    def create_user(self, username, email, password):
        user = User(username=username, email=email, password=password)
        #Agregamos el usuario a la pila de datos para cargar a la bd
        self.session.add(user)
        #Carga los datos de la pila a la BD
        self.session.commit()
        return user
    
    # En esta funcion estamos verificando los datos del usuario
    def login(self,password,email):
        # en base al email dado buscamos si existe
        user = self.session.query(User).filter_by(email=email).first() 
        #verificamos el resultado de la consulta
        if user != None:
            #Si el resultado es correcto usamos los datos de este para verificar
            if user.password == password:
                return f"Bienvenido {user.username}"
            else:
                return "Usuario o Contrasenia Incorrectos."# como buena practica de seguridad no le damos tantos datos al usuario sobre que fallo
        else:    
            return "Usuario o Contrasenia Incorrectosas" ## Damos un mensaje generico esto como buena practica de seguridad