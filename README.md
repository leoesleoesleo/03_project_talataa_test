#
# Test Talataa (Backend)
Por: Leonardo Patiño Rodriguez
## &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/download/releases/3.7/)

## Diseño modelado de datos
Modelo: https://dbdiagram.io/d/6383a24fc9abfc61117575bf
<p align="justify">
Modelo de datos, utilizando el ORM que proporciona Django, tomando como base la tabla auth_user.
</p>
<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/diagrama_datos_talataa.PNG" alt="Talataa">
</div>

## API REST con sus endpoints.

[POST] http://localhost:8000/api/token/

- Response
	```
	{
		"refresh":
		"access":
	}
	```

[POST] https://127.0.0.1:8000/orders/request

- Request
	```
	{
		"email": "test@gmail.com",
		"time_zone": 8,
		"direction": "cr 1a 11 11",
		"order": {
			"test_order":"test_order" 
		}
	}
	```
- Response
	```
	{
		"response": "success",
		"data": {
			"email": "test@gmail.com",
			"deliver_date": "2022-11-28T18:26:25.613925",
			"date_order": "2022-11-28T10:26:25.960909",
			"dispatcher": 3
		}
	}
	```


[GET] https://127.0.0.1:8000/orders/request

- Request
	```
	{
		"dispatcher_id": 1,
		"date_order": "2022-11-27"
	}
	```
- Response
	```
	{
		"date_order": "2022-11-27",
		"status": [
			0,
			0,
			0,
			0
		],
		"orders": [
			{
				"test_order": "test_order"
			},
			{
				"test_order": "test_order"
			},
			{
				"test_order": "test_order"
			},
			{
				"test_order": "test_order"
			}
		]
	}
	```
- Conociendo el response

<p align="justify">
	Status 0 : Pedido PENDING Pendiente
	Status 1 : Pedido DELIVERED Entregado
</p>


## Arquitectura de aplicación en Python
<p align="justify">
<strong>Arquitectura Hexagonal</strong>
</p>
<p align="justify">
El principal motivo para separar nuestra aplicación en dos capas (Customer, Orders ) es que cuente con su propia responsabilidad. De esta manera consigue desacoplar capas de nuestra aplicación permitiendo que evolucionen de manera aislada. Además, tener el sistema separado por responsabilidades nos facilitará:
</p>

- La reutilización y mantenibilidad
- Pruebas unitarias
- Más tolerantes a cambios (Responsabilidad única)
- Desacoplamiento

## Uso de buenas prácticas.
<p align="justify">
<strong>Implementación de principios solid</strong>
</p>

- Principio de Responsabilidad Única
- Principio de Inversión de Dependencias

<p align="justify">
<strong>Flake8 - Isort</strong>
</p>

<p align="justify">
Implementación de flake8 e Isort para estandarización y limpieza de código. 
</p>

## Patrones de diseño utilizados.
<p align="justify">
<strong>3 Capas</strong>
</p>
<p align="justify">
Un patrón común como la arquitectura de 3 niveles, donde la aplicación se divide en capa de presentación, capa lógica y capa de datos.
</p>

## Despliegue de proyecto en cualquier tipo de nube.
<p align="justify">
<strong>AWS</strong>
</p>

- RDS - Mysql: 
- EC2 - Linux AWS

<p align="justify">
Ip pública: http://18.213.118.152:8000/admin/ 
</p>
<p align="justify">
Se implementa una arquitectura cloud básica en la capa gratuita de AWS en donde los servicios se encuentran en una misma región en una VPC estándar, el RDS tiene acceso al público y el EC2 solo permisos por IP. para poder ver la app será necesario compartir la ip pública de la máquina donde se quiere ver la aplicación.
</p> 

## Documentación Apiary
Archivo: apiary.apib
https://app.apiary.io/simulador/editor



## Manual de instalación

### Pasos

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/03_project_talataa_test.git
	```
- Crear entorno virtual

    Ejemplo anaconda
	```
	conda create -n env_project_talataa python=3.7
	```
	```
	conda activate env_project_talataa
	```
    Ejemplo virtualenv Linux
    ```
	pip install virtualenv
	```
	```
	python3 -m venv env_project_talataa
	```
	```
	source env_project_talataa/bin/activate
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
   python manage.py loaddata fixtures/data_customer_customer.json
   python manage.py loaddata fixtures/data_customer_direction.json
   python manage.py loaddata fixtures/data_orders_dispatcher.json
   python manage.py loaddata fixtures/data_orders_orders.json
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

- Administrar Usuarios desde el panel admin Django(Opcional)
    ```
   http://127.0.0.1:8000/admin/
    ```

-  Iniciar programa en el navegador con APIView
    ```
   https://127.0.0.1:8000/orders/request
    ```
