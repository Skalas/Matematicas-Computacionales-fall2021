# Matemáticas Computacionales

## Antes de empezar ...

1. Instalar `git`
   1. Si estás en una distro de  `GNU/Linux` tipo `Debian`: `sudo apt-get install git`.
   2. Si estás en una MacOS sigue las instrucciones de [aquí](http://git-scm.com/download/mac) y sigue las instrucciones.
1. Crea una cuenta en github
2. Crear una [llave `ssh`](https://help.github.com/articles/generating-ssh-keys) y conectarla a **Github**.
2. *Forkear* este repositorio
3. Instalar [`docker`](https://docs.docker.com/installation/#installation)
4. Instalar **un editor de textos**
   1. `GNU/Emacs`
   2. `Sublime`
   3. `VsCode`
   4. `Atom`


## El curso


### Objetivos

* El alumno **interactuará** con la línea de comandos.
* El alumno **mantendrá** un repositorio de código versionado de sus archivos y programas.
* El alumno **creará** gráficas y ecuaciones de calidad para presentaciones y publicaciones.
* El alumno **visualizará** expresiones análiticas y **observará** su comportamiento al variar parámetros.
* El alumno **leerá** y **escribirá** a archivos locales.
* El alumno **creará** interfaces con periféricos.
* El alumno **analizará** datos ajustando curvas y optimización.
* El alumno **comprenderá** los algoritmos numéricos y su estabilidad, precisión y complejidad.
* El alumno **seleccionará** el algoritmo apropiado para cada problema.
* El alumno **implementará** el algoritmo seleccionado.
* El alumno **probará** y *debugeará* la implementación.

### ¿Cómo comunicarnos?

#### Por correo

Escribe a `miguel.escalante@itam.mx` y que el *subject* empiece con `[Mate Computacional 2021]`.

### ¿Cómo será el curso?

- Pasaremos el tiempo de la clase aprendiendo a codificar para resolver problemas de ingeniería o ciencia.
- Algunas actividades requerirán que se haga [*programación por pares*](http://es.wikipedia.org/wiki/Programaci%C3%B3n_en_pareja).
- Las tareas estarán basadas en las habilidades que desarrolles en clase ¡Trata de no faltar!
- Practicar es la única manera de volverse bueno en esto. Lo más probable es que pases de 8 a 12 horas por semana (además del tiempo de la clase) escribiendo y *debugeando* código.
- Si tienes problemas con la tarea, pregúntame, o busca ayuda de tus compañeros. **NO** esperes a que sea demasiado tarde para tomar tu destino en tus manos.


### Evaluación

La calificación final está compuesta de la manera siguiente:

| Categoría                     | Porcentaje |
|-------------------------------|------------|
| Ejercicios del Proyecto Euler | 10%        |
| Tareas                        | 30%        |
| Examen intermedio             | 20%        |
| Proyecto                      | 30%        |
| Presentación del proyecto     | 10%        |

Recuerda que esta clase es de *construir* habilidades. La única manera de construirlas es practicando.


#### Ejercicios del Proyecto Euler

Cada semana se asignará un problema del Proyecto Euler. Deberás entregar la solución en tu carpeta asignada, en la subcarpeta `project_euler` en `github`. El archivo debe de llamarse

```
ProjectEuler<número>.ipynb`
```

donde `número` es el número del ejercicio. El archivo deberá de contener una celda de encabezado con el título del problema y una celda en `markdown` con la descripción. Tu solución deberá de pasar el caso de prueba que regularmente viene incluido.

Deberá de entregarse antes de las `23:59` los domingos.

Obviamente las soluciones se pueden encontrar en la web, te recuerdo que copiar código viola las leyes de honestidad académica (ver más abajo) y además recuerda que que existe *software* que identifica código copiado...

#### Tareas

Las tareas serán especificadas cada semana y deberán entregarse el jueves posterior antes de las `23:59` en la carpeta `tareas`. Las instrucciones para nombrar los archivos (obviamente en tu carpeta de `github`) serán dados con la tarea.

#### Examen intermedio

El día 20 de octubre habrá un examen intermedio que estará basado en las tareas y temas vistos en clase, no debería de haber ningún problema.

#### Proyecto

A la mitad del curso, asignaré proyectos. Tendrás hasta el día **26 de Noviembre, 2021** antes de las `23:59` para subirlo a la carpeta `proyecto`.

### Calificación

Se usará la siguiente escala para las tareas

| Puntos | Descripción                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------|
| 5      | Excelente. Código limpio, conciso, documentado y exploró los conceptos en profundidad.                           |
| 4      | Completo y correcto. Incluye el análisis, el programa, el caso de pruebas y responde a las preguntas planteadas. |
| 3      | Contiene unos cuentos errores menores.                                                                           |
| 2      | Entrega parcial o tiene errores mayores.                                                                         |
| 1      | Le faltó mucho.                                                                                                  |
| 0      | Ni lo intentó :(                                                                                                 |


#### Calificación del proyecto

El proyecto se evaluará promediando las siguientes categorías. Se usará la escala recién mostrada en cada una de ellas.

| Categoría     | Descripción                                                                                                                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Diseño        | El proyecto está bien organizado, fácil de seguir y se especifica claramente el problema a resolver.                                                                                            |
| Documentación | Instrucciones de como ejecutar el código. Nombres de las variables y funciones son descriptivas. Incluye comentarios para que el lector pueda seguir el algoritmo. Se incluyen casos de prueba. |
| Completez     | Todos los elementos del proyecto están incluidos.                                                                                                                                               |
| Correcto      | La lógica del código es correcta y produce resultados con sentido.                                                                                                                              |
| Análisis      | Todas las preguntas de análisis en la descripción del proyecto fueron resueltas. La interpretación del resultado está incluida.                                                                 |


#### Demostración del proyecto

Al final del curso, tendrás que mostrar tu proyecto en 40 minutos a la clase. Se calificará por mí y por tus compañeros.


## Aclaraciones

* El código **NO** es la respuesta.
* La gráfica **NO** es la respuesta.
* Debes de **mostrar que entendiste la solución y el problema**.


## Código de conducta académica

*Adaptado del departamento de ciencias de la computación de Grand Valley State University y de  George Washington University)*

- Se espera que tú...

    - Crees / desarrolles tus tareas (incluyendo el código fuente).
    - Entiendas tus soluciones
    - Reconozcas la ayuda de otros en la escritura.
    - Cites la fuente en la tarea.
    - Te protejas de sospecha al no permitir que otros vean tu tarea antes de que sea enviada.
    - Contactes al profesor para aclarar los requerimientos de las tareas.
    - Uses extensivamente Github para *socializar* el conocimiento, soluciones, dudas, etc.

- Se prefiere que tú...

    - Discutas diversos caminos para alcanzar la solución.
    - Compartas tu conociemiento con otros estudiantes acerca de errores de sintáxis, trucos de código, etc.
    - Proveas y recibas ayuda respecto a errores de ejecución.
    - Proveas y recibas ayuda usando el ambiente de computación.
    - Participes, junto con otros estudiantes, en discuiones hacer de las tareas, requerimientos, estrategais de solución, etc.


- Eres culpable de romper el código de conducta si ...
    - Le das tu código fuente a cualquiera en formato electrónico o analógico.
    - Recibes de otro estudiante la solución en formato electrónico o analógico.
    - Subes al repositorio como tuyos otros archivos, soluciones o documentos.
    - Subes tareas sin indicar que colaboraste con alguien.
    - Realizas modificaciones al código en un esfuerzo de ocultar un engaño.
    - Usas material no permitido en examen o te comunicas con alguien de manera no autorizada durante el examen.

## Ligas de interes

- [Libro de git](http://git-scm.com/book)
- [Think python](http://www.greenteapress.com/thinkpython/)
- [Project Euler](http://projecteuler.net/)


Documento adaptado con permiso del Dr. Adolfo de Unánue Tiscareño
