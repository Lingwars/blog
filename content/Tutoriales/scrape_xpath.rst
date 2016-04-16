Scrapeando la web con Python
============================

:date: 2016-04-13 19:54
:tags: scraping, xpath, regex
:slug: scrape-xpath


Existen varias herramientas muy buenas que permiten *scrapear* la web sin tener
conocimientos de programación y sin meterse en cosas raras como XPath o expresiones
regulares, sin embargo, antes o después ambas se hacen necesarias si queremos que
la extracción de información sea precisa y eficiente. De hecho las dos herramientas
que he probado, `Import.io`_ y `Portia` (Scrapinghub) ofrecen la posibilidad
de incorporar ambas tecnologías a los scrapers que se crean con sus interfaces
gráficas.

.. _`Import.io`: https://www.import.io/
.. _`Portia`: http://scrapinghub.com/portia/

Y yo me digo, si ya utilizamos XPath y regex, ¿por qué no abordarlo directamente con
programación 100%. El objetivo de esta publicación es mostrar un pequeño ejemplo con
el que vamos a ser capaces de automatizar el proceso de descarga de los artículos de
una web.


¿Qué necesito?
--------------
Vamos a utilizar Python para este ejemplo (aunque bien podría haberse abordado con
cualquier lenguaje de programación) e instalaremos también algunos paquetes adicionales
que nos van a simplificar la vida, a pesar de que bien podríamos hacerlo con las librerías
instaladas por defecto con nuestro Python.

Así que, si aún no lo has hecho, debes `instalarte Python <{filename}install_python_win7.md>`_
y después estos paquetes adicionales:

.. code:: bash

    $> pip install requests
    $> pip install lxml

Una brevísima descripción:

 * `requests`_: una librería estupenda para trabajar con HTTP, una de las imprescindibles en tu mochila ;D
 * `lxml`_: es una librería para manejar XML, básica, pero suficientemente potente para lo que haremos.

.. _`requests`: http://docs.python-requests.org/en/master/
.. _`lxml`: http://lxml.de/

Y ahora que ya tienes todo listo, let's go!


HTML/XHTML
----------
El HTML es el *HyperText Markup Language*, es el código con el que se escriben las páginas web.
Este código es interpretado por el navegador y junto con las hojas de estilo (CSS) y el 
javascript nos permite obtener unas páginas web interactivas y agradables como las que tenemos
hoy en día.

Actualmente el estándar es **HTML5/XHTML5** que añade algunas etiquetas nuevas de caracter
semántico y asociadas a funcionalidades, pero no necesitamos entrar en esto, lo que vamos
a hacer es mucho más sencillo.

Un ejemplo de HTML podría ser el siguiente:

.. code:: html 

    <html>
        <head>
            <!-- Comentario: Este título se mostrará en la barra superior del navegador -->
            <title>Wikipedia | HTML</title>
        </head>
        <body>
            <!-- Todo lo incluido dentro de la etiqueta 'body' es lo vemos en el navegador -->
            <div id="content">
                <h1>Ejemplo de HTML</h1>
                <div class="section">
                    <h2>Primera sección</h2>
                    <p>Y esto es un párrafo con algo en <strong>negrita</strong> y poco más.</p>
                </div>
                <div>
                    <h2>Segunda sección</h2>
                    <p>En este otro párrafo pongo un <a href="https://lingwars.github.io/blog">link a Lingwars</a>.</p>
                </div>
            </div>
        </body>
    </html>


En el extracto de código anterior se puede ver la estructura básica de una página web; en
ella se aprecia la disposición jerárquica de los elementos y las secciones principales.
Sin embargo, el código de una web de verdad es mucho más largo y farragoso, lo puedes comprobar
tú mismo abriendo una web cualquiera en tu navegador y utilizando la opción `ver código fuente`
que se te mostrará al hacer *click* con el botón derecho en cualquier lugar de la página.

.. figure:: {filename}/images/scrape-xpath-1.png
   :align: center
   :width: 600
   :alt: Código fuente de un artículo de la web de Lingwars.
   
   Código fuente de un artículo de la web de Lingwars.

