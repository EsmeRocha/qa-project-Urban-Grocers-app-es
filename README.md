# Proyecto Urban Grocers 


Contenido

1. Descripción del proyecto 
2. Lista de comprobación de pruebas
3. Archivos del Proyecto
4. Recursos
5. Paquetes Instalados
6. Ejecucion de las pruebas
7. Objetivos

1. Descripción del proyecto 
Este proyecto automatiza la validación de un endpoint REST para la creación de kits asociados a 
usuarios/as en un sistema. Incluye pruebas automatizadas para verificar que el endpoint cumple 
con los requisitos especificados, como la longitud del nombre, el manejo de caracteres especiales 
y las validaciones de parámetros obligatorios.

El objetivo principal es garantizar que el backend funcione según las especificaciones, 
implementando un enfoque estructurado para pruebas automáticas usando Pytest.

2. Lista de comprobación de pruebas
№	Description	                                                        ER:
1	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
3	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
4	El número de caracteres es mayor que la cantidad permitida (512):
kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
5	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
6	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400

3. Archivos del Proyecto 
* configuration.py: Configuración de rutas y URL base de la API.
* data.py: Almacenamiento de cuerpos de solicitudes y datos comunes.
* sender_stand_request.py: Implementación de funciones para realizar solicitudes HTTP.
* create_kit_name_kit_test.py: Carpeta que contiene las pruebas automatizadas organizadas por módulos.
* README.md: Este archivo incluye la descripción del proyecto.
* .gitignore: Incluye los archivos que no se deben subir a los repositorios.

4. Recursos
Lenguaje:   Python
Pytest:     Framework para pruebas automatizadas.
Requests:   Librería para enviar solicitudes HTTP.
Git:        Control de versiones.
JSON:       Formato de intercambio de datos.
API REST:   Endpoint para la creación de usuarios/as y kits.


5. Paquetes instalados

a. Clona el repositorio:

git clone https://https//github.com/EsmeRocha/qa-project-Urban-Grocers-app-es
cd proyecto-kits

b. Crea un entorno virtual:

python -m venv venv
venv\Scripts\activate     # Para Windows

6. Ejecucion de las pruebas

a. Verifica que estás en el entorno virtual:

venv\Scripts\activate     # Windows

b. Ejecuta todas las pruebas:

pytest folder/del/proyecto

c. Ejecución de pruebas específicas:

pytest create_kit_name_kit_test.py::test_kit_name_max_char


7. Objetivos 

1 Garantizar la estabilidad y confiabilidad de la API.
2 Identificar y reportar posibles errores en el manejo de solicitudes y respuestas.
3 Facilitar el mantenimiento y escalabilidad del código para futuras extensiones.

Detalles del Autor
Nombre: Esmeralda Rocha Diaz
Sprint: Creación de Kits Sprint 7
Contacto: esmerocio92.erd@gmail.com

