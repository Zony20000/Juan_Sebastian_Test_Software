import pytest
from App.login import *

@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def user_manager(db_session):
    return UserManager(db_session)

@pytest.fixture
def created_user(user_manager):
    user= user_manager.create_user("testuser", "test@example.com","Punta.2")    
    return user

def test_user_management_integration(created_user):

    # Verifica que el usuario haya sido creado correctamente
    assert created_user is not None
    assert created_user.username == "testuser"
    assert created_user.email == "test@example.com"
    assert created_user.password == "Punta.2"   

def test_login_true(user_manager,created_user):

    resultado_esperado = f"Bienvenido {created_user.username}"

    resultado_actual = user_manager.login("Punta.2","test@example.com")

    assert resultado_actual == resultado_esperado
    
def test_login_false_by_password(user_manager,created_user):

    resultado_esperado = "Usuario o Contrasenia Incorrectos."

    resultado_actual = user_manager.login("Pua.","test@example.com")

    assert resultado_actual == resultado_esperado
    
def test_login_false_by_email(user_manager,created_user):

    resultado_esperado = "Usuario o Contrasenia Incorrectosas"

    resultado_actual = user_manager.login("Punta.2","test@example.co")

    assert resultado_actual == resultado_esperado