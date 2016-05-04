Conexión al stream de Twitter
=============================

:date: 2016-05-06 15:20
:tags: taller, twitter, python
:slug: twitter-stream
:author: Javier G. Sogo

En esta ocasión vamos a dar una pinceladas sobre cómo podemos conectarnos a la
API de Twitter para volcar en nuestro ordenador los *tweets* que se van publicando
sobre algún tema a medida que van apareciendo en la red. Es decir, nos conectaremos
a la que se conoce como `Streaming API`_.

.. _`Streaming API`: https://dev.twitter.com/streaming/overview

Recibir los *tweets* en tiempo real nos permite hacer cosas tan curiosas como
`emojitracker`_ que muestra en tiempo real los emoticonos que se están utilizando,
o también podríamos hacer seguimiento de algún acontecimiento al mismo tiempo que 
sucede mediante análisis de sentimieno, o... ¿nos comentas que se te ocurre en los
comentarios más abajo?

.. _`emojitracker`: http://emojitracker.com/

.. figure:: {filename}/images/emojitracker.jpg
   :align: center
   :width: 600
   :alt: emojitracker: realtime emoji use on twitter.
   
   emojitracker: monitorización en tiempo real del uso de emoticonos en Twitter.
   

¿Qué necesito?
--------------
Vamos a utilizar Python para este ejemplo (aunque bien podría haberse abordado con
otro lenguaje de programación) e instalaremos también algunos paquetes adicionales
que nos van a simplificar la vida.

Así que, si aún no lo has hecho, debes `instalarte Python <{filename}install_python_win7.md>`_
y después estos paquetes adicionales:

.. code:: bash

    $> pip install tweepy

Con la línea anterior instalamos `tweepy`_, una librería que nos va a simplificar sobremanera
la utilización de la API de Twitter con Python.

.. _`tweepy`: http://www.tweepy.org/


¿Qué es una API?
----------------
API es la abreviatura de *Application Programming Interface*, es decir, la interfaz que nos
permite conectarnos programáticamente a una aplicación, lo que podríamos llamar el contrato
que establece una aplicación con su entorno con una serie de claúsulas del tipo
*"si tú me preguntas de esta manera, yo te respondo de esta otra"*; y gracias a ellas podemos
hacer programas que colaboren unos con otros.

Twitter, como muchas otras aplicaciones online ofrecen una API que nos permite hacer programas
que utilicen sus datos y también aportar datos a través de otras aplicaciones. Prácticamente
cualquier aplicación que tengamos en nuestro teléfono móvil se estará comunicando continuamente
con una servidor en internet para intercambiar datos.

En el caso de las APIs de internet algo imprescindible es la identificación de quién está
haciendo la llamada y qué acciones puede realizar. Como podrás suponer, mi móvil tiene acceso
a mis datos y el tuyo a los tuyos, y todos queremos que esto sea así; esta vinculación se
consigue a través de credenciales, parejas de claves públicas/privadas, autenticación,...  

Ni hoy ni aquí, es el momento ni el lugar para hablar largo de esto, espero que con esta
brevísima introducción te hayas hecho una mínima idea, pero siempre tendrás internet a mano
para consultar más.


1) Obteniendo las claves
------------------------
Lo primero que vamos a tener que hacer es darnos de alta en Twitter e indicar que queremos
crear una aplicación como desarrolladores para que nos generen las claves y *tokens* de acceso
que tendremos que utilizar a continuación. Quizá suena más complicado de lo que es:

  #. Necesitas crearte una cuenta en Twitter.
  #. Después tendrás que crear una nueva aplicación en https://apps.twitter.com/. 
  #. Y en la pestaña `Keys and access tokens` podrás generar un `access_token`. Ahora
     deberías tener acceso a cuatro numerajos como estos:
     
     .. code:: python
     
        consumer_key = 'qjKzLb55Ddq9uTirHRSLh2fn1'
        consumer_secret = 'crUCVcphcM6CM1EhNmQcknLMHV4lIdRIovwF42A8943b7pMghh'
        access_token = '332912007-O2ZZQqICUcRNaImFuuVzyQCstVGo6giphaaJ5Pvu'
        access_token_secret = 'I7hTnSJhefdmRZFaHIxeX5gtQkuurYxUV01jOwDI89yoL'
        
     Ten en mente que cualquiera que acceda a estos datos podrá publicar en Twitter
     usando tu cuenta, y borrar tus tweets... así que trátalos con cuidado y no se
     los dejes a nadie. 

2) El esqueleto del programa
----------------------------
Cuando uno programa hay que ser muy ordenado (y utilizar un control de versiones), así
que vamos a crear el esqueleto de un programa al que después vamos a ir dotando de
funcionalidad.

Crea un directorio en tu ordenador con el nombre que vaya a tener tu programa y dentro
de él vamos a poner dos archivos:

.. code:: bash
        
        secret.py
        run.py

En el primero de ellos, `secret.py`, debes poner tus claves y tokens:

.. code:: python

        consumer_key = 'qjKzLb55Ddq9uTirHRSLh2fn1'
        consumer_secret = 'crUCVcphcM6CM1EhNmQcknLMHV4lIdRIovwF42A8943b7pMghh'
        access_token = '332912007-O2ZZQqICUcRNaImFuuVzyQCstVGo6giphaaJ5Pvu'
        access_token_secret = 'I7hTnSJhefdmRZFaHIxeX5gtQkuurYxUV01jOwDI89yoL'
        
y en el segundo es donde vamos a escribir el código de nuestra aplicación, empecemos
por lo más sencillo, sólo para ver que funciona:

