# Tercera Entrega

## Instrucciones
# 
### Objetivos Generales

✔ Desarrollar una WEB Django con patrón MVT subida a Github.

Se debe entregar

✔ Link de Github con el proyecto totalmente subido a la plataforma.

✔ Proyecto Web Django con patrón MVT que incluya:

    1. Herencia de HTML.
    2. Por lo menos 3 clases en models.
    3. Un formulario para insertar datos a todas las clases de tus models.
    4. Readme que indique el orde en el que se prueban las cosas y/o donde están las funcionalidades.
---

## Descripción
#
Repositorio correspondiente a la tercera entrega del curso Python de Coderhouse.
Proyecto de desarrollo de Web con Django con patrón MVT.

---

## Requisitos mínimos para ejecutar el código
#
    1. Visual Studio Code
    2. Git


---
## Instrucciones para ejecutar el proyecto
#
Para el correcto funcionamiento del proyecto se recomienda seguir las instrucciones a continuación:


`Generación del proyecto en repositorio local`

- Creación de carpeta del proyecto

Se recomienda crear una carpeta en el ordenador donde se vaya a ejecutar el proyecto. Posteriormente se debe abrir dicha carpeta en el editor de código Visual Studio Code.

- Ubicar la carpeta del proyecto en la terminal

Mediante el comando cd se debe ubicar la carpeta generada.

- Clonar repositorio desde Github

Se debe clonar el repositorio alojado en Github. Para ello se debe ejecutar el siguiente comando en la terminal del VSC:

> git clone https://github.com/PalaciosBeltran/Coder_Python.git

`Preparación del entorno del proyecto`

- Crear un entorno virtual

Se debe generar un entorno virtual donde se instalarán las dependencias requeridas para el proyecto. 

>python -m venv .venv

- Instalar Django en el entorno virtual

Se procede a instalar Django en el entorno virtual creado en el paso anterior.

>pip install Django

- Activar el entorno virtual

Una vez ubicado en la carpeta del proyecto, carpeta donde debe encontrarse el entorno virtual llamado .venv se debe ejecutar el siguiente comando en la terminal para empezar a trabajar en el proyecto:

> .\venv\scripts\activate

`Ejecución del proyecto`

Una vez instaladas las dependencias y el entorno virtual requerido, procederemos a ejecutar nuestro proyecto de desarrollo web mediante el siguiente comando:
>python manage.py runserver

Una vez se inicia el servidor se puede ingresar a la web desarrollada en el puerto http://127.0.0.1:8000/

`Pruebas de funcionamiento`

- Homepage o inicio

Desde la esquina superior izquierda en "Descubre Colombia" o en el navbar en "Inicio" podemos ir al homepage de nuestra web.

- Menú de destinos

Para ir a los destinos podemos ingresar en el inicio en el botón que indica "...empieza hoy!" o directamente en el navbar en la opción "Destinos".

En la página de inicio de destinos se pueden ubicar los primeros cuatro elementos registrados en nuestra base de datos (ya con data precargada desde Github).

En la parte inferior podemos ingresar a "...Ver todos los destinos!" para listar todos los elementos de nuestra base de datos en la categoría destinos. Allí contamos con un botón que nos permite regresar a nuestra página de inicio de destinos.

También podemos ingresar en "...Solicita un destino diferente!" donde se puede crear un elemento adicional a los que se encuentran en la lista precargada y el sistema lo ingresará automáticamente. Para probar esta función se puede copiar y pegar la siguiente data:

1. Nombre: Cúcuta
2. Departamento: Norte de Santander
3. Descripción: Cúcuta es una ciudad de turismo de paso, de compras y de negocios. Tiene una actividad comercial muy activa por el intercambio de productos entre Colombia y Venezuela.
4. Foto: https://www.colombiaturismo.com.co/img/900/cucuta-colombia.jpg

- Menú de servicios o productos

De la misma manera que con los destinos, podemos ingresar al menú de servicios desde nuestro navbar seleccionando la opción "Servicios".

Allí observaremos los cuatro primeros elementos de nuestra base de datos de servicios y podemos listar todos desde el botón "...Ver todos los servicios disponibles!" o ingresar un servicio nuevo ingresando en el botón "...Solicita un servicio diferente!". Para probar esta función se puede ingresar los siguientes datos:

1. Nombre: Actividades
2. Descripción: Aquí puedes encontrar una gran variedad de actividades, excursiones, tickets y atracciones para disfrutar al máximo de tu destino favorito.
3. Foto: https://img.europapress.es/fotoweb/fotonoticia_20220627125150_420.jpg
