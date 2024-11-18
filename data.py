headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Rocio",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_body = {
    "name": "Nombre"
}

# Valores de prueba para diferentes casos de la lista de comprobación

# 1. El número permitido de caracteres (1)
kit_body_name_min_length = {
    "name": "a"  # Nombre con 1 carácter
}

# 2. El número permitido de caracteres (511)
kit_body_name_max_length = {
    "name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
          "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
          "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
          "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
          "abcdabcdabcdabcdabcdabcdabcdabC"}

# 3. Se permiten caracteres especiales
kit_body_name_special_chars = {
    "name": "№%@,"  # Nombre con caracteres especiales
}

# 4. Se permiten espacios
kit_body_name_with_spaces = {
    "name": "A Aaa"  # Nombre con espacios
}

# 5. Se permiten números
kit_body_name_numbers = {
    "name": "123"  # Nombre con números
}

# 6. El número de caracteres es menor que la cantidad permitida (0)
kit_body_name_empty = {
    "name": ""  # Nombre vacío
}

# 7. El número de caracteres es mayor que la cantidad permitida (512)
kit_body_name_over_max_length = {
    "name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcD"}


# 8. El parámetro no se pasa en la solicitud
kit_body_name_missing = {
    # Sin parámetro 'name'
}

# 9. Se ha pasado un tipo de parámetro diferente (número)
kit_body_name_as_number = {
    "name": 123  # Nombre con tipo de dato incorrecto (número en lugar de cadena)
}