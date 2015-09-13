Retos y juegos lingüísticos
===========================

:date: 2015-09-13 10:20
:tags: proyect, python, apicultur
:author: Javier G. Sogo

Acabamos de poner online la primera versión de un conjunto de
desafíos lingüísticos (para nosotros lo serán de programación)
que queremos sacar adelante. `¿Te atreves?`_.

.. _¿Te atreves?: http://games.lingwars.com

La idea de estos juegos/desafíos es que nos sirvan para definir
pequeños proyectos con los que ir aprendiendo a programar y a
utilizar las APIs y recursos que estén a nuestro alcance. Al mismo
tiempo servirán para darnos a conocer y que la gente pueda ver
e interaccionar con algunas de las cosas que hacemos.


Los juegos
----------
He intentado diseñar una arquitectura para la web que permita que
la incorporación de nuevos juegos como si fueran *plug-ins*, es decir,
que haya una parte central fija que gestione las funcionalidades del
sistema y que los juegos se incorporen al sistema mediante clases 
derivadas de una interfaz común GameBase_
que define las funciones que deben implementar.

.. _GameBase: https://github.com/Lingwars/lingwars-games/blob/affc6c02701dc0c6ae9967182ef5354787c053a5/appweb/engine/utils/game.py#L10 

Actualmente hay dos juegos programados de este modo que puedes
utilizar como base para crear los tuyos propios:

* Sum_: suma de enteros. Es un ejemplo de juego con un código muy simple
  que muestra al usuario dos números enteros y le pide que los sume.
  Está aquí con la única intención de mostrar el ejemplo mínimo
  que permite incorporar un juego al sistema.
   
* word2def_: de la palabra a la definición. Este juego muestra al usuario una
  palabra y cuatro posibles definiciones entre las que debe escoger
  la correcta. El código de este juego no se limita a la funcionalidad
  básica como en el caso anterior, sino que es una `aplicación de Django`_
  que además tiene sus propias tablas en la base de datos donde 
  almacena los resultados.
  
Estoy seguro de que en breve habrá alguno más.

.. _Sum: https://github.com/Lingwars/lingwars-games/tree/affc6c02701dc0c6ae9967182ef5354787c053a5/games/sum
.. _word2def: https://github.com/Lingwars/lingwars-games/tree/affc6c02701dc0c6ae9967182ef5354787c053a5/games/word2def
.. _aplicación de Django: https://docs.djangoproject.com/en/1.8/ref/applications/


Cómo añadir nuevos juegos
-------------------------
Si tienes alguna idea de juego o desafío que quieres que pongamos en
el sistema puedes programarlo tú mismo y pedir un pull-request en 
Github para que lo incorporemos. Te voy a explicar cómo hacerlo:

1. Lo primero que tienes que hacer es preparar el sistema para que
   puedas probar todo en local antes de subirlo a la web. Es muy sencillo:
    
    * Haz un **fork** del repositorio `Lingwars/lingwars-games`_  
  
    * Clónate ese repositorio en tu ordenador.  
    * Crea un archivo :code:`secret.py` junto a :code:`~/appweb/appweb/settings.py` con tus
      claves de Apicultur.
     
        .. code-block:: python
            
            ACCESS_TOKEN_STORE = "tu access_token"
            ACCESS_TOKEN_IO = "tu access_token"
    
    * Creamos la base de datos de pruebas (será una base de datos local sqlite3):
     
        .. code-block:: bash
        
            ~/appweb$ python manage.py migrate
        
    
    * Y vamos a arrancar el servidor web en local:

        .. code-block:: bash
        
            ~/appweb$ python manage.py runserver
        
  
    * LLegado aquí deberías ser capaz de acceder a la página en tu navegador
      introduciendo la dirección :code:`http://localhost:8000/`
      
.. _Lingwars/lingwars-games: https://github.com/Lingwars/lingwars-games

2. Después tendrás que programar el juego. Te recomiendo que empieces por
   un juego sencillo (o no), pero que no necesite utilizar una base de datos
   y que sea también **de seleccionar una opción entre varias** (si tienes
   interés en crear otro tipo de juego donde la mecánica sea diferente, 
   coméntamelo antes para preparar la infraestructura).
   
   Todo juego debe cumplir dos requisitos:
   
    * Debe implementarse en una clase que derive de GameBase
    * Tiene que existir un objeto :code:`game` de dicho juego en la raíz
      del paquete de Python.
      
   La primera condición significa que tienes que crear una clase, con
   el nombre que quieras, e implementar los métodos :code:`make_question`
   y :code:`score`, tal y como he hecho aquí con SumGame_ o como 
   aparece a continuación:
   
    .. code-block:: python
       
        class MyAwesomeGame(GameBase):
            title = 'My Awesome Game'
            author = 'Me myself'
            description = "In this game you blablabla"

            def make_question(self, *args, **kwargs):
                question = {
                    'query': "Question to the user", 
                    'options': ["list", "of", "answers",]
                    }
                response = {
                    'answer': <index of correct answer>,  # Esto debe ser el índice de la respuesta correcta en la lista.
                    'info': "Some info to the user"
                    }
                return question, response

            def score(self, response, user_answer):
                # Check the `user_answer`, it should be equal to response['answer']
                # :param:`response` contains the same data created in `make_question`
                u = user_answer.get('answer', None)
                try:
                    u = int(u)
                except TypeError:
                    return 0
                else:
                    return 1 if u == response.get('answer') else 0

   La segunda condición hace referencia a que debe existir una instancia del juego
   en el archivo :code:`__init__.py` del paquete. Como ocurre 
   `aquí <https://github.com/Lingwars/lingwars-games/blob/0b2efb99e0c811a7ab30c5b2486b0e9bbaaa7a21/games/sum/__init__.py#L42>`__.
   
.. _SumGame: https://github.com/Lingwars/lingwars-games/blob/master/games/sum/__init__.py

Si estos archivos los pones en un nuevo paquete dentro del directorio :code:`~/games/`
el sistema debería ser capaz de detectarlos automáticamente y presentarlos en el listado
de juegos para que lo pruebes.

Si has llegado hasta aquí, ¡enhorabuena! Manda tu pull-request y estaremos encantados
de incorporarlo a la web para que la gente se enfrete a tu nuevo desafío.

----

En próximos capítulos veremos cómo:

* Crear un juego que no sea de opción múltiple
* Crear juegos que hagan uso de la base de datos (serán aplicaciones de Django)