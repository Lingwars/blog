Title: Crónica del EOL2
Date: 2015-11-20 10:20
Tags: eol, chronicle
Author: Javier G. Sogo

El pasado 14 de noviembre celebramos el II Encuentro Oficial Lingẅars centrado en la lingüística de *corpus* (ya habíamos realizado uno,
pero de ese no escribimos crónica :/). Es el primer encuentro en el que nos centramos en un área concreta y creo que es una
coincidencia que debemos adoptar como constumbre, ya que permite seguir un hilo conductor durante toda la jornada y relacionar
unas charlas con otras.

**Spoiler alert.-** Algunos dicen que el próximo encuentro podría ir sobre algo llamado semántica estructural. ¡Apúntate utilizando
el sobrecito que hay arriba y serás pertinentemente avisado!


# Por la mañana

Comenzamos el día con una introducción al grupo a cargo de [Eduardo](https://twitter.com/ebaste) así los que vienen de nuevas
pueden saber a qué nos dedicamos, quiénes somos y qué objetivos tenemos... y de paso vamos autodefiniéndonos, que no es tarea fácil.

## Introducción a la lingüística de corpus

A continuación entramos en harina, directos hacia el corpus de la mano de **Tania** y con la ayuda de **[Leticia](https://twitter.com/nimbusaeta)**;
entre las dos aprendimos lo que es un corpus y cómo manejarlo. En primer lugar nos introdujeros varios conceptos sobre los *corpora*:

* Qué son.
* Por qué usarlos.
* Criterios para construir un corpus.
* Corpus anotados.
* Tipos de corpus.

Una introducción imprescindible para la gente que se acerca por vez primera a este campo, podéis descargar la presentación
[aquí]({filename}/pdfs/eol-2-intro_to_corpus.pdf).

![Introducción a la lingüística de corpus]({filename}/images/lw-043.jpg)

## AntConc

Después **Tania** nos mostró como utilizar [AntConc](http://www.laurenceanthony.net/software.html), una herramienta para
trabajar con corpus desarrollada por Laurence Anthony. Tania nos guió por la herramienta en un recorrido desde las cosas
más simples como contar palabras hasta estudios de concordancia que permiten identificar el sustrato cultural al que 
pertenece un conjunto de documentos.
Si quieres hacer pruebas tú mismo puedes instalarte el programa y descargarte el corpus con el que anduvimos cacharreando:
una selección de artículos de El País recogidos por Tania utilizando [import.io](https://import.io/), ¡algún día nos contará 
cómo lo hizo! [Corpus El Pais 2015-7 (7,8 Mb)]({filename}/pdfs/eol-2-corpus-Pais_2015_7.zip).


# Por la tarde

## Proyectos
Dividimos la tarde en dos secciones, en primer lugar contamos algunos proyectos que están en marcha o en los que participamos:

* [Neutrón (Javi)]({filename}/pdfs/eol-2-neutron.pdf): una herramienta para ayudar en la neutralización de textos y la
traducción translectal. Está en fase de gestación, pero apunta maneras ;D
* [Aracne (Leticia y Elena)]({filename}/pdfs/eol-2-aracne.pdf): un proyecto de [Fundéu BBVA](http://www.fundeu.es/) para analizar la
evolución del lenguaje periodístico durante el último siglo. En breve tendremos noticias de las conclusiones a las que vayan
llegando a través de los medios, seguro.
* [El Enclitizador (Tania y Leticia)]({filename}/pdfs/eol-2-encliticos.pdf): herramienta que analiza una forma verbal con
enclíticos y ofrece información detallada sobre su corrección y la función de cada uno de ellos. Por cierto, buscan a alguien
con conocimientos de programación que quiera hacer una interfaz: una web, un bot de Telegram,... ¿te animas?

![Variedades principales de español]({filename}/images/lw-044.png)

## Recuperación de información
Después la cosa tornó diferente, empezamos a ver ecuaciones proyectadas. **[Javi](https://twitter.com/jgsogo)**
nos introdujo lo que era la **recuperación de información** y la importancia de poder medir la distancia entre
dos documentos cualesquiera, un problema muy común que se encuentra en la raíz de los sistemas de búsqueda
en internet y de los motores de recomendación o el *topic modelling*. Los dos objetivos principales de la
presentación eran concienciarnos del problema y exponer una métrica muy sencilla (pero potente) para realizar
estos cálculos: [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf). También puedes ver
la [presentación]({filename}/pdfs/eol-2-information_retrieval.pdf).

La jornada terminó con un pequeño trozo de código en el que se implementaba un motor de búsqueda muy básico, pero
que nos permitía realizar *queries* y obtener el documento que estábamos buscando 
([ver código](https://gist.github.com/jgsogo/61975297ff6ca3f01a71)).


# ¡Te esperamos en la próxima!


