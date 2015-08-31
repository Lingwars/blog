Title: Crear contenidos en el blog
Date: 2015-07-30 10:20
Tags: blog
Author: Javier G. Sogo

Voy a explicar cómo añadir contenidos a este blog, así ya nadie tendrá excusas. El blog está construido utilizando [Pelican](http://docs.getpelican.com/en/3.6.0/) y alojado en [Github](https://github.com/Lingwars/blog), porque somos así de _techies_; de esta forma **cualquiera que quiera contribuir puede enviar sus artículos** a través de un pull-request y, después de pasar por nuestro exigente sistema de revisión y corrección, serán incorporados a la versión online.

Si ya estás familiarizado con el funcionamiento de Github entonces este tutorial no va a dirigido a ti, aquí vamos a explicar este proceso sin necesidad de que salgas de tu navegador y sin que tengas que utilizar Git en ningún momento.

Primero te indicamos cómo añadir un nuevo artículo y, después, está la explicación sobre cómo corregir un artículo existente.


# Añadir un nuevo artículo
Para añadir un artículo nuevo debes seguir los siguientes pasos:

 1. **Crear un usuario en Github:** el usuario no es necesario para ver y navegar por la web, pero lo necesitarás para poder realizar las modificaciones.
 
 1. **Hacerte una copia del repositorio:** para ello tienes que acceder a la web donde se encuentra este blog [https://github.com/Lingwars/blog](https://github.com/Lingwars/blog) y hacer clic en el botón `Fork` que aparece en la zona superior derecha:
    
    ![Fork a repository]({filename}/images/lw-1.png)
    
    el sistema creará una copia del repositorio y lo añadirá a los repositorios de tu usuario. Ahora deberías haber sido transportado a esta copia, en la parte superior aparecerá un texto indicando en qué repositorio estás y de dónde has hecho el _fork_.
    
 1. **Crear un nuevo archivo para escribir:** cada publicación del blog está en un archivo diferente, así que para crear un nuevo artículo tendrás que ir al directorio `content`. Ahí encontrarás archivos y directorios; los directorios son las categorías del blog, así que elige aquella en la que mejor encaje lo que vas a escribir:
    
    ![Create new file]({filename}/images/lw-3.png)
    
    ponle un buen nombre al archivo (siempre es mejor si no tiene espacios en blanco ni caracteres especiales como acentos, eñes... y mejor en minúsculas). Recuerda que el archivo debe tener la extensión `.md`. Pues ya sólo te queda ponerte a escribir:
    
    ![Write]({filename}/images/lw-4.png)
   
 1. **Formato del texto:** el contenido hay que escribirlo utilizando Markdown, para ello puedes ayudarte de algún editor online como [este](http://dillinger.io/) o [este](https://stackedit.io/editor); aunque una vez que le cojas el truco, verás que es muy fácil.
    
 1. **Guardar:** ten en cuenta que puedes guardar el archivo cuando quieras y seguir después. Si vas a la parte de abajo puedes ver el siguiente botón, pon unos buenos comentarios y pulsa en él:
    
    ![Save]({filename}/images/lw-7.png)
    
    El archivo está guardado y a partir de ahora podremos ayudarte a escribirlo.
    
 1. **Continuar escribiendo:** para añadir contenidos a un archivo existente tendrás que encontrarlo y navegar hasta él, una vez que lo tengas debes hacer clic en el lápiz, que indica _editar_:
      
    ![Edit]({filename}/images/lw-8.png)
    
    añade lo que consideres oportuno y repite el ciclo "Guardar", "Continuar escribiendo" tantas veces como necesites.
    
    Una vez que estés satisfecho con el contenido del artículo, que consideres que lo has terminado, debes hacer un pull-request para pedirnos que lo incorporemos al blog.

 1. **Pedir un pull-request:** para pedir un pull-request sólo tienes que darle al texto que está a la derecha y que dice _Pull request_:
    
    ![Pull request]({filename}/images/lw-9.png)

    El sistema te muestra todos los cambios que has realizado y te pide que confirmes tu intención:
    
    ![Confirm pull request]({filename}/images/lw-10.png)
    
    Una vez más te exigirá un mensaje y una descripción antes de poder darle finalmente al botón verde `Create pull request`.
    
¡Y ya está! Ahora puedes ver la lista de artículos pendientes de incorporación en esta
URL ([https://github.com/Lingwars/blog/pulls](https://github.com/Lingwars/blog/pulls)) y meternos prisa si se nos acumulan.


# Corregir un artículo existente
Si lo que quieres es corregir un artículo o añadir más contenido a uno existente entonces tendrás que encontrarlo en el repositorio ([https://github.com/Lingwars/blog](https://github.com/Lingwars/blog)), navegar hasta él dentro del directorio `content` y abrirlo haciendo clic. A continuación:

 1. **Abrir para editar:** en la parte de la derecha tienes el icono del lápiz que indica _editar_, al hacer clic en él se mostrará el contenido del archivo en texto plano.
    
    ![Edit]({filename}/images/lw-8.png)
    
 1. **Editar el contenido**: edita el contenido que consideres oportuno y, cuando hayas terminado, en la parte inferior de la página puedes proponer el cambio _Propose file change_:
    
    ![Propose changes]({filename}/images/lw-11.png)
    
    El sistema te muestra todos los cambios que has realizado y te pide que confirmes tu intención:
    
    ![Confirm pull request]({filename}/images/lw-10.png)
    
    Una vez más te exigirá un mensaje y una descripción antes de poder darle finalmente al botón verde `Create pull request`.
    
¡Y ya está! Ahora puedes ver la lista de artículos pendientes de incorporación en esta
URL ([https://github.com/Lingwars/blog/pulls](https://github.com/Lingwars/blog/pulls)) y meternos prisa si se nos acumulan.

Muchas gracias por colaborar.


PD.- Si no te aclaras con todo esto también puedes mandarnos el archivo escrito con tu editor de texto preferido y ya nos encargamos nosotros de incorporarlo al blog.
