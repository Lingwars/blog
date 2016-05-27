Instalar Python 3 en Mac OS X
=============================

:date: 2016-05-27 10:00
:tags: Mac, OS X, Python, instalación
:slug: python-mac
:author: taniaka

¿Tienes un Mac y quieres empezar a utilizar Python? ¡Muy buena decisión! En este post te explicaremos los primeros pasos que tienes que dar para echarlo a andar.

Existen distintas maneras de abordar la instalación de Python en un Mac. Nosotros te explicaremos la más rápida y tal vez más adelante, cuando ya sientas más seguro te podrá interesar explorar las otras opciones (Homebrew, Anaconda etc.) 

Por defecto, tu Mac viene con Python 2 preinstalado. Sin embargo, nosotros vamos a instalar Python 3. ¿Por qué? Aunque muchos proyectos siguen utilizando Python 2, el futuro está en Python 3 y la `wiki oficial de Python`_ nos dice claramente que *Python 2.x está anticuado* (Python 2.x is legacy). Además, Python 3 nos ofrece más facilidades para gestionar cadenas de texto y esto es una gran ventaja para nuestra labor lingüística. Así que, ¡a por Python 3!

.. _`wiki oficial de Python`: https://wiki.python.org/moin/Python2orPython3

El Terminal
---------------
Todas nuestras manipulaciones las haremos desde el Terminal de nuestro Mac. Si nunca has usado el Terminal, no te preocupes, es muy sencillo.

Para abrirlo, simplemente tienes que teclear la palabra *Terminal* en el Finder o en el Spotlight, y darle un click. Se abrirá una ventana de este estilo:

.. figure:: {filename}/images/mac-python3-1.png
   :align: center
   :width: 300
   :alt: ventana del Terminal de Mac.
   
La primera cosa que haremos será comprobar la versión de Python que tenemos por defecto. Para esto en el Terminal teclearemos:

.. code:: bash

    Tanias-MacBook-Pro:~ tania$ python --version

El símbolo $ y todo lo que le precede ya está en el Terminal y por supuesto no tienes que volver a teclearlo. Solo teclearás lo que viene después del $.

Tras darle a Enter, obtendrás la respuesta:

.. code:: bash

    Python 2.7.6

El resultado es bien previsible: tenemos Python 2 instalado en nuestro Mac, concretamente la versión 2.7.6.


Instalar Python 3.x.x
---------------------

**AVISO IMPORTANTE**: bajo ningún concepto desinstales la versión de Python 2 preinstalada en tu Mac. A lo mejor nunca la vas a utilizar, pero tu sistema operativo sí que la necesita para funcionar con normalidad. Varias versiones de Python pueden coexistir perfectamente en el mismo Mac, así que dejaremos Python 2.x en paz y abriremos la `página de descargas de Python`_.

.. _`página de descargas de Python`: https://www.python.org/downloads/

Ahí, tendremos la posibilidad de elegir entre la última versión de Python 3 y la última versión de Python 2 para Mac OS X (en el momento de escribir este post, 3.5.1 y 2.7.11 respectivamente). Por supuesto, elegiremos la primera opción. Una vez terminada la descarga, pincharemos en el archivo *.pkg* descargado y seguiremos los pasos habituales de instalación.

.. role:: bash(code)
   :language: bash
   
Cuando termine la instalación podemos volver al Terminal para comprobar que todo ha ido bien. Volveremos a teclear :bash:`python -- version` y veremos ... que no ha cambiado nada: el Terminal nos sigue diciendo que tenemos Python 2. ¿Qué hemos hecho mal? Nada. Simplemente ya tenemos dos versiones de Python pero dado que Python 2 sigue siendo la versión *por defecto*, al escribir :bash:`python` a secas estamos invocando Python 2. Si queremos invocar Python 3 tendremos que escribir :bash:`python3`:

.. code:: bash

    Tanias-MacBook-Pro:~ tania$ python3 --version
    Python 3.5.1

Ahora vemos que Python 3.5.1 se ha instalado correctamente. ¡Genial!


Entorno virtual
----------------

Imáginate que estás trabajando sobre tres proyectos escritos en Python. Cada uno de tus proyectos tiene sus propios requisitos en cuanto a las versiones de las librerías de Python (se podría decir que una librería es una especie de módulo que amplia las funciones iniciales de Python). Tal vez la versión de la librería que tienes instalada te va a funcionar en uno de los proyectos pero no va a funcionar en los otros dos.

La solución a este problema se llama **entorno virtual** (virtual environment). Un entorno virtual es como un espacio cerrado en el que puedes trabajar a tu gusto sin miedo a afectar al mundo exterior y verte afectado por éste. En el caso descrito más arriba simplemente crearíamos tres entornos virtuales, uno por proyecto.

Para hacer tus primeros pasos en Python puedes perfectamente prescindir del entorno virtual. Por otro lado, no es mala idea desde principio acostumbrarse a hacer las cosas bien. Por eso, te enseñaremos cómo crear un entorno virtual. Afortunadamente, Python 3 te lo pone muy fácil ya que de la versión 3.3 ya viene con una herramienta de gestión de entornos virtuales llamada **pyvenv**.

De este modo, la única cosa que tendrás que hacer es escoger un nombre para tu nuevo entorno virtual (por ejemplo *dataenv*, pero podría ser cualquier otro nombre) y escribir:

.. code:: bash

    Tanias-MacBook-Pro:~ tania$ pyvenv dataenv

Este simple comando creará un entorno virtual llamado dataenv. De hecho, lo podrás comprobar en el Finder, ya que verás que en el directorio con tu nombre de usuario (en mi caso "tania") ha aparecido una nueva carpeta llamada "dataenv". Así de simple.

Para penetrar en este mundo hermético que te has creado, simplemente escribirás:

.. code:: bash

    Tanias-MacBook-Pro:~ tania$ source dataenv/bin/activate
    
Tras darle a Enter, verás que a comienzo de la línea ha aparecido el nombre de tu entorno entre paréntesis:

.. code:: bash

    (dataenv) Tanias-MacBook-Pro:~ tania$ 

Por otro lado, como ves no has tenido que precisar que querías crear el entorno con Python 3.5.1 y no con Python 2. Se ha hecho solo ya que pyvenv, como ya lo hemos dicho, solo existe a partir de la version 3.3. Si quisieras crear un entorno virtual en Python 2 o en una versión de Python 3 anterior a la 3.3, probablemente usarías *virualenv*. No lo vamos a cubrir en este post, pero si te interesa puedes echar un vistazo a `este tutorial`_.

.._'este tutorial`: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Y, ¿qué piensas que va a pasar ahora si tecleas :bash:`python -- version`? Efectivamente, si has creado tu entorno con Python 3.5.1 ya no tienes que escribir :bash:`python3` ya que :bash:`python` a secas ya invocará Python 3.5.1. 

Cuando quieras salir de tu *retiro*, solo tendrás que hacer

.. code:: bash

    (dataenv) Tanias-MacBook-Pro:~ tania$ deactivate

y verás que las paréntesis habrán desaparecido.

Si de momento no le ves mucha utilidad a los entornos virtuales, no te preocupes. Acabarás pillándoles el gusto cuando empieces a escribir tu primeros programas en Python. Y seguramente no tardarás mucho en hacerlo, ¿verdad?

Esto era todo para hoy. En el próximo tutorial hablaremos un poco más del Terminal y te explicaremos cómo ejecutar un script de Python.






