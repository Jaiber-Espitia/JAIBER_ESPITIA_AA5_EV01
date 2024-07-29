# Sistema de autenticación de usuarios

Aplicación web para el registro y autenticación, el cual permitirá llevar un control del acceso a los usuarios, cuenta con un sistema para la creación de una cuenta de usuario, inicio de sesión y un restablecedor de contraseña en caso de olvidarla, para acceder a la sección de productos el usuario deberá estar logeado ya que algunas vistas están protegidas.


## Tecnologías usadas

- Python versión 3.8.5
- Framework Django versión 4.2.5
- Bootstrap versión 5.3
- CSS
- HTML5
- IDE (Visual studio code)
- GIT versión 2.37.2.windows.2


## Instalación

1. Clona este repositorio: `https://github.com/AndresSilverall/User-authentication-system.git`
2. Navega a la carpeta del proyecto: `cd User-authentication-system`
3. Ejecuta un entorno virtual de Python para la ejecución de la App


### Instalar un entorno virtual en Python

- Instalar desde el gestor de paquetes de Python: `pip install venv`
- Crear un entorno virtual: `python -m venv venv`
- Navegar al entorno virtual creado: `cd venv`
- Luego ingresar a `cd Scripts`
- Presionar `activate` dentro de la carpeta `Scripts` para activar el entorno virtual
- Una vez ya activado el entorno virtual deberá volver a la carpeta raíz del proyecto
- Desde la carpeta raíz del proyecto instalar todas las dependencias de la aplicación con `pip install -r requirements.txt`

4. Ejecuta el servidor de desarrollo: `python manage.py runserver`
5. Abre tu navegador y ve a: `http://127.0.0.1:8000/`


## Pruebas de software (Unit Testing)

La aplicación cuenta con diferentes módulos como lo son los formularios, vistas, rutas (URLs), templates y modelos, para verificar el correcto funcionamiento de cada módulo por separado se aplicaron pruebas unitarias (Unit Testing), se aplicó un total de 16 de casos de pruebas, en las que se llevaron a cabo pruebas de éxito y pruebas de error.

### Aplicacion de pruebas unitarias a cada componente (algunos ejemplos)


#### Vistas

- Comprobar que la vista home debe retornar un codigo de estado HTTP de tipo 200  ✓

- Comprobar que la vista home no debe retornar un codigo de estado HTTP de tipo 404  ✓

- Comprobar que la vista home tiene asociado el template 'home.html'  ✓


#### Modelos

- Comprobar que el objeto 'product_one' es una instancia del modelo 'Products'  ✓

- Comprobar que el modelo con la columna 'name' cuenta con una tupla  ✓

- Comprobar que el  nombre del producto dentro del modelo de pruebas cuenta con un nombre igual a 'Iphone 14'  ✓

- Comprobar que el precio del producto dentro del modelo de pruebas es menor a 5.000.000  ✓


#### URLS

- Comprobar que la URL 'logout' tiene asociada la función 'logout_user'  ✓

- Comprobar que la URL 'home' tiene asociada la función 'home'  ✓


#### Formularios

- Comprobar que los datos ingresados en el formulario de registro de usuario son validos  ✓

- Comprobar que los datos ingresados en el formulario de registro de usuario son invalidos  ✓

- Comprobar cuando el usuario envie los datos en el formulario de registro este debe retornar un codigo de estado HTTP de tipo 200 ✓



Para correr los tests unitarios ejecuta el siguiente comando: `python manage.py test Authenticate -v 2`


#### Resultados de las pruebas

<img src="assets/tests_success.png" alt="tests_success.png" width="680">


## App en ejecución

### Creación de usuario
<img src="assets/create.gif" alt="create.gif" width="730">


### Campos incorrectos 
<img src="assets/create_user_error.gif" alt="create_user_error.gif" width="730">


### Login
<img src="assets/login_user.gif" alt="login_user.gif" width="730">


### Usuario o contraseña incorrectos
<img src="assets/login_user_error.gif" alt="login_user_error.gif" width="730">


### Cambiar contraseña
<img src="assets/change_password.gif" alt="change_password.gif" width="730">


### Error de cambio de contraseña
<img src="assets/reset_password_error.gif" alt="reset_password_error.gif" width="730">


### Sección de productos (El usuario deberá estar autenticado para acceder)
<img src="assets/products.gif" alt="products.gif" width="730">


### Cerrar sesión
<img src="assets/logout.gif" alt="logout.gif" width="730">

