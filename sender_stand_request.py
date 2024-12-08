import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers={"Content-Type": "application/json"})


# Función para realizar una solicitud POST y crear un nuevo kit
def post_new_client_kits(kit_body):
    create_user_response = post_new_user(data.user_body)
    auth_token = create_user_response.json().get('authToken')
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers
                         )