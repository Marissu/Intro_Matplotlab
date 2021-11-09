#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01"><img src = "https://ibm.box.com/shared/static/9gegpsmnsoo25ikkbl4qzlvlyjbgxs5x.png" width = 400> </a>
# 
# <h1 align=center><font size = 5>Introducción a Matplotlib y a las Gráficas de Líneas</font></h1>
# 

# ## Introducción
# 
# El objetivo de estos laboratorios es darte una introducción a la visualización de datos con Python, tan concreto y conciso como sea posible.
# Hablando de consistencia, debido a que no existe la *mejor* librería para visualizar datos en Python – hasta la fecha de creación de estos laboratorios – tendremos que mostrar distintas librerías y ensenar sus beneficios cuando discutamos nuevos conceptos sobre visualización. De esta forma esperamos que los estudiantes se familiaricen con librerías y conceptos para que puedan juzgar y decidir la mejor técnica y herramienta para visualizar dado el problema *y* la audiencia.
# 
# Asegurate de haber completado los requisitos previos para este curso, estos son [**Python Basics for Data Science**](https://www.edx.org/course/python-basics-for-data-science-2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01) and [**Analyzing Data with Python**](https://www.edx.org/course/data-analysis-with-python?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 
# **Observación**: La mayoría de las graficas y visualización serán generadas usando datos almacenados en DataFrames *pandas*. Por consiguiente, en este laboratorio, daremos un curso rápido de *pandas*. Sin embargo, si tienes interés en aprender mas sobre la librería *pandas*, una descripción detallada y explicaciones sobre como limpiar y procesar datos en un dataframe *pandas* están disponibles en nuestro curso [**Analyzing Data with Python**](https://www.edx.org/course/data-analysis-with-python?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 
# ***
# 

# ## Tabla of Contenido
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
# 1.  [Exploración de Conjuntos de Datos con *pandas*](#0)<br>
# 
# 1.1 [El Conjunto de Datos: Inmigración en Canadá desde 1980 a 2013](#2)<br>
# 1.2 [Conceptos básicos de *pandas*](#4) <br>
# 1.3 [Conceptos Intermedios de *pandas*: Indexado y Selección](#6) <br>
# 2\. [Visualizar Datos con Matplotlib](#8) <br>
# 2.1 [Matplotlib: Librería Estándar de Visualización para Python](#10) <br>
# 3\. [Gráficas de Líneas](#12)
# 
# </div>
# <hr>
# 

# # Exploración de Conjuntos de Datos con *pandas* <a id="0"></a>
# 
# *pandas* es un kit de herramientas para el análisis de datos. De su \[sitio web] ([http://pandas.pydata.org/](http://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01)):
# 
# > *pandas* es un paquete de Python que ofrece estructuras de datos rápidas, flexibles y expresivas diseñadas para facilitar el trabajo con datos “relacionales” o “etiquetados”. Su objetivo es ser el bloque de construcción principal para realizar análisis practicas **del mundo real** en Python.
# 
# El curso tiene como base principal el uso de *pandas* para la exploración, análisis y visualización de datos. Te recomendamos invertir un poco de tu tiempo para familiarizarte con la API de referencia de *pandas*:[http://pandas.pydata.org/pandas-docs/stable/api.html](http://pandas.pydata.org/pandas-docs/stable/api.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 

# ## El Conjunto de Datos: Inmigración en Canadá desde 1980 a 2013 <a id="2"></a>
# 

# Fuente de los Datos: [Flujos migratorios internacionales a y desde los países seleccionados – Revisión de 2015 ](http://www.un.org/en/development/desa/population/migration/data/empirical2/migrationflows.shtml?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 
# El conjunto de datos contiene información anual sobre los flujos de migración internacional recopilada por los países de destino. Los datos representan flujos de entrada y salida de acuerdo con el lugar de nacimiento, ciudadanía o lugar de residencia anterior/próxima tanto para extranjeros como nacionales.  La versión actual presenta datos provenientes de 45 paises.
# 
# En esta sesión, nos enfocaremos en los datos Migratorios de Canadá.
# 
# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/coursera/Images/Mod1Fig1-Dataset.png" align="center" width=900>
# 
# Por cuestiones de simplicidad, los datos migratorios de Canadá han sido extraídos y cargados a uno de los servidores de IBM. Puedes obtener los datos desde [aquí](https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 
# ***
# 

