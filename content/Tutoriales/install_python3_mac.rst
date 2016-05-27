Instalar Python 3 en Mac OS X
=============================

:date: 2016-05-27 10:00
:tags: Mac, OS X, Python, instalación
:slug: python-mac
:author: taniaka

¿Tienes un Mac y quieres empezar a utilizar Python? ¡Fenomenal! En este post te explicaremos los primeros pasos que tienes que dar.

Por defecto, tu Mac viene con Python 2 preinstalado. Sin embargo, nosotros vamos a trabajar con Python 3. ¿Por qué? Aunque muchos proyectos siguen utilizando Python 2, el futuro está en Python 3 y la `wiki oficial de Python`_ nos dice claramente que *Python 2.x is legacy* (Python 2.x está anticuado). Además, Python 3 nos ofrece más facilidades para gestionar cadenas de texto y esto es una gran ventaja para nuestra labor lingüística. Así que, ¡a por Python 3!

.. _`wiki oficial de Python`: https://wiki.python.org/moin/Python2orPython3

El Terminal
---------------
Todas nuestras manipulaciones las haremos desde el Terminal de nuestro Mac. Si nunca has usado el Terminal, no te preocupes, es muy sencillo.

Para abrir el Terminal, simplemente tienes que teclear *Terminal* en el Finder o en el Spotlight, y darle un click. Se te abrirá una ventana de este estilo:

.. figure:: {filename}/images/mac-python3-1.png
   :align: center
   :width: 400
   :alt: Ventana del Terminal de Mac.
   
La primera cosa que haremos será comprobar la versión de Python que tenemos por defecto. Para esto en el Terminal teclearemos:

.. code:: bash

    $ python --version

(el símbolo $ ya está ahí, no tienes que teclearlo)

Tras darle a *Enter*, obtendremos la respuesta:

.. code:: bash

    Python 2.7.5

Tal y como pensabamos, tenemos Python 2 por defecto, en concreto la versión 2.7.5


Instalar Python 3.x.x
---------------------

**AVISO IMPORTANTE**: bajo ningún concepto desinstales Python 2.x. A lo mejor tú nunca lo vas a utilizar, pero tu sistema operativo sí lo necesita para funcionar con normalidad. Varias versiones de Python pueden perfectamente coexistir en tu Mac, así que dejaremos Python 2.x en paz y abriremos la `página de descargas de python`_.

.. _`página de descargas de python`: https://www.python.org/downloads/

Ahí, tendremos la posibilidad de elegir entre la última versión de Python 3 o la de Python 2 para Mac OS X (en el momento de escribir este post, son las versiones 3.5.1 y 2.7.11 respectivamente). Por supuesto, elegiremos la primera opción. Una vez terminada la descarga, pincharemos en el archivo *.pkg* descargado y seguiremos los pasos habituales de instalación.

Cuando termine la instalación podemos volver al Terminal para comprobar que todo a ido bien. Volveremos a teclear :bash:`python -- version` y ... veremos otra vez el número de versión correspondiente a Python 2. Lo que ha pasado es que ahora tenemos dos versiones instaladas pero la versión *por defecto* sigue siendo la de Python 2.

Para ver qué versión de Python 3 tenemos, tendremos que teclear :bash:`python3 -- version` y entonces sí aparecerá el número de versión que nos acabamos de instalar:

.. code:: bash
    Tanias-MacBook-Pro:~ tania$ python3 --version
    Python 3.5.1

Pip
++++


Entorno virtual
----------------

Imáginate que estás trabajando sobre tres proyectos escritos en Python. Cada uno de tus proyectos tiene sus propios requirimientos en cuanto a las versiones de las librerías de Python (una librería es una especie de módulo que amplia las funciones iniciales de Python). Tal vez la versión de la librería que tienes instalada te va a funcionar en uno de los proyectos pero no va a funcionar en los otros dos.

La solución a este problema se llama **entorno virtual** (virtual environment). Un entorno virtual es como un espacio cerrado en el que puedes trabajar a tu gusto sin miedo a afectar el mundo exterior. En el caso descrito más arriba crearíamos tres entornos virtuales, uno por proyecto.

Para hacer tus primeros pasos en Python puedes perfectamente prescindir del entorno virtual. Por otro lado, no es mala idea desde principio acostumbrarse a hacer las cosas bien. Por eso, te enseñaremos cómo crear un entorno virtual. Afortunadamente, Python 3 te lo pone muy fácil ya apartir de Python 3.3 ya tienes una herramienta llamada pyvenv preinstalada. De este modo la única cosa que tendrás que hacer es escoger un nombre para tu entorno virtual (supongamos que queremos llamar el entorno "dataenv") y luego teclear lo siguiente en nuestra terminal (todo lo que está antes del $ ya está en el Terminal, no hace falta volver a teclearlo):


.. code:: bash
    Tanias-MacBook-Pro:~ tania$ pyvenv dataenv

Este simple comando creará un entorno virtual llamado dataenv. De hecho, lo podremos comprobar en el Finder, ya que veremos que en el directorio con nuestro nombre de usuario (en mi caso "tania") ha aparecido una nueva carpeta llamada "dataenv". ¡Genial!

Por 

Ahora solo nos hace falta aprender a activar nuestro entorno virtual, o dicho de otra manera, a penetrar en este mundo hermético que nos hemos creado. Nada más fácil:

.. code:: bash
    Tanias-MacBook-Pro:~ tania$ source dataenv/bin/activate
    
Tras darle a Enter, verás que en la parte izquierda de la línea a aparecido el nombre de tu entorno entre paréntesis:

.. code:: bash
    (dataenv) Tanias-MacBook-Pro:~ tania$ 

Ahora todas las librerías que vas a instalar solo afectarán a este entorno y a nada más y por consecuencia los scripts de python que vas a ejecutar estando en este entorno van a utilizar las librerías instaladas en él.

Por último, para abandonar el entorno virtual, simplemente harás

.. code:: bash
    (dataenv) Tanias-MacBook-Pro:~ tania$ deactivate

y verás que las paréntesis con el nombre del entorno han desaparecido. Esto quiere decir que ya has salido del encierro.

Esto es todo para hoy. En el próximo tutorial te enseñaremos cómo ejecutar un script de python.