Puedes leer (recomendado) los artículos de la Wikipedia referentes a HTML_ y HTML5_,
nosotros ahora vamos a seguir avanzando.

.. _HTML: https://es.wikipedia.org/wiki/HTML#C.C3.B3digos_HTML_b.C3.A1sicos
.. _HTML5: https://es.wikipedia.org/wiki/HTML5


Descargar la web
----------------
El paquete `requests`_ al que hicimos referencia anteriormente es especialmente bueno en esto.
Con el siguiente script podemos descargarnos el código HTML de cualquier web:

.. code:: python

    import requests
    import sys

    def download(url):
        """Returns the HTML source code from the given URL
            :param url: URL to get the source from.
        """
        r = requests.get(url)
        if r.status_code != 200:
            sys.stderr.write("! Error {} retrieving url {}".format(r.status_code, url))
            return None
        
        return r.text

    
    if __name__ == '__main__':
        url = "http://elpais.coms"
        r = download(url)
        if r:
            sys.stdout.write(r[:200])
        else:
            sys.stdout.write("Nothing was retrieved.")
            
        
La función `download` anterior devuelve el contenido HTML de la `url` que le pasamos como parámetro,
deberías probar a ejecutar el código anterior con diferentes URLs y puedes comprobar que el texto
devuelto es el mismo que ves en el navegador al utilizar el botón `ver código fuente`.


XPath - Acceso a los datos
--------------------------
El XPath (XML Path Language) es un lenguaje que permite extraer contenido de un documento XML
de una forma parecida a cómo lo hacen las expresiones regulares sobre el texto. Ambos son
bastante complejos y la forma más fácil de aprender es a base de prueba y error, y luego ya
con la práctica cada vez habrá más aciertos.

Pruebas online
++++++++++++++ 
Vamos a hacer algunas pruebas sobre el XHTML que mostramos más arriba. A mí me gusta utilizar
esta aplicación online (`XPath Tester`_) para probarlo de forma interactiva, pero puedes utilizar cualquier otra
que te guste o encuentres por internet.

.. _`XPath Tester`: http://codebeautify.org/Xpath-Tester

Probaremos algunas cadenas XPath típicas para ver qué nos devuelven:

 * `//a/@href`: devuelve el atributo `href` de los nodos cuya etiqueta sea `a` y que se encuentren en cualquier
   punto del árbol jerárquico (`//`).
 * `//title/text()`: devuelve el texto (el contenido que hay entre las etiquetas) de los nodos cuya etiqueta sea
   `title` y que se encuentren en cualquier punto del árbol.
 * `//div[@id='content']//p/text()`: devuelve el texto de todos los nodos tipo `p` que estén por debajo del
   nodo `div` cuyo atributo `id` es `content`, en cualquier lugar en que se encuentre este nodo.
 * `//div[@id='content']//p//text()`: prácticamente igual que la anterior, pero con una sutil diferencia. Esta
   cadena XPath devuelve el texto de todos los nodos hijo de todos los nodos tipo `p` (también el texto del propio
   nodo `p`).

Implementación en Python
++++++++++++++++++++++++
Por supuesto, estas pruebas las podemos hacer también con Python. Fíjate en el siguiente programa:

.. code:: python

    import requests
    import sys
    from lxml import html


    def download(url):
        """Returns the HTML source code from the given URL
            :param url: URL to get the source from.
        """
        r = requests.get(url)
        if r.status_code != 200:
            sys.stderr.write("! Error {} retrieving url {}\n".format(r.status_code, url))
            return None
        
        return r


    if __name__ == '__main__':
        sys.stdout.write("=============================\n")
        sys.stdout.write("== Lingwars - Scrape XPath ==\n")
        sys.stdout.write("=============================\n")
        
        url = "http://www.elmundo.es/internacional.html"
        
        page = download(url)
        if page:
            sys.stdout.write("\n\n1) Download text from {}\n".format(url))
            sys.stdout.write(page.text[:200])
            
            # Parse the text to XML structures
            sys.stdout.write("\n\n2) Let's try some XPath expresions:")
            tree = html.fromstring(page.content)
            
            # Execute xpath over retrieved html content
            xpath_string = '//a/@href'
            results = tree.xpath(xpath_string)
            sys.stdout.write('\n\t'.join(results))
            
        else:
            sys.stdout.write("Nothing was retrieved.")