# ## Conceptos básicos de *pandas*<a id="4"></a>
# 

# Lo primero que haremos será importar dos módulos esenciales para el análisis de datos: *pandas* y *Numpy*.
# 

# In[1]:


import numpy as np  # muy útil para cálculos científicos con Python
import pandas as pd # Librería para estructar datos primarios


# Vamos a descargar e importar el conjunto principal de datos sobre Inmigración en Canadá utilizando el método *pandas* `read_excel()`. Normalmente, antes de hacerlo, necesitaremos descargar un modulo requerido por *pandas* para poder leer archivos de Excel. Este modulo es **xlrd**. Para tu comodidad, hemos preinstalado dicho modulo. De no ser así, tendrías que ejecutar la siguiente línea de código para instalar el modulo **xlrd**:
# 
# ```
# !conda install -c anaconda xlrd --yes
# ```
# 

# Ahora estamos listos para leer los datos.
# 

# In[4]:


df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')


# Veamos las primeras 5 filas de nuestro conjunto de datos con la función `head()`
# 

# In[3]:


df_can.head()
# tip: puedes especificar el numero de filas que quieres ver de la siguiente manera: df_can.head(10)


# También podemos ver las 5 filas del final en nuestro conjunto de datos con la función `tail()`.
# 

# In[5]:


df_can.tail()


# Cuando se analiza un conjunto de datos, es una buena idea empezar obteniendo información básica sobre tu dataframe. Podemos hacer esto con el método `info()`.
# 

# In[6]:


df_can.info()


# Para obtener la lista de las cabeceras de las columnas podemos hacer uso del parámetro del dataframe `.columns`.
# 

# In[7]:


df_can.columns.values 


# De manera similar para obtener una lista de los índices podemos usar el parámetro  `.index`.
# 

# In[8]:


df_can.index.values


# Observación: El tipo de dato por defecto de los índices y columnas NO es lista (list).
# 

# In[9]:


print(type(df_can.columns))
print(type(df_can.index))


# Para obtener los índices y columnas como tipo lista (list) podemos usar el método `tolist()`
# 

# In[10]:


df_can.columns.tolist()
df_can.index.tolist()

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))


# Para ver las dimensiones del dataframe usamos el parámetro `.shape`.
# 

# In[11]:


# tamaño del dataframe (filas, columnas)
df_can.shape    


# Observación: Los tipos principales almacenados en objetos *pandas* son *float*, *int*, *bool*, *datetime64\[ns]* y *datetime64\[ns, tz] (in >= 0.17.0)*, *timedelta\[ns]*, *category (in >= 0.15.0)*, y *object*. Además estos tipos de datos posen tamaño, por ejemplo int64 and int32.
# 

# Limpiemos el conjunto de datos para retirar columnas innecesarias. Podemos usar el método de *pandas* `drop()` de la siguiente manera:
# 

# In[12]:


# En pandas axis=0 representa filas (por defecto) y axis=1 representa columnas.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)


# Renombremos las columnas para que tengan sentido. Podemos usar el método `rename()` pasándole un diccionario con nombres viejos y nuevos de la siguiente manera:
# 

# In[13]:


df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns


# Vamos a añadir también una columna 'Total' para el numero total de inmigrantes por país a lo largo del periodo 1980 – 2013 de la siguiente manera:
# 

# In[16]:


df_can['Total'] = df_can.sum(axis=1)


# Podemos revisar cuantos objetos vacíos (null) tenemos en el conjunto de datos de esta forma:
# 

# In[17]:


df_can.isnull().sum()


# Para finalizar, veamos un resumen rápido de cada columna en nuestro dataframe usando el método `describe()`.
# 

# In[18]:


df_can.describe()


# ***
# 
# ## Conceptos Intermedios de *pandas*: Indexado y Selección (slicing)<a id="6"></a>
# 

