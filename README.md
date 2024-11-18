# Proyecto Urban Grocers 


Contenido

Descripción del proyecto 
Lista de comprobación de pruebas
Archivos del Proyecto
Recursos
Objetivos

Descripción del proyecto 
Este proyecto tiene como objetivo automatizar las pruebas de una API destinada a la gestión y creación de kits personalizados para usuarios. Se desarrollaron pruebas que verifican el correcto funcionamiento de los endpoints principales, asegurando la validez de las solicitudes y respuestas, tanto en escenarios positivos como negativos.

Lista de comprobación de pruebas
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
Archivos del Proyecto 
* configuration.py: Configuración de rutas y URL base de la API.
* data.py: Almacenamiento de cuerpos de solicitudes y datos comunes.
* sender_stand_request.py: Implementación de funciones para realizar solicitudes HTTP.
* create_kit_name_kit_test.py: Carpeta que contiene las pruebas automatizadas organizadas por módulos.
* README.md: Este archivo incluye la descripción del proyecto.
* .gitignore: Incluye los archivos que no se deben subir a los repositorios.

Recursos
Lenguaje: Python

Paquetes instalados

requests
pytest

Objetivos 

1 Garantizar la estabilidad y confiabilidad de la API.
2 Identificar y reportar posibles errores en el manejo de solicitudes y respuestas.
3 Facilitar el mantenimiento y escalabilidad del código para futuras extensiones.
