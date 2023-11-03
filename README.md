## Producto Minimo Viable (MVP)
# Introduccion del Contenido
Este repositorio busca mostrar adecuadamente el proceso realizado en pro de la replicacion del proyecto y una vista general de los distintos codigos creados para dicho fin.
Nuestro contenido esta basado en distintas etapas:

  * [Objetivo](#objetivo)
  * [Entorno Virtual](#entorno-virtual)
  * [Renderizado y Despliegue](#renderizado-y-despliegue)
  * [Recoleccion del Dataset](#recoleccion-del-dataset)
  * [Procesamiento del Dataset](#procesamiento-del-dataset)
  * [Analisis Exploratorio](#analisis-exploratorio)
  * [Funciones propuestas y API](#funciones-propuestas-y-api)
  * [Modelo de machine Learning](#modelo-de-machine-learning)
  * [Archivo Main](#archivo-main)
  * [Conclusion](#conclusion)

# Objetivo
El proyecto busca desarrollar una API con FastAPI para proporcionar consultas detalladas sobre reseñas de videojuegos, incluyendo estadísticas por género, horas jugadas por usuario, recomendaciones de juegos y análisis de sentimientos. También implica explorar manualmente los datos, crear un modelo de recomendación y desplegar la API en un servicio de alojamiento. El objetivo final es presentar un video demostrativo que muestre el funcionamiento de la API y el modelo de aprendizaje automático.

## Enlaces:
* [Deployment](https://andresruiz-deploy.onrender.com/)
* [Docs & Funciones](https://andresruiz-deploy.onrender.com/docs)
* [Video]()

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

# Procesamiento del Dataset

Se creo un Notebook llamado __etl,ipynb__ con el fin de convertir nuestros archivos .json.gz a pandas.Dataframe. Ademas, se crearon multiples funciones que nos ayudaron al ordenamiento, tranformacion y visualizacion de los distintos formatos encontrados en los archivos originales. Una vez los datos fueron transformados, estos fueron cargados como archivos tipo .parquet con el fin de ahorrar todo el espacio posible.

__Funciones:__
1. def json_double_a_df(json_file)
2. def json_simple_a_df(json_file)
3. def diccionario_tipos_datos(dataframe_file)
4. def cambio_a_float(dato)
5. def cambio_a_datetime(dato)
6. def abrir_lista(dataframe_file,nombre_col)

## Nota: 
El orden de este proceso fue creado teniendo en cuenta el patron : Modelo - Vista - Controlador (MVC). Esto nos permite un mayor ordenamiento y posicion de todos los elementos que se encuentran en el codigo.
El patron creado es llamado: Libreria - Acciones - Vistas (LAV)

# Analisis Exploratorio

Se creo un Notebook llamado __eda.ipynb__ con el fin de explorar nuestros datos y tener una vision de que esta pasando con estos. Es importante resaltar que se busca informacion util como: Outliers, Quartiles, Moda, Media, Mediana, etc. Ademas, por cada analisis o grafica creada dentro del archivo, hay pequenas observaciones al final de estos con la intencion de dar una perspectiva de los datos.

__Funciones:__
1. def df_bool(dataframe_file, col, year, bool)
2. def analisis_sentimiento(data)

## Nota: 
El orden de este proceso fue creado teniendo en cuenta el patron : Modelo - Vista - Controlador (MVC). Esto nos permite un mayor ordenamiento y posicion de todos los elementos que se encuentran en el codigo.
El patron creado es llamado: Libreria - Acciones - Vistas (LAV)

# Funciones propuestas y API

Se creo un Notebook llamado __api.ipynb__ con el fin de crear todas aquellas funciones propuestas dentro del repositorio [PI_ML_OPS](https://github.com/soyHenry/PI_ML_OPS/tree/PT). Ademas, tambien se crearon datasets que pueden ser utiles al momento de llamar a dichas funciones, estos datasets nos permiten ahorrar recursos de la maquina. Se da una introduccion de lo que se plenea usar para poder consumir nuestra API y se generan pruebas para verificar la funcionalidad.

__Funciones:__
1. def PlayTimeGenre(genero: str)
2. def UserForGenre(genero : str)
3. def UsersRecommend(anio : int)
4. def UsersNotRecommend(anio : int)
5. def sentiment_analysis(anio : int)

## Nota: 
El orden de este proceso fue creado teniendo en cuenta el patron : Modelo - Vista - Controlador (MVC). Esto nos permite un mayor ordenamiento y posicion de todos los elementos que se encuentran en el codigo.
El patron creado es llamado: Libreria - Acciones - Vistas (LAV)

# Modelo de machine Learning

Se creo un notebook llamado __ml_model.ipynb__ en el cual nuestra intencion principal es la de crear un modelo de machine learning que nos permita desarrollar una recomendacion item-item teniendo como base el codigo ID de algun juego que se encuentre en el dataset. Esto es, permite sugerir elementos con generos similares a aquellos usuarios que han interactuado con un juego en especifico. Dentro del modelo se usa la __Similitud del coseno__ con el fin de calcular el parecido entre distinto datos y asi obtener el Output que estamos buscando. Es de resaltar que este modulo hace los calculos entre vectores, por tanto vectorizamos nuestro datos usando el modulo __TfidfVectorizer__.

__Funciones:__
1. def recomendacion_juego(id_producto)

## Nota: 
El orden de este proceso fue creado teniendo en cuenta el patron : Modelo - Vista - Controlador (MVC). Esto nos permite un mayor ordenamiento y posicion de todos los elementos que se encuentran en el codigo.
El patron creado es llamado: Libreria - Acciones - Vistas (LAV)

# Archivo Main

Se creo un archivo llamado main.py. En este documento se trajeron las librerias necesarias, se creo un pequeno codigo PHP y ademas se trajeron todas las funciones creadas con anterioridad. Nuestra pagina web puede leer este documento y traer todo el trabajo realizado previamente y asi ser consumido por la API para darnos un resultado.

__Funciones:__
1. def PlayTimeGenre(genero: str)
2. def UserForGenre(genero : str)
3. def UsersRecommend(anio : int)
4. def UsersNotRecommend(anio : int)
5. def sentiment_analysis(anio : int)
6. def recomendacion_juego(id_producto)

Podemos decir que este MVP nos permitio poner en practica todo lo aprendido durante el curso de Henry. Pudimos crear un proceso de ETL en el dataset provisto, un analisis exploratorio que nos da importantes insights sobre el negocio, funciones que nos permiten obtener datos que nos interesan, un modelo de machine learning que nos da recomendaciones teniendo en cuenta el genero de un juego en especifico y el deployment de nuestra pagina web que permite a cualquier usuario hacer uso de todo aquello por lo que hemos trabajado.

# Enlaces