# ### Seleccionar Columna
# 
# **Hay dos maneras de filtrar por el nombre de una columna:**
# 
# Método 1: Rápido y fácil, pero solo funcionará si el nombre de la columna NO tiene caracteres especiales o espacios.
# 
# ```python
#     df.column_name 
#         (returns series)
# ```
# 
# Método 2: Es mas robusto y puede filtrar múltiples columnas.
# 
# ```python
#     df['column']  
#         (returns series)
# ```
# 
# ```python
#     df[['column 1', 'column 2']] 
#         (returns dataframe)
# ```
# 
# ***
# 

# Ejemplo: Hagamos un filtro en la lista de países ('Country').
# 

# In[19]:


df_can.Country  # regresa una serie


# Vamos a filtrar en la lista de países ('OdName') y en los datos para los años 1980 – 1985.
# 

# In[20]:


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # regresa un dataframe
# Observa que 'Country' es una cadena y los años son enteros.
# Con la finalidad de ser consistentes, convertiremos todos los nombres de las columnas a tipo cadenas mas adelante.


# ### Seleccionar Fila
# 
# Existen tres formas principales para seleccionar filas:
# 
# ```python
#     df.loc[label]        
#         #filtra por la etiqueta del índice/columna
#     df.iloc[index]       
#         #filtra por la posición del índice/columna
# ```
# 

# Antes de proceder, observa que el índice por defecto del conjunto de datos es un rango numero desde 0 hasta 194. Esta dificulta hacer una consulta por un país en especifico. Por ejemplo para buscar información de Japón necesitamos su valor de índice correspondiente.
# 
# Esto puede resolverse con facilidad estableciendo la columna 'Country' como índice mediante el método `set_index()`.
# 

# In[23]:


df_can.set_index('Country', inplace=True)
# Tip: Lo opuesto de establecer (set) es reestablecer (reset). Para reestablecer el índice podemos usar df_can.reset_index().


# In[24]:


df_can.head(3)


# In[25]:


# opcional: remueve el nombre del índice
df_can.index.name = None


# Ejemplo: Veamos el numero de inmigrantes japoneses (fila 87) para los siguientes escenarios:
# 1\. El total de filas de datos (todas las columnas)
# 2\. Para el año 2013
# 3\. Para los años 1980 a 1985
# 

# In[27]:


# 1. El total de filas de datos (todas las columnas)
print(df_can.loc['Japan'])

# métodos alternativos
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())


# In[ ]:


# 2. Para el año 2013
print(df_can.loc['Japan', 2013])

# método alternativo
print(df_can.iloc[87, 36]) # el año 2013 esta en la ultima columna con una posición de índice de 36


# In[28]:


# 3. Para los años 1980 a 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])


# Los nombres de las columnas que son enteros (como las de los años) puede provocar cierta confusión. Por ejemplo, cuando hacemos referencia al año 2013 uno pudiera confundirlo con la posición 2013 del índice.
# 
# Para evitar esta ambigüedad, vamos a convertir los nombres de las columnas a tipo cadena: '1980' a '2013'.
# 

# In[29]:


df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- retirar el código comentado para revisar el tipo de dato de las cabeceras de las columnas


# Debido a que convertimos los años a tipo cadena, declaremos una variable que nos permita fácilmente hacer una llamada al rango completo de años:
# 

# In[30]:


# de utilidad para graficar mas adelante
years = list(map(str, range(1980, 2014)))
years


# ### Filtrado basado en Criterios
# 
# Para filtrar un dataframe en base a una condición implemente debemos pasar la condición como vector boleano.
# 
# Por ejemplo, filtremos el dataframe para mostrar los datos acerca de los países asiáticos (AreaName = Asia).
# 

# In[31]:


# 1. crear las series de condiciones boleanas 
condition = df_can['Continent'] == 'Asia'
print(condition)


# In[32]:


# 2. pasar al dataframe esta condición 
df_can[condition]


# In[ ]:


# Podemos pasar múltiples condiciones en la misma línea
# filtremos por AreaNAme = Asia y RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# observación: cuando usamos los operadores 'and' y 'or', panda requiere el uso de '&' y '|' en lugar de 'and' y 'or'
# no olvides poner entre paréntesis las dos condiciones


