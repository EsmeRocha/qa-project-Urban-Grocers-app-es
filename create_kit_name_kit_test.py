import sender_stand_request
import data

# Función para obtener el cuerpo del kit con un nombre específico
def get_kit_body(name):
    kit_body = data.product_kit_body.copy()
    kit_body["name"] = name
    return kit_body

# Función para obtener el authToken creando un nuevo usuario
def get_new_user_token():
    user_body = data.user_body.copy()
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 201
    auth_token = response.json()["authToken"]
    return auth_token

# Función de aserción positiva
def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kits(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función de aserción negativa para código 400
def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kits(kit_body, auth_token)
    assert response.status_code == 400
   # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

# Prueba 1: Nombre con 1 carácter (caso positivo) 201
def test_create_kit_with_1_char_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

# Prueba 2: Nombre con 511 caracteres (caso positivo) 201
def test_create_kit_with_511_char_name():
    auth_token = get_new_user_token()
    long_name = "a" * 511
    kit_body = get_kit_body(long_name)
    positive_assert(kit_body, auth_token)

# Prueba 3: Nombre vacío (caso negativo) 400
def test_create_kit_with_empty_name():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

# Prueba 4: Nombre con 512 caracteres (caso negativo) 400
def test_create_kit_with_512_char_name():
    auth_token = get_new_user_token()
    long_name = "a" * 512
    kit_body = get_kit_body(long_name)
    negative_assert_code_400(kit_body, auth_token)

# Prueba 5: Nombre con caracteres especiales (caso positivo) 201
def test_create_kit_with_special_characters():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body, auth_token)

# Prueba 6: Nombre con espacios (caso positivo) 201
def test_create_kit_with_spaces():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body, auth_token)

# Prueba 7: Nombre con números (caso positivo) 201
def test_create_kit_with_numbers():
    auth_token = get_new_user_token()
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)

# Prueba 8: Sin el parámetro "name" en el cuerpo (caso negativo)
def test_create_kit_without_name():
    auth_token = get_new_user_token()
    kit_body = data.product_kit_body.copy()
    kit_body.pop("name", None)
    negative_assert_code_400(kit_body, auth_token)

# Prueba 9: Tipo de dato incorrecto en "name" (número en lugar de cadena) (caso negativo)
def test_create_kit_with_name_as_number():
    auth_token = get_new_user_token()
    kit_body = get_kit_body(123)  # 123 es un número
    negative_assert_code_400(kit_body, auth_token)
