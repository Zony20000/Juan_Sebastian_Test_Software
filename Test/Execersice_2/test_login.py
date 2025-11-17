import pytest
from App.Execersice_2.login import *

# Set BD - lo escribi en ingles por que en espaniol se escribe raro
# el decorador de pytest ayuda a que esto se vuelva un parametro global/base para las pruebas consiguiente y se puedan usar, como un parametro a recibir evitando conflictos
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

# Creamos un solo usuario, por que el enfoque de las pruebas es el login y corroborar que esto funcione
@pytest.fixture
def created_user(user_manager):
    user= user_manager.create_user("testuser", "test@example.com","Punta.2")    
    return user

# Created user retorna el objeto del usuario y en este podemos consultar por sus atributos
def test_user_management_integration(created_user):

    # Verifica que el usuario haya sido creado correctamente
    assert created_user is not None
    assert created_user.username == "testuser"
    assert created_user.email == "test@example.com"
    assert created_user.password == "Punta.2"   

# con los datos correctos manejamos el login y la funcion es dada por la instancia por ello se necesita user_manager
def test_login_true(user_manager,created_user):

    resultado_esperado = f"Bienvenido {created_user.username}"

    resultado_actual = user_manager.login("Punta.2","test@example.com")

    assert resultado_actual == resultado_esperado

#Estas pruebas son de falla aunque no se muestre diferencia existe esto dado por el punto, donde se busca mantener tambien buenas practicas de seguridad
def test_login_false_by_password(user_manager,created_user):

    resultado_esperado = "Usuario o Contrasenia Incorrectos."

    resultado_actual = user_manager.login("Pua.","test@example.com")

    assert resultado_actual == resultado_esperado

# En esta caso la verificacion se realiza con el query de la clase si no se realiza da como resultado que user is None    
def test_login_false_by_email(user_manager,created_user):

    resultado_esperado = "Usuario o Contrasenia Incorrectosas"

    resultado_actual = user_manager.login("Punta.2","test@example.co")

    assert resultado_actual == resultado_esperado