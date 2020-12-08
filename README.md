# Proyecto Web Scrapping

> En este repositorio se encuentra el contenido de nuestro software de Web Scrapping, con el cual podreís escrapear cualquier sito web que siga el protocolo "htpps".

[![python version](https://img.shields.io/badge/python-v3.7-blue)](https://www.python.org/downloads/)
[![status application](https://img.shields.io/badge/status-stable-brightgreen)](https://github.com/AntoniPizarro/proyecto_dual)

## Tabla de contenidos

1. [Motivación](#motivación)
1. [Tecnologías usadas](#tecnologías-usadas)
1. [Features](#features)
1. [Código de Ejemplo](#codigo-de-ejemplo)
1. [Tests](#tests)
1. [Guia de Uso](#guia-de-uso)
1. [Instalación](#instalación)
1. [Contribución](#contribución)
1. [Colaboradores](#colaboradores)
1. [Licencia](#licencia)
<!---Estado de construcción-->

---

## Motivación

Este proyecto sobre **Web Scrapping** ha sido fruto del trabajo del primer año de _Formación Profesional de Desarrollo Web_. Gracias a la autonomía y participación de sus colaboradores y a la estimulación del reto de sus objetivos.

**[⬆ back to top](#tabla-de-contenidos)**

---

## Tecnologías Usadas

- Python 3
- CSS3
- HTML5
- Mongo DB
- Markdown
- os
- requests
- tkinter
- MongoClient

**[⬆ back to top](#tabla-de-contenidos)**

---

## Features

- [x] Escrapea páginas "https"
- [x] Almacena la información en una base de datos
- [x] No se requiere registro o inicio de sesión
- [x] Dispone de GUI
- [ ] Actualizaciones automáticas
- [ ] Ejecución automática

**[⬆ back to top](#tabla-de-contenidos)**

---

## Instalación

1. Primero de todo crearemos un directorio y a continuación nos situamos en él desde nuestra terminal o consola.

2. Copiamos la url que proporcionamos a continuación y nos aseguraremos de clonar el repositorio en el directorio que acabamos de crear.

3. Para clonar el repositorio en el directorio, asegurándonos que nos encontramos en el interior del repositorio deseado, ejecutamos el siguiente comando:

> git clone https://github.com/AntoniPizarro/proyecto_dual.git

4. A continuación podemos proceder con su uso tan solo accediendo al directorio “resources” y ejecutando el archivo llamado “interface.py”

**[⬆ back to top](#tabla-de-contenidos)**

---

## Guia de Uso

A continuación explicaremos los conceptos necesarios para poder usar la _interfaz gráfica_ (GUI), la cual nos permitirá ejecutar todas las funcionalidades de nuestro programa.

1. Primero de todo accedemos al directorio _“resources”_, en el cual encontraremos el archivo _“interface.py”_ y procedemos a ejecutarlo, haciendo doble clic sobre él o pulsando botón izquierdo y seleccionando la opción _“abrir”_.

2. A continuación podremos observar que se nos habre la consola, aunque mantendrá la pantalla en negro y al mismo tiempo se nos abrirá otra pestaña conteniendo la GUI de nuestra aplicación.

3. En el borde superior de la GUI podemos identificar tres pestañas diferentes:

   - Scrap
   - Generar Productos
   - Ayuda

##### **Scrap**

Al seleccionar la pestaña Scrap observamos que la apariencia de nuestra GUI cambia. Aparece una casilla en blanco con una etiqueta que pone “url” y también podemos localizar un botón con el nombre “Insertar en la BD”.
En la casilla en blanco introduciremos cualquier url de una página web de nuestro sitio web.
Después de haber introducido la url y de pulsar el botón, el programa recogerá toda la información de los servicios y los subirá a la base de datos.
Llegados a este punto, probablemente el título de la ventana de la GUI nos informe de que el programa no responde, pero es totalmente normal ya que está trabajando en segundo plano.
Durante el proceso, en la consola o terminal va apareciendo la información de los servicios en estructura json, y que a su vez nos indica si se guarda en la base de datos o se ha actualizado un documento ya existente.

#### Generar Productos

Al hacer clic sobre esta pestaña podemos ver que aparece un menú desplegable con tres opciones a elegir, las tres opciones que nos muestra son:

- Generar en sitio WEB
- Generar en MongoAtla
- Generar en sitio WEB y MongoAtlas

Las tres opciones nos mostrarán la misma distribución en pantalla pero debemos saber de antemano que no ejecutan los mismo procesos.

Cualquiera de las tres opciones nos creará un archivo que contendrá un servicio, el cual pensamos incluir en nuestra página web, base de datos o ambas, conteniendo las especificaciones que nosotros le hayamos asignado a ese servicio en particular. Disponemos de distintos campos, algunos de ellos requerirán que se rellenen manualmente, seleccionando sobre ellos o escribiendo el contenido que creamos adecuado para el servicio. Tendremos un apartado donde se mostrarán distintas casillas para elegir las características que tiene el servicio que pensamos incluir. A continuación explicaremos el estandarte convencional para rellenar los campos de forma adecuada para la comprensión del cliente y para su correcta visualización:

- Modelo: nombre del vehículo de nuestro servicio.
- Tasa: precio del servicio.
- Marca: filiación del nuevo servicio.
- Color: color del cual está compuesto en su mayoría.
- Gama: grado de calidad.
- Plazas: capacidad de pasajeros del vehículo.
- Texto alternativo imagen: texto con más conveniencia para visualizarse en caso de que el navegador no pueda cargar la imagen.
- url imagen: dirección de la imagen.
- Características: hay 15 casillas que se pueden seleccionar. Se pueden seleccionar hasta 6.

###### Generar en sitio web

Nos da la opción de crear archivos HTML que contendrán las especificaciones que nosotros le hayamos querido dar a nuestro nuevo servicio. Este archivo se generará en el directorio en el que se encuentran el resto de servicios.

###### Generar en mongoAtlas

Nos da la opción de crear archivos JSON que contendrán las especificaciones que nosotros le hayamos querido dar a nuestro nuevo servicio. El documento JSON se generará sobre nuestra base de datos en la colección donde tenemos todos los productos de los que hemos recogido la información o tenemos intención de recoger información de la página web.

###### Generar en sitio web y mongo Atlas

Es la mezcla de las funcionalidades de las dos pestañas anteriores.

**[⬆ back to top](#tabla-de-contenidos)**

---

## Contribución

> Para contribuir en nuestro proyecto, simplemente deberás seguir los siguientes pasos:

1. Clona el repositorio (https://github.com/AntoniPizarro/proyecto_dual.git)
2. Crea tu rama "feature" (git checkout -b feature/<nombre colaborador>)
3. Haz un commit de tus cambios (git commmit -m "Añadiendo nuevo contenido")
4. Haz un push de la rama que has creado (git push origin feature/myBranch)
5. Finalmente en el caso de que la aportación sea lo suficientemente valiosa como para poder considerarse una mejora del programa original se creará una “pull request” para poder incluir los cambios en la rama principal del proyecto a la cual cualquier persona puede tener acceso

**[⬆ back to top](#tabla-de-contenidos)**

---

## Colaboradores

- [Ver Colaboradores](https://github.com/AntoniPizarro/proyecto_dual/pulse)

**[⬆ back to top](#tabla-de-contenidos)**

---

## Licencia

MIT License

Copyright (c) 2020 AntoniPizarro and Pau Llinàs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**[⬆ back to top](#tabla-de-contenidos)**