Lo que estamos haciendo es descargarnos la web `http://www.elmundo.es/internacional.html`,
parsear el XML y utilizar la cadena XPath `//a/@href` para recuperar todos las direcciones
de los enlaces que hay en la página.

Ejemplo con un artículo
+++++++++++++++++++++++
Muchas veces querremos obtener los datos de una publicación, sigamos con el periódico El Mundo
y pensemos en que queremos obtener el autor, la fecha, el contenido y toda la información que
podamos de un artículo en su web.

Utilicemos como ejemplo el que aparece en este link: `http://www.elmundo.es/internacional/2016/04/14/570f7ad946163f045f8b45e4.html`

.. figure:: {filename}/images/scrape-xpath-2.png
   :align: center
   :width: 600
   :alt: Captura de un artículo del periódico El Mundo.
   
   Captura de un artículo del periódico El Mundo.

Podemos modificar el programa anterior para que acceda a la URL del artículo y con las
siguientes cadenas XPath obtener los datos que buscábamos (algunos datos pueden estar
presentes en varios nodos, podemos elegir cuál es el más sencillo de obtener):

 * título: `//article/h1[@itemprop='headline']/text()`
 * entradilla: `//article/div[@itemprop='articleBody']/p[@class='summary-lead']//text()`
 * autor: `//footer/ul/li[@itemprop='name']//text()`
 * localización: `//footer/ul/li[@itemprop='address']//text()`
 * datetime: `//article/div[@itemprop='articleBody']/time//text()`
 * contenido: `//article/div[@itemprop='articleBody']/p[not(@class='summary-lead')]//text()`
 
No continúes sin probar lo anterior. Asegúrate de que entiendes el por qué de cada elemento
de las cadenas anteriores y si no, aquí estamos para ayudarte.

   
Automatizar el proceso
----------------------
Si te has dado cuenta, los dos ejemplos que hemos mostrado permiten extraer todas las URLs
de una página y el contenido (título, autor, fecha,...) de la misma, en caso de que existan,
claro. ¿Qué te parecería juntar ambos en uno? ¿Qué tal si hacemos un crawler que se
descargue todos los artículos de El Mundo? ¿O que se descargue sólo los de una sección?

Podemos utilizar la siguiente estrategia:

 #. Seleccionar un conjunto de páginas de inicio (o una sola).
 
    .. code:: python

        url = "http://www.elmundo.es/internacional.html"

 #. Establecer los patrones de las URLs que debe visitar nuestro crawler para seguir buscando.
 
    .. code:: python
    
        visit_pattern = [re.compile('https?:\/\/(www.)?elmundo.es\/internacional.*'),]
        
 #. Fijar los patrones de las páginas en las que debe buscar el contenido.
 
    .. code:: python
    
        content_pattern = [re.compile('https?:\/\/(www.)?elmundo.es\/internacional\/(?P<year>\d{4})\/(?P<month>\d{2})\/(?P<day>\d{2})\/(?P<uuid>[\d\w]+).html'),]
 
 #. Y ahora construir un bucle recursivo en los siguientes pasos:
 
    #. Buscar todas las URLs de en las páginas de inicio (¡elimina los duplicados!)    
    #. Para cada una de estas URLs:
    
        #. Si satisface algún `visit_pattern`, extraer las URLs que encuentre y añadirlas a la lista de URLs por visitar.
        #. Si satisface algún `content_pattern`, scrapear su contenido y guardarlo.
        
¿Te animas a implementarlo? No mires `aquí <https://github.com/Lingwars/lingwars/blob/master/lingwars/scrape/example.py>`_
hasta que no te hayas peleado un poco tratando de hacer el programita.