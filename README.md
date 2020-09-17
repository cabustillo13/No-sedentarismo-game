# No-sedentarismo-game

<p align="center">
 <img width="100px" src="https://github.com/cabustillo13/No-sedentarismo-game/blob/master/Readme/videojuegos.svg" align="center" alt="No-sedentarismo-game" />
 <h2 align="center">No-sedentarismo-game</h2>
 <p align="center"><b>Nueva forma de jugar a los videojuegos, para ponerte en movimiento y evitar el sedentarismo.</b></p>

</p>
  <p align="center">
    <a href="https://github.com/cabustillo13/No-sedentarismo-game/actions/new">
      <img alt="Tests Passing" src="https://github.com/anuraghazra/github-readme-stats/workflows/Test/badge.svg" />
    </a>
        <a href="https://github.com/cabustillo13/No-sedentarismo-game/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/cabustillo13/No-sedentarismo-game?color=0088ff" />
    </a>
    <a href="https://github.com/cabustillo13/No-sedentarismo-game/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/cabustillo13/No-sedentarismo-game?color=0088ff" />
    </a>
    <br />
    <p align="center">
    <a href="https://github.com/cabustillo13/No-sedentarismo-game/blob/master/README.md">Español</a>
    ·
  </p>
</p>

## Problemática

Según la Organización Mundial de la Salud, al menos un 60% de la población mundial no realiza la actividad física necesaria para obtener beneficios para la salud. Esto se debe en parte a la insuficiente participación en la actividad física durante el tiempo de ocio y a un aumento de los comportamientos sedentarios durante las actividades laborales y domésticas. 

Por consiguiente, las enfermedades no transmisibles asociadas a la inactividad física son el mayor problema de salud pública en la mayoría de los países del mundo.

La evolución mundial de la actividad física es especialmente preocupante en algunas poblaciones de alto riesgo: jóvenes, mujeres y adultos mayores. Es importante que, a la hora de desarrollar y aplicar la iniciativa "Por tu salud, muévete".

## Solución

Una manera de ponernos en movimiento de forma lúdica,divertida y de bajo costo para niños, niñas,adolescentes e incluso adultos mayores, es integrando actividades físicas mientras se juega videojuegos. 

Mi proyecto consiste en un script ejecutable en Python3 que se puede implementar en simultáneo (en un thread paralelo para ser más específico) a juegos de computadora. Mediante un sistema de captación de video con la cámara web, el script adquiere los movimientos del usuario, los proceso y los traduce en comandos por teclado (previamente configurados). 

Previamente había mencionado que es una herramienta de bajo costo. No hay necesidad de contar con la consola Wii, ni un kinect del Xbox 360 ni otro elemento costoso adicional para jugar con el movimiento del cuerpo. Para nuestro caso, debido a que el script funcionando una cierta gama de colores. Basta con que el usuario consiga alguna cartulina del color correspondiente al color configurado, pintar con colores en una hoja, buscar algún elemento del color propuesto o cambiarle el color que está detectando el script para adaptarlo a los elementos que tenga en su casa. Y con eso es más que suficiente para poder comenzar a jugar sus videojuegos.

## Ejemplos

Actualmente tengo un control para jugar el juego del Dinosaurio de Chrome, donde el usuario se pega un pedazo de cartulina en la camisa, se aleja de la cámara y ejecuta el juego. El usuario al saltar, el script interpreta esa acción con el comando de la barra espaciado, y hará que el dinosaurio salte en el juego. Al agacharse, el script interpreta esa acció con el comando de la key down, y haŕa que el dinosaurio se agache.

También tengo un control para controlar el clásico juego de Snake con la frente. El usuario realiza movimiento hacia la derecha, izquierda, arriba y abajo para mover la serpiente del juego.

## Objetivo de mostrar mi proyecto en el Freedon Software Day

* Poder crear scripts genéricos, que funcionen para sus distintos tipos de videojuegos  y que más personas se pongan en movimiento,se diviertan, mejorar la experiencia del juego y sobre todo mejoren su salud para tener una mejor calidad de vida. 

* También la idea es que sea una herramienta adicional donde tu joystick es tu cuerpo, y se controla por tus movimientos. 

## Casos de uso en otros países

* Un estudiante con problemas de obesidad en Estados Unidos se negaba a realizar el curso de educación física, pero en  la escuela, al ver que gustaba de los videojuegos decidieron alternar la clase por Dance Dance Revolution (juego en el que debes bailar y créanme que se suda) al finalizar el año había bajado casi 20 kilos.

* Imagine tener 80 años, haber sido un excelente jugador de tenis pero por las condiciones físicas debidas a la edad ya no puede practicar… se trata de una frustración que puede convertirse en depresión. Incluso el Dr. Patch Adams menciona que la sonrisa es la mejor medicina. También mi script se puede formar parte de la rehabilitación de muchos asilos.

## Bibliografía

* [Artículo de la OMS sobre sedentarismo](https://www.who.int/dietphysicalactivity/factsheet_inactivity/es/)

* [Casos de uso en otros países](https://gestion.pe/blog/juegomaniaticos/2017/04/los-videojuegos-y-el-sedentarismo.html/?ref=gesr)

* [Gesture Controlled](https://github.com/mohitwildbeast/Gesture-Controlled-Snake-Game)