.. code:: python

        import tweepy
        from secret import consumer_key, consumer_secret, access_token, access_token_secret
        
        if __name__ == '__main__':
            print("===== My Application =====")
            # Here starts my program
            
            # End
            print("c'est fini!")
        
Esta separación es muy útil si queremos compartir nuestro programa con otras personas,
así podremos pasarles el archivo con el código, `run.py`, sin necesidad de tener que
borrar las claves que no queremos compartir. **¡Importante!** Si lo estás guardando
con algún sistema de control de versiones acuérdate de indicar que debe ignorar el
archivo `secret.py` para que no lo suba a internet.

Y ahora la prueba de fuego, vamos a ver si nuestro esqueleto de programa funciona:

  #. Abre una consola de comandos (pantalla negra) y ve hasta el directorio donde estén
     los dos archivos anteriores.
  #. Ejecuta `run.py` utilizando Python, es decir, tendrás que escribir:
  
     .. code:: bash
     
        python run.py
        

3) Un programa que funcione
---------------------------
Antes de conectarnos al stream de Twitter vamos a comprobar que todo está en su sitio.
Para ello podemos modificar el archivo `run.py` con el código que aparece a continuación:

.. code:: python

    import tweepy
    from secret import consumer_key, consumer_secret, access_token, access_token_secret


    def get_auth():
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
        

    if __name__ == '__main__':
        print("===== My Application =====")
        
        # Get an API item using tweepy
        auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
        api = tweepy.API(auth)  # Build an API object.
        
        # Test it works
        api.update_status('Hola @lingwars! Estoy mandando este tweet desde mi ordenador')
        
        # End
        print("c'est fini!")
    
¡Pruébalo! ¿Qué ha pasado? ¿Nada? ¿Algo? Este momento es crucial, no sigas adelante si
estás obteniendo algún tipo de error al ejecutar el programa anterior.


4) Conexión al stream
---------------------
Y ya por fin, vamos a por el **tiempo real**. Gracias a la librería `tweepy`_ hacer
esto es tan sencillo como se muestra en el siguiente trozo de código que puedos poner
en tu archivo `run.py`:

.. code:: python

    import tweepy
    from secret import consumer_key, consumer_secret, access_token, access_token_secret


    def get_auth():
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
        

    class MyStreamListener(tweepy.StreamListener):

        def on_status(self, status):
            # When a tweet is published it arrives here.
            print(status.text.encode("ascii", errors='replace'))  # Console output may not be UTF-8
            print("-"*10)
        
        
    if __name__ == '__main__':
        print("===== My Application =====")
        
        # Get an API item using tweepy
        auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
        api = tweepy.API(auth)  # Build an API object.
        
        # Connect to the stream
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        
        print(">> Listening to tweets about #python:")
        myStream.filter(track=['python'])
        
        # End
        print("c'est fini!")
    
Ejecútalo como ya sabes y espera:

.. code:: bash

    python run.py
    
Como podrás imaginar, Twitter no nos está enviando todos los *tweets* que se publican en
el mundo (eso tiene un precio), pero quizá la muestra sea suficientemente significativa
para nuestros propósitos.

¿Y ahora qué?
-------------
Puedes jugar con el programa anterior modificando pequeñas partes a tu antojo. Seguro que
tienes muchas ideas para probar, pero puedes empezar por alguna de éstas:

  * Guardar los tweets en un archivo de texto para consultarlos después
  
    .. code:: python
        
        [...]
        
        def on_status(self, status):
            # Print
            print(status.text.encode("ascii", errors='replace'))  # Console output may not be UTF-8
            print("-"*10)
            # Append to file
            with open("tweets.txt", "a") as myfile:
                myfile.write(status.text)
    
        [...]
        
  * Cotillea qué otra información viene con cada tweet. Para ello puedes cambiar el *listener* por
    algo como lo siguiente:
  
    .. code:: python
    
        import json
        
        [...]
        
        class MyStreamListener(tweepy.StreamListener):

            def on_data(self, data):
                try:
                    decoded = json.loads(data)            
                    print(decoded)
                except:  # Catch it all (very bad practise)
                    pass
                finally:
                    return True  # Keep listening

    Fíjate en que hay información muy interesante como el autor, imágenes, hashtags,... y piensa
    que todo eso podrías guardarlo en una base de datos y hacer búsquedas. \\o/
     
  * Geoposiciona los *tweets*: ¿qué te parece guardar sólo los tweets con información de geolocalización
    y después pintarlos en un mapa? Pues no es complicado, sólo tienes que combinar los dos ejemplos
    anteriores y después utilizar alguna herramienta sencilla para crear mapas como `CartoDB`_
    
.. _`CartoDB`: https://cartodb.com/
        
  * ¿Y si filtramos para que nos muestre únicamente tweets en español escritos desde España?
  
    .. code:: python
        
        # LOCATIONS. Use http://boundingbox.klokantech.com/ for boundingboxes
        SPAIN_GEOBOX = [-9.38,36.05,3.35,43.75]
        myStream.filter(languages=["es"], locations=SPAIN_GEOBOX)
        
    Aunque también podríamos haber detectado el idioma español utilizando una lista de `stopwords`, ¿no?
    
Espero que todo esto haya despertado tu inquietud y te hayas puesto como loco a programar el próximo
digestor de tweets.

        
Antes de acabar
---------------
¿Recuerdas que arriba comentábamos que cualquiera que tuviera tu `consumer_secret`,
`access_token` y `access_token_secret` podría acceder a tu cuenta y publicar en tu
nombre? Quizá ha llegado el momento de borrarlos si no lo vas a utilizar más o de
revocar el acceso a estos tokens (puedes hacerlo en la misma página donde los creaste
utilizando el botón *Regenerate consumer key and secret*. Avisado estás.

     
