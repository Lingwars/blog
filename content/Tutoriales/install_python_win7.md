Title: Instalar Python en Windows 7
Date: 2015-08-29 21:20
Tags: Windows 7,Python,instalación,path,pip
Author: nimbusaeta

Tengo un Windows 7 y después de haber aprendido a instalar Python en este sistema y de haberlo explicado a mucha gente que ha venido a las sesiones de Lingwars, voy a dejarlo por escrito también en este tutorial para que pueda hacerlo todo aquel que quiera participar online. La instalación del programa en realidad es muy sencilla, pero luego hay que toquetear un poquito la configuración del sistema, así que está bien que alguien nos lo explique.

En Windows 8 y en Windows 10 es muy parecido.

# Instalar Python

Vamos a la [página de descargas de la web oficial de Python](https://www.python.org/downloads/) y por defecto nos salen los enlaces para Windows. Descargaremos la versión 2.7.10.

Ejecutamos el archivo .msi que nos hemos bajado y seguimos los pasos del asistente para instalar el programa. Para la segunda parte de la instalación **es importante acordarse de la carpeta en que hemos guardado los archivos de Python**.

# Configurar path

Path es una variable del sistema que tenemos que configurar un poquito para poder ejecutar Python con comodidad. Vamos a explicar paso a paso cómo hacerlo en Windows 7.

 1. Ve a _Equipo_ y, debajo de la barra de menús, haz click en _Propiedades de sistema_.

    ![Propiedades de sistema]({filename}/images/lw-020.jpg)

 1. Ahora ve a _Configuración avanzada del sistema_, a la izquierda.

    ![Configuración avanzada del sistema]({filename}/images/lw-021.jpg)

 1. Te saldrá una ventana como la de la siguiente imagen. Ve al botón `Variables de entorno...` y haz click sobre él.

    ![Variables de entorno]({filename}/images/lw-022.jpg)

 1. En la siguiente ventana que te aparece, busca en la parte de abajo _Path_. Selecciona la línea y luego haz click en `Editar...` (o haz doble click en la fila de _Path_).

    ![Path]({filename}/images/lw-023.jpg)

 1. En la siguiente ventana, lo que tenemos que hacer es escribir un par de cosas en el cuadro de abajo, el que dice _Valor de la variable_. En este cuadro aparecen las rutas de todos los programas que tenemos instalados. Por eso, no tiene por qué aparecer lo mismo en la imagen de abajo que en tu ordenador. Eso solo significa que probablemente el último programa que yo instalé fue Calibre ;)

    ![Path_editar]({filename}/images/lw-024.jpg)

 1. Tienes que ir al final del texto de ese cuadro y pegar ";" seguido de **la ruta de la carpeta en que hayas instalado Python**. Esto es importante: puede que también sea "D:\Programas\Python\", pero no tiene por qué.

    ![Path_editar]({filename}/images/lw-025.jpg)

 1. Tienes que averiguar dónde instalaste Python. Para ello, cuando estés en la carpeta correcta, puedes copiar la ruta con el siguiente truco: haz click en la barra superior (donde puedes navegar hacia carpetas anteriores) sobre la parte vacía. Así seleccionarás la ruta de esa carpeta. Fíjate en las imágenes:

    ![Carpeta-Python]({filename}/images/lw-027.jpg)

    ![Carpeta-Python]({filename}/images/lw-028.jpg)

 1. Ahora solo tienes que copiar y pegar ese texto al final del cuadro _Valor de la variable_, que vimos antes (recuerda, seguido de un punto y coma -;-).

 1. Y el último paso es que vuelvas a pegar, detrás de otro punto y coma, esa misma ruta que tienes copiada en el portapapeles más el texto "\Scripts", como se ve en la imagen.

    ![Scripts]({filename}/images/lw-026.jpg)

# Instalar pip

Pip es un gestor de paquetes de Python, y vamos a instalarlo porque va a ahorrarnos muchos pasos a la hora de programar en Python, es más cómodo.

 1. Primero hay que descargar el fichero [get-pip.py](https://bootstrap.pypa.io/get-pip.py) (click derecho en el link y "Guardar como").
 
 1. Y luego ejecutar en la consola (¡recuerda que tendrás que ir hasta el directorio en el que guardaste ese archivo!): `python get-pip.py`. Puedes abrir la consola yendo a `Inicio`, y en el cuadro de texto que dice `Buscar programas y archivos...` escribe "cmd" y dale a intro. Te saldrá la consola, donde ya puedes escribir.

Esto es todo. Si has llegado hasta aquí, ¡felicidades! Ya puedes programar en Python en tu ordenador. Y si te has atascado en algún paso o tienes cualquier otra duda, no dudes en contactar con nosotros.

