headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

user_body = {
    "firstName": "Rocio",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

product_kit_body = {
    "ids": [1, 2, 3]
}

# Valores de prueba para diferentes casos de la lista de comprobación

# 1. El número permitido de caracteres (1)
kit_body_1_char = {
    "name": "a"  # Nombre con 1 carácter
}

# 2. El número permitido de caracteres (511)
kit_body_511_chars = {
    "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
}

# 3. El número de caracteres es menor que la cantidad permitida (0)
kit_body_empty = {
    "name": ""  # Nombre vacío
}

# 4. El número de caracteres es mayor que la cantidad permitida (512)
kit_body_over_limit = {
    "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
}

# 5. Se permiten caracteres especiales
kit_body_special_chars = {
    "name": "№%@,"  # Nombre con caracteres especiales
}

# 6. Se permiten espacios
kit_body_spaces = {
    "name": " A Aaa "  # Nombre con espacios
}

# 7. Se permiten números
kit_body_numbers = {
    "name": "123"  # Nombre con números
}

# 8. El parámetro no se pasa en la solicitud
kit_body_no_name = {
    # Sin parámetro 'name'
}

# 9. Se ha pasado un tipo de parámetro diferente (número)
kit_body_invalid_type = {
    "name": 123  # Nombre con tipo de dato incorrecto (número en lugar de cadena)
}
