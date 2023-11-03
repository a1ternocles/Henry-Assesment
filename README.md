## Producto Minimo Viable (MVP)
# Introduccion del Contenido
Este repositorio busca mostrar adecuadamente el proceso realizado en pro de la replicacion del proyecto y una vista general de los distintos codigos creados para dicho fin.
Nuestro contenido esta basado en distintas etapas:

  * [Objetivo](#objetivo)
  * [Entorno Virtual](#env)
  * [Renderizado y Despliegue](#render)
  * [Recoleccion del Dataset](#dataset_collection)
  * [Procesamiento del Dataset (ETL)](#etl)
  * [Creacion de un analisis exploratorio (EDA)](#eda)
  * [Funciones propuestas y API (API)](#api)
  * [Modelo de machine Learning](#ml)
  * [Creacion de un archivo Main](#main)
  * [Conclusion](#conclusion)

# Objetivo
El proyecto busca desarrollar una API con FastAPI para proporcionar consultas detalladas sobre reseñas de videojuegos, incluyendo estadísticas por género, horas jugadas por usuario, recomendaciones de juegos y análisis de sentimientos. También implica explorar manualmente los datos, crear un modelo de recomendación y desplegar la API en un servicio de alojamiento. El objetivo final es presentar un video demostrativo que muestre el funcionamiento de la API y el modelo de aprendizaje automático.

# Entorno Virtual

Un entorno virtual es un ambiente aislado y autónomo que permite instalar y ejecutar diferentes versiones de programas, bibliotecas y dependencias específicas para un proyecto o aplicación.
Sirve para:

* __Isolar proyectos__: Permite trabajar en varios proyectos con diferentes requerimientos de software sin que entren en conflicto unos con otros.
* __Gestionar dependencias__: Facilita la gestión de las dependencias de un proyecto, ya que se pueden instalar versiones específicas de librerías y herramientas sin afectar el sistema global.
* __Reproducibilidad__: Asegura que un proyecto sea reproducible en diferentes entornos al tener control sobre las versiones de las dependencias.
* __Organización__: Ayuda a mantener orden en el desarrollo al separar claramente las dependencias y versiones utilizadas en un proyecto específico.

__Pasos:__
 1. Crear carpeta de trabajo (Recomendacion: Crear dentro una carpeta llamada __FastApi__ donde se alojaran los archivos)
 2. Abrir el Terminal o CMD
 3. Buscar la carpeta en cuestion usando el comando cd "carpeta_de_trabajo"/FastApi
 4. python3 -m venv fastapi-env
 5. fastapi-env\Scripts\activate.bat
 6. pip install fastapi
 7. pip install uvicorn

De esta manera hemos creado nuestro entorno virtual dentro de la carpeta que hayamos creado.

# Renderizado y Despliegue

Una vez creado nuestra carpeta que contenga todos los archivos con los que trabajaremos, podemos considerar el crear una pagina web y al mismo tiempo desplegarla con el fin de que nuestra API pueda consumirse sin mayor incoveniente.

__Pasos(En la terminal o Git Bash):__

1. Actualizar nuestro entorno: python -m pip install --upgrade pip
2. pip freeze > requirements.txt (Se recomienda copiar el requirement.txt de este repositorio para evitar errores)
3. Crear un repositorio Git Hub: [Como crear un repositorio](https://docs.github.com/es/get-started/quickstart/create-a-repo)
4. Crear una cuenta en Render.com
5. En el apartado __Dashboard__, click en __Web Service__
6. En la seccion: __Public Git Repository__, pegar url del repositorio del paso 3.
7. Name: "Nombre de tu archivo"; Branch: "main"; Runtime: Python 3; Start Command : $ uvicorn main:app --host 0.0.0.0 --port 10000
8. Click: Create Web service

De esta manera concluimos la creacion de tu pagina web. En la parte superior encontraras el link de la pagina. tener en cuenta que debido a que no se ha creado nada aun, estara vacio.

# Recoleccion del Dataset

Con el fin de completar las tareas solicitadas, se hizo entrega de un [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj). Es importante tener en cuenta que la data entregada se encuentra en formato .json.gz. Por lo tanto, una vez descargado el dataset y guardado en nuestra carpeta creada para tal fin, es necesario descomprimir dichos archivos y montarlos en un tipo de formato amigable para poder trabajar.

__Recomendaciones__:

1. Crear una carpeta llamada "data" dentro de nuestro folder principal para tener toda la informacion en un lugar
2. Utilizar pandas para crear dataframes. Esto nos permite ver los archivos como tablas y poder trabajar con dicha libreria

# Procesamiento del Dataset (ETL)

## Nota: 
El orden de este proceso fue creado teniendo en cuenta el patron : Modelo - Vista - Controlador (MVC). Esto nos permite un mayor orden y posicion de todos los elementos que se encuentran en el codigo, ademas

ETL, que significa Extracción, Transformación y Carga, es un proceso fundamental en el ámbito de la gestión y análisis de datos. Consiste en la extracción de datos desde múltiples fuentes, su transformación para ajustarlos, limpiarlos, y estructurarlos de manera coherente, y finalmente, cargarlos en un repositorio o almacén de datos para su posterior análisis. 
Teniendo este concepto en mente, se creo un Notebook llamado __etl,ipynb__ con el fin de convertir nuestros archivos .json.gz a pandas.Dataframe

# Creacion de un analisis exploratorio (EDA)
# Funciones propuestas y API (API)
# Modelo de machine Learning
# Creacion de un archivo Main
# Conclusion



