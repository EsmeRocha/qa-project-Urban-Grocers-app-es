import sender_stand_request
import data

# Función para obtener el cuerpo del kit con un nombre específico
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body

# Función de aserción positiva para códigos 201
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kits(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_name

# Función de aserción negativa para código 400
def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kits(kit_body)

    assert kit_response.status_code == 400

# Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert sender_stand_request.response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert sender_stand_request.response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

# Función de aserción negativa para el caso sin campo "name"
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kits(kit_body)

    assert response.status_code == 400

# Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Pruebas positivas
# Prueba 1: Nombre con 1 carácter (caso positivo) 201
def test_kit_name_min_length():
   positive_assert(data.kit_body_name_min_length)

# Prueba 2: Nombre con 511 caracteres (caso positivo) 201
def test_kit_name_max_length():
   positive_assert(data.kit_body_name_max_length)

# Prueba 3: Nombre con caracteres especiales (caso positivo) 201
def test_kit_name_special_chars():
    positive_assert(data.kit_body_name_special_chars)

# Prueba 4: Nombre con espacios (caso positivo) 201
def test_kit_name_with_spaces():
    positive_assert(data.kit_body_name_with_spaces)

# Prueba 5: Nombre con números (caso positivo) 201
def test_kit_name_numbers():
    positive_assert(data.kit_body_name_numbers)


# Pruebas negativas
# Prueba 6: Nombre vacío (caso negativo) 400
def test_kit_name_empty_get_error_response():
    negative_assert(data.kit_body_name_empty)

# Prueba 7: Nombre con 512 caracteres (caso negativo) 400
def test_kit_name_over_max_length():
    negative_assert(data.kit_body_name_over_max_length)

# Prueba 8: Sin el parámetro "name" en el cuerpo (caso negativo)
def test_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_name(kit_body)

# Prueba 9: Tipo de dato incorrecto en "name" (caso negativo)
def test_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(data.kit_body_name_as_number)
    response = sender_stand_request.post_new_client_kits(kit_body)

    assert response.status_code == 400