# Antes de continuar: revisemos los cambios que hemos hecho en el dataframe.
# 

# In[33]:


print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)


# ***
# 
# # Visualizar Datos con Matplotlib<a id="8"></a>
# 

# ## Matplotlib: Librería Estándar de Visualización para Python<a id="10"></a>
# 
# La primera librería para graficado que exploraremos en este curso será [Matplotlib](http://matplotlib.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01). Como se menciona en su sitio web:
# 
# > Matplotlib es una librería para graficar de Python 2D y que produce imágenes y publicaciones de calidad en una variedad de formatos y entornos interactivos a través de varias plataformas. Matplotlib puede usarse con scripts de Python, la Shell de Python y IPython, cuadernos de jupyter, servidores de aplicaciones de web y cuatro kits de herramientas para interfaces graficas de usuario.
# 
# Si quieres crear visualizaciones impactantes con Python, Matplotlib es una herramienta esencial que tienes a tu disposición.
# 

# ### Matplotlib.Pyplot
# 
# Uno de los aspectos centrales de Matplotlib es `matplotlib.pyplot`. Es la capa de scripting de Matplotlib que hemos estudiado en detalle en los videos acerca de Matplotlib. Recuerda que es una colección de funciones de tipo comando que hacen que Matplotlib trabaje junto a MATLAB. Cada función `pyplot` provoca algún cambio en una imagen, p.ej. crear una figura, crear un área de dibujo en una figura, graficar algunas líneas, decorar la grafica con etiquetas, etc. En este laboratorio trabajaremos con la capa de scripting con el fin de aprender a generar graficas de líneas. En próximos laboratorios trabajaremos con la capa de artista también para experimentar de primera mano sus diferencias con la capa de scripting.
# 

# Empecemos importando `Matplotlib` y `Matplotlib.pyplot` de la siguiente manera:
# 

# In[34]:


# se usara el backend en línea
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# \*opcional: revisar si Matplotlib esta cargado.
# 

# In[35]:


print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0


# \*opcional: aplicar un estilo a Matplotlib
# 

# In[36]:


print(plt.style.available)
mpl.style.use(['ggplot']) # opcional: para el estilo tipo ggplot


# ### Graficar con *pandas*
# 
# Afortunadamente pandas tiene una implementación pre cargada de Matplotlib que podemos usar. Graficar en *pandas* es tan simple como añadir un método `.plot()` a una serie o dataframe.
# 
# Documentación:
# 
# *   [Graficación con Series](http://pandas.pydata.org/pandas-docs/stable/api.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01#plotting)<br>
# *   [Graficación con Dataframes](http://pandas.pydata.org/pandas-docs/stable/api.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01#api-dataframe-plotting)
# 

# # Gráficas de Líneas (Series/Dataframe) <a id="12"></a>
# 

# **¿Qué es una grafica de línea y para que se usa?**
# 
# Una grafica de línea muestra información como una seria de puntos de datos llamados 'marcadores' conectados por segmentos de líneas rectas. Es un tipo de grafica común en muchos campos.
# Utiliza graficas de líneas cuando tengas conjuntos de datos continuos. Estas graficas son ideales para visualización que muestran una tendencia de los datos a lo largo de un periodo de tiempo.
# 

# **Empecemos con un caso de estudio:**
# 
# En 2010 Haití sufrió un terremoto catastrófico de 7.0 grados de magnitud. Esto causo devastación y perdidas de vida en grandes áreas y afectando alrededor de tres millones de personas. Como parte de los esfuerzos humanitarios por parte de Canadá, el gobierno acepto refugiados provenientes de Haití. Podemos visualizar rápidamente este esfuerzo con el uso de una grafica de `Línea:`
# 
# **Pregunta:** Dibuja una Grafica de Línea de la inmigración proveniente de Haití usando `df.plot()`.
# 

# Primero, extraeremos la serie de datos de Haití.
# 

# In[37]:


haiti = df_can.loc['Haiti', years] # ejecución en los años 1980 a 2013 para excluir la columna 'total'
haiti.head()


# Después, dibujaremos una grafica de línea anexando `.plot()` al dataframe `haiti`
# 

# In[38]:


haiti.plot()


# *pandas* completó automáticamente el eje x con los valores de los índices (años) y el eje y con los valores de las columnas (población). Sin embargo, observe que los años no se mostraron porque son del tipo cadena. Por lo tanto, modifiquemos el tipo de los valores de índice a entero para su diagramación.
# 
# Además, etiquetemos el eje x y el eje y con `plt.title()`, `plt.ylabel()` y `plt.xlabel()` de la manera siguiente:
# 

# In[39]:


haiti.index = haiti.index.map(int) # cambiemos los valores de índice de Haiti al tipo entero para la graficación
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # esta línea es necesaria para mostrar las actualizaciones en la imagen


# Podemos observar con claridad la mayor cantidad de inmigrantes desde Haití a partir de 2010, año en que Canadá aumentó sus esfuerzos para aceptar refugiados haitianos. Anotemos este pico en el diagrama con el método `plt.text()`.
# 

# In[40]:


haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# anotar el terremoto de 2010.
# sintaxis: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # vea la nota abajo

plt.show() 


# Con unas pocas líneas de código, pudo identificar rápidamente el aumento en inmigración y visualizarlo.
# 
# Una nota rápida sobre los valores de x y de y en `plt.text(x, y, label)`:
# 
# ```
#  Debido a que el eje x (años) es del tipo 'enteros', especificamos x como un año. El eje y (cantidad de inmigrantes) es del tipo 'enteros'; por lo tanto, podemos especificar el valor de y = 6000.
# ```
# 
# ```python
#     plt.text(2000, 6000, '2010 Earthquake') # años almacenados como tipo entero
# ```
# 
# ```
# Si los años se hubieran almacenado como tipo 'cadena', deberíamos especificar x como la posición del índice para el año. P. ej., el índice 20.º es el año 2000, debido a que se trata del año 20.º a partir del año base de 1980.
# ```
# 
# ```python
#     plt.text(20, 6000, '2010 Earthquake') # años almacenados como tipo enteros
# ```
# 
# ```
# Trataremos los métodos de anotación avanzados en módulos posteriores.
# ```
# 

# Podemos agregar fácilmente más países al gráfico de líneas para llevar a cabo comparaciones significativas en la inmigración desde distintos países.
# 
# **Pregunta:** Comparemos la cantidad de inmigrantes desde India y China entre 1980 a 2013.
# 

# Paso 1: Obtenga el conjunto de datos para China e India, y muestre el DataFrame.
# 

# In[41]:


### escribe aquí tu respuesta
df_CI = df_can.loc[['India', 'China'], years]
df_CI.head()


# Haz doble clic **aquí** para ver la solución.
# 
# <!-- The correct answer is:
# df_CI = df_can.loc[['India', 'China'], years]
# df_CI.head()
# -->
# 

# Paso 2: Dibuje el gráfico. Especificaremos explícitamente el gráfico de líneas al ejecutar el parámetro `kind` en `plot()`.
# 

# In[42]:


### escribe aquí tu respuesta
df_CI.plot(kind='line')


# Haz doble clic **aquí** para ver la solución.
# 
# <!-- The correct answer is:
# df_CI.plot(kind='line')
# -->
# 

# ¡Eso no se ve correcto!
# 
# Recuerda que pandas dibuja los índices en el eje x y las columnas como líneas individuales en el eje y. Debido a que `df_CI` es un DataFrame con `country` como índice y years como columnas, debemos primero transponer el DataFrame con el método `transpose()` a fin de intercambiar la fila y las columnas.
# 

# In[43]:


df_CI = df_CI.transpose()
df_CI.head()


# *pandas* creará automáticamente un gráfico con los dos países. Grafique el nuevo DataFrame transpuesto. Asegúrese de agregar un título al diagrama y de etiquetar los ejes.
# 

# In[45]:


### escribe aquí tu respuesta
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')



plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()



# Haz doble clic **aquí** para ver la solución.
# 
# <!-- The correct answer is:
# df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
# df_CI.plot(kind='line')
# -->
# 
# <!--
# plt.title('Immigrants from China and India')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# -->
# 
# <!--
# plt.show()
# --> 
# 

# A partir de la grafica anterior, podemos observar que China e India tienen tendencias inmigratorias muy similares a lo largo de los años.
# 

# *Observación*: ¿Por qué no tuvimos que transponer el DataFrame de Haití antes de diagramarlo (como hicimos con df_CI)? did for df_CI)?
# 
# Porque `haiti` es una serie, en lugar de un DataFrame, y los años son sus índices, como se muestra debajo.
# 
# ```python
# print(type(haiti))
# print(haiti.head(5))
# ```
# 
# > class 'pandas.core.series.Series' <br>
# > 1980    1666 <br>
# > 1981    3692 <br>
# > 1982    3498 <br>
# > 1983    2860 <br>
# > 1984    1418 <br>
# > Name: Haiti, dtype: int64 <br>
# 

# El gráfico de líneas es una herramienta práctica para mostrar varias variables dependientes contra una variable independiente. Sin embargo, no se recomiendan más de 5 a 10 líneas por gráfico. Si hay más líneas, se hace difícil interpretar el gráfico.
# 

# **Pregunta:** Compara la tendencia de los 5 países principales que aportaron la mayor cantidad de inmigrantes a Canadá.
# 

# In[46]:


### escribe aquí tu respuesta
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()


# Haz doble clic **aquí** para ver la solución.
# 
# <!-- The correct answer is:
# \\\\ # Step 1: Get the dataset. Recall that we created a Total column that calculates the cumulative immigration by country. \\ We will sort on this column to get our top 5 countries using pandas sort_values() method.
# \\\\ inplace = True paramemter saves the changes to the original df_can dataframe
# df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
# -->
# 
# <!--
# # get the top 5 entries
# df_top5 = df_can.head(5)
# -->
# 
# <!--
# # transpose the dataframe
# df_top5 = df_top5[years].transpose() 
# -->
# 
# <!--
# print(df_top5)
# -->
# 
# <!--
# \\\\ # Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
# df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
# df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
# -->
# 
# <!--
# plt.title('Immigration Trend of Top 5 Countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
# -->
# 
# <!--
# plt.show()
# -->
# 

# ### Otros gráficos
# 
# ¡Felicidades! Aprendiste a dominar datos con Python y a crear un gráfico de líneas con Matplotlib. Hay muchos más estilos de graficación disponibles, además del gráfico de líneas predeterminado. Puede acceder a todos ellos al ejecutar la palabra clave `kind` en `plot()`. La lista completa de diagramas disponibles es la siguiente:
# 
# *   `bar` para diagramas de barras verticales
# *   `barh` para diagramas de barras horizontales
# *   `hist` para histograma
# *   `box` para diagrama de caja
# *   `kde` o `density` para diagramas de densidad
# *   `area` para diagramas de área
# *   `pie` para diagramas circulares (de pastel)
# *   `scatter` para diagramas de dispersión
# *   `hexbin` para diagramas con agrupamiento hexagonal
# 

# ### ¡Gracias por completar este laboratorio!
# 
# Este cuaderno fue creado originalmente por [Jay Rajasekharan](https://www.linkedin.com/in/jayrajasekharan?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01) con aportes de [Ehsan M. Kermani](https://www.linkedin.com/in/ehsanmkermani?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01) y [Slobodan Markovic](https://www.linkedin.com/in/slobodan-markovic?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 
# Recientemente, esta libreta fue modificada por [Alex Aklson](https://www.linkedin.com/in/aklson/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01). Espero que esta sesión de laboratorio le haya resultado interesante. ¡Si tiene alguna pregunta, comuníquese conmigo!
# 

# Este cuaderno es parte del curso en **edX** llamado *The Data Science Method*. Si tienes acceso a este documento desde fuera del curso, puedes tomarlo en línea haciendo clic [aquí](https://cocl.us/DS0103EN_edX_LAB4).
# 

# <hr>
# 
# Copyright © 2019 [Cognitive Class](https://cognitiveclass.ai/?utm_medium=dswb&utm_source=bducopyrightlink&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ESedX20297760-2021-01-01).
# 
