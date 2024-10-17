import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


# Función para realizar una solicitud POST y crear un nuevo kit
def post_new_client_kits(kit_body, auth_token):
    headers_with_auth = data.headers.copy()  # Copia los encabezados originales para evitar modificar el original
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"  # Añade el token de autenticación al encabezado

    kit_response = requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # Ruta completa para crear el kit
        json=kit_body,  # Datos del kit en el cuerpo de la solicitud
        headers=headers_with_auth  # Encabezados que incluyen el token de autorización
    )
    return kit_response  # Retorna la respuesta de la solicitud