#
# Iniciativa BotsiTech (Backend)
Por: Leonardo Patiño Rodriguez
## &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/download/releases/3.7/)

## Modelo de Datos
Modelo: https://dbdiagram.io/d/62a4d75a9921fe2a96e58872
<p align="justify">
Dado que centralizar todas las necesidades de los clientes en un solo modelo de datos puede ser muy complejo, se construye primero un modelo de datos base llamado core en donde contenga la funcionalidad simple y estándar (de fábrica) en donde se pueda instanciar y posteriormente escalar añadiendo nuevas tablas y relaciones de acuerdo a las necesidades puntuales de cada cliente.
</p>
<p align="justify">
Este modelo de datos tendrá dos momentos, el momento 1 es el diseño de las tablas del core en un diagrama lógico, tendrán tablas y campos estándar de cualquier tipo de negocio, con el fin de que se pueda reutilizar para cada tipo de cliente que tenga su lógica de negocio. El momento 2 será crear también un modelo de datos lógico en donde se reutilice el modelo core y se agreguen nuevas tablas y relaciones de acuerdo a la lógica de negocio del cliente.
</p>
<p align="justify">
Como propuesta este core va a estar centralizado en donde sea el mismo para todos los clientes.
</p>
<p align="justify">
Las tablas serán desacopladas y solo vivirán en el ecosistema de su naturaleza, ejemplo tabla intents vivirá en el servicio experto.
</p>

## Modelo NLP y Experto
<div align="center">
	<img height="700" src="https://leoesleoesleo.github.io/imagenes/botsi_flujo.PNG" alt="PokeAPI">
</div>  

Artículo NPL
https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077


## Documentación Apiary
Archivo: apiary.apib
https://app.apiary.io/simulador/editor

## API Rest

[POST] https://127.0.0.1:8000/botsitech/chat/bot

- Request
	```
	{
		"customer_id": 1,
		"phone": "3004971591",
		"sentence": "hola"
	}
	```
- Response
	```
	{
	  "model_tag": "saludo",
	  "chat_rn": "[NO]",
	  "response_inventory": [],
	  "response_nlp": "Hola ¿qué puedo hacer por ti?",
	  "response_expert": "",
	  "response_step": [
	    [
	      "Menu del dia",
	      "Productos",
	      "Combos"
	    ]
	  ],
	  "respose_order": ""
	}
	```
	
- Conociendo el response


<strong>- model_tag:</strong> <p align="justify">El  tag es la predicción del modelo de machine learning que ayuda a conocer la intención del usuario al escribir una sentence, el programa tomará un patterns aleatorio para responder.</p>

	
	{
		"tag": "saludo",
		"patterns": [
			"Hola",
			"Oye",
			"Cómo estás",
			"¿Hay alguien ahí?",
			"Hola",
			"Buenos días"
		],
		"responses": [
			"Hola gracias por visitar",
			"Hola ¿qué puedo hacer por ti?",
			"Hola ¿cómo puedo ayudar?"
		]
	}
	

<strong>- chat_rn:</strong> Regla de negocio para el front, es la comunicación entre el backend y el forntend.

    |  RN  | DESCRIPTION 	
    
    | [NO] | RN_COMMON 		
    | [EL] | RN_PRODUCT_DELETE 	
    | [OP] | RN_OPTIONS_QUANTITY 	
    | [AG] | RN_PRODUCT_ADD 		
    | [OB] | RN_OBSERVATION 		
    | [DE] | RN_DELETE_LIST_PRODUCT 	
    | [EP] | RN_SALE_ORDER 	
    | [EN] | RN_CANCELED_ORDER 	

<strong>- response_inventory:</strong> Respuesta de todo lo relacionado con productos o servicios.

<strong>- response_nlp:</strong> Patterns propuesto por el modelo de machine learning.

<strong>- response_expert:</strong> Respuesta de todo lo relacionado con Confirmación de pedido, Enviar pedido, Eliminar productos y agregar Observación.

<strong>- response_step:</strong> Opciones de recomendación de la tabla expert_steps.

<strong>- respose_order:</strong> Información del pedido solicitado por el usuario, este es el que se guarda en la tabla customer_orders.


## Manual de instalación

### Pasos

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/03_project_botsitech.git
	```
- Crear entorno virtual

    Ejemplo anaconda
	```
	conda create -n env_botsi python=3.7
	```
	```
	conda activate env_botsi
	```
    Ejemplo virtualenv
    ```
	pip install virtualenv
	```
	```
	python3 -m venv env_botsi
	```
	```
	\Scripts\activate
	```
	

- Navegar hasta la carpeta del proyecto en la carpeta requirements para instalar dependencias
    ```
    pip install -r requirements.txt
    ```

- Crear archivo de variables de entorno .env basado en .env.example

- Solo si va crear su bd local: migrar la base de datos, en la altura del archivo manage.py
    ```
   python manage.py makemigrations
    ```
    ```
   python manage.py migrate
    ``` 

- Crear super usuario en auth_user, en la altura del archivo manage.py
    ```
   python manage.py createsuperuser
    ```
    
- Ejecutar Fixtures, en la altura del archivo manage.py
    ```
   python manage.py loaddata fixtures/*.json
    ```

- Si no funciona el comando anterior hacerlo uno por uno.
    ```
   python manage.py loaddata fixtures/data_customer_customer.json
   python manage.py loaddata fixtures/data_consumer_consumer.json
   python manage.py loaddata fixtures/data_customer_coverage.json
   python manage.py loaddata fixtures/data_customer_group.json
   python manage.py loaddata fixtures/data_expert_category.json
   python manage.py loaddata fixtures/data_expert_inventory.json
   python manage.py loaddata fixtures/data_expert_step.json
   python manage.py loaddata fixtures/data_nlp_intentions.json
    ```

- Entrenar Modelo (Opcional, ya está entrenado)
    ```
   python manage.py shell_plus
    ```
    ```
   from integration.nlp.services import train_nlp
    ```
    ```
   train_nlp(customer_id="1")
    ```

- Ejecutar pruebas unitarias (Opcional)
   ```
   pytest -v  
    ``` 

- Validar cobertura de la aplicación (Opcional)
    ```
   coverage run -m pytest -v -p no:cacheprovider --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html  
    ```    
    
- Levantar servicio
    ```
   python manage.py runserver
    ```

- Administrar Usuarios (Opcional)
    ```
   http://127.0.0.1:8000/admin/
    ```

-  Iniciar programa en el navegador con APIView
    ```
   https://127.0.0.1:8000/botsitech/chat/bot
    ```

- Levantar ChatBot desde el Shell (Opcional)
    ```
   python manage.py shell_plus
    ```
    ```
   from integration.chat.services import main_chat
    ```
    ```
   main_chat(customer_id=1,phone="3004971594", sentence="hola", debug=True)
    ```
