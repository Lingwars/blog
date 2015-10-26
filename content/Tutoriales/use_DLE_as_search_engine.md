Title: Cómo añadir el DLE como motor de búsqueda del navegador  
Date: 2015-10-25 10:00  
Tags: tutoriales, recursos, DLE, RAE, diccionarios, navegadores, Google Chrome, Mozilla Firefox
Author: nimbusaeta  

Ahora que la 23ª edición del Diccionario de la RAE está disponible en línea, he tenido que cambiar la configuración de mi navegador para poder buscar directamente en el diccionario desde la barra de búsqueda. Y ya que lo hago para mí enseño cómo hacerlo ;)

La nueva versión es hipertextual (se puede ir a la definición de cualquier palabra pinchando en ella desde otras definiciones), agrupa y muestra variedades ortográficas (si buscas, por ejemplo, _chupachús_, te redirige directamente a _chupachups_, que es la variante que recomienda, sin tener que hacer otro click), y lematiza mejor (antes, al buscar, por ejemplo, _elegantísimamente_, no obtenías ningún resultado; ahora, te sugiere la definición de _elegante_). En [esta sección de la obra en papel](http://www.rae.es/sites/default/files/La_vigesimotercera_edicion.pdf) se explican más novedades de la nueva edición.

Aunque estemos acostumbrados a llamarlo DRAE (Diccionario de la Real Academia Española) ahora se prefiere DLE (Diccionario de la Lengua Española), ya que en él han colaborado todas las academias de la [ASALE](http://www.asale.org/) (Asociación de Academias de la Lengua Española).

# Google Chrome

En primer lugar vamos a `http://dle.rae.es/` (desde donde se nos redirige automáticamente a `http://dle.rae.es/?w=diccionario`, la dirección correspondiente a la palabra _diccionario_). 

En el cuadro de búsqueda, hacemos click con el botón derecho y elegimos de entre las opciones del menú desplegable `Añadir como motor de búsqueda...`.

![Añadir como motor de búsqueda]({filename}/images/lw-030.jpg)

Nos aparecerá un cuadro como el de la siguiente imagen:

![Editar motor de búsqueda]({filename}/images/lw-031.jpg)

El nombre va a servir para encontrarlo después entre los demás motores de búsqueda que tengamos, y aparecerá al buscar en el navegador cuando lo terminemos de configurar. La palabra clave será la cadena de caracteres que tengamos que escribir en la barra de búsqueda del navegador cuando queramos buscar en este motor. Y la URL, aquella a la que el navegador irá cuando usemos la palabra clave.

Mi recomendación es poner en `Nombre:` algo descriptivo, como "DLE" o "Diccionario de la Lengua Española"; y en `Palabra clave:`, algo corto y en minúsculas, como "dle". Lo que aparece en `URL:` no solemos tener que editarlo en otros motores, pero no sé por qué en el caso del DLE no aparece la URL correcta. Hay que sustituir lo que sale por defecto por `http://dle.rae.es/?w=%s`.

![Editar motor de búsqueda]({filename}/images/lw-032.jpg)

Le damos a `Aceptar` ¡y ya está! Cuando escribamos en la barra de direcciones del navegador `dle luquete` aparecerá lo siguiente:

![Búsqueda con palabra clave]({filename}/images/lw-033.jpg)

Solo tenemos que darle a `Intro` y nos llevará a la definición de _luquete_ :D

# Mozilla Firefox

Firefox trata los motores de búsqueda como marcadores. El proceso es parecido pero hay que editar la URL en la configuración de los marcadores.

Lo primero que hay que hacer es ir a `http://dle.rae.es/`  y en el cuadro de búsqueda, hacer click con el botón derecho. Elegimos de entre las opciones del menú desplegable `Añadir una palabra clave para esta búsqueda...`.

![Añadir una palabra clave para esta búsqueda]({filename}/images/lw-034.jpg)

Nos aparecerá un cuadro como el de la siguiente imagen:

![Editar motor de búsqueda]({filename}/images/lw-035.jpg)

Podemos poner el nombre y la palabra clave que queramos. El nombre va a servir para encontrarlo después entre los marcadores, y la palabra clave será la cadena de caracteres que tengamos que escribir en la barra de búsqueda del navegador cuando queramos buscar en este motor.

Mi recomendación es poner en `Nombre:` algo descriptivo, como "DLE" o "Diccionario de la Lengua Española"; y en `Palabra clave:`, algo corto y en minúsculas, como "dle".

![Editar motor de búsqueda]({filename}/images/lw-036.jpg)

Le damos a `Guardar` y ahora tenemos que editar la URL. Para ello podemos presionar Ctrl+Mayús.+B o pinchar en el botón de la imagen siguiente y después en `Mostrar todos los marcadores`.

![Editar motor de búsqueda]({filename}/images/lw-037.jpg)

Nos aparecerá una ventana como la siguiente. En el cuadro de arriba a la derecha podemos buscar con el nombre que le hayamos dado al motor de búsqueda y aparecerá entre todos nuestros marcadores.

![Editar motor de búsqueda]({filename}/images/lw-038.jpg)

Lo único que tenemos que hacer es sustituir, en el campo `Dirección:`, la URL que viene por defecto por `http://dle.rae.es/?w=%s`. Luego podemos salir dándole a la X.

![Editar motor de búsqueda]({filename}/images/lw-039.jpg)

Ahora, con solo escribir en la barra de direcciones del navegador `dle dingolondango` nos llevará a la definición de esa curiosa palabra :D

![Búsqueda con palabra clave]({filename}/images/lw-040.jpg)






En ambos casos lo que hemos hecho es decir al navegador que cuando usemos esa palabra clave nos lleve a una URL que depende de lo que escribamos inmediatamente después, sustituyendo `%s` por lo que sigue a la palabra clave. No es nada ilegal ni raro ni le quitamos tráfico a la RAE ni nada; de hecho, ellos recomiendan algo parecido pero un poco menos cómodo en su [Guía de consulta](http://dle.rae.es/?t=ayuda.html#sec12&o=h): aprenderte de memoria la URL.




