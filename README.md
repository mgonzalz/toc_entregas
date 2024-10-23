# Técnicas de Optimización y Control: Caso práctico.
## Repositorio.
- Link: https://github.com/mgonzalz/toc_entrega-1.git
- Usuario: @mgonzalz
## Contenido.
### Estructura del Proyecto.
- Caso práctico: Este archivo Jupyter Notebook resuelve todo el ejercicio de manera interactiva. En él, se pueden visualizar las curvas, realizar simulaciones y analizar los resultados de forma clara y concisa.
- Newton-Raphson: La carpeta alberga el archivo `main.py`, punto de entrada del proyecto y ejecuta el algoritmo de Newton-Raphson. La carpeta modulos alberga las funciones y clases necesarias para resolver el problema, permitiendo que el proyecto se ejecute y funcione correctamente.

#### Estructura de Carpetas.
````
/toc_entrega-1/
│
├── newton_raphson/
│   ├── main.py          # Archivo principal que ejecuta el algoritmo de Newton-Raphson.
│
│   ├── modulos/
│      ├── funcion.py       # Contiene las clases necesarias para los cálculos.
│      ├── newton.py        # Implementación de la función de Newton-Raphson.
│
├── caso_practico.ipynb  # Notebook que resuelve todo el ejercicio.
│
└── requirements.txt      # Archivo con las dependencias del proyecto.
````

### Ejecución Newton-Raphson.
Ejecuta el archivo principal `main.py` ubicado en la carpeta `newton-raphson` para la resolución del sistema de ecuaciones propuesto a través de Newton-Raphson.

Para poder instalar todas las dependencias necesarias:
```bash
pip install -r requirements.txt
```
## Enunciado.

Los economistas del Banco Central Europeo han ajustado los datos de variación de la tasa de ahorro de las familias ($ \% \Delta$ Tasa de ahorro) en función de la variación del PIB ($\% \Delta$ PIB) y la variación del consumo de los hogares (\%$\Delta$CH) en función del tiempo $t$ en trimestres. Todas las tasas de variación son inter-trimestrales. Si consideramos, para simplificar el problema, que $x = \% \Delta PIB$ e $y = \% \Delta CH$, la ecuación a optimizar es:
$$
\% \Delta \text{Tasa de ahorro} = J = \int \left[ (1 + t^2) \cdot (\Delta PIB_t) + (\Delta CH_t) + \left( \frac{\partial \Delta PIB_t}{\partial t} \right)^2 + \left( \frac{\partial \Delta CH_t}{\partial t} \right)^3 \right] \, dt
$$
$$
\% \Delta \text{Tasa de ahorro} = J = \int \left[ (1 + t^2) \cdot x(t) + y(t) + \left( \frac{\partial x(t)}{\partial t} \right)^2 + \left( \frac{\partial y(t)}{\partial t} \right)^3 \right] \, dt
$$

- **Apartado A.** Mediante el cálculo de variaciones, calcular las curvas óptimas de PIB y de consumo de los hogares ($CH$) en función de $t$ (en función de las constantes de integración), que optimizan el problema.

- **Apartado B.** Se ha establecido para la simulación que para $t = 0.5$ la tasa de variación del PIB y del consumo de los hogares es del 0.5\%. De igual modo, para $t = 1$ las tasas de variación del PIB y del consumo de los hogares son del 1\%. Calcular las curvas óptimas bajo estas condiciones de contorno. Dibujar las curvas. *Nota: se aconseja usar métodos numéricos, especialmente el método de Newton-Raphson.*
    
- **Apartado C.** Los economistas necesitan saber si existe un punto $t^*$ que iguale las curvas de optimización. Demostrar si existe este punto desde un punto de vista gráfico dentro de los intervalos de $t$ de 0 a 2. ¿Qué significado económico podemos concluir tras este análisis?
    
- **Apartado D.** Aplicando la distancia por diferencias (diferencia entre los valores de $x^*$ e $y^*$), calcular el punto $t^*$ que minimice dicha distancia entre las curvas. Razonar la respuesta e indicar cómo usar este parámetro desde un punto de vista económico.*Nota: se aconseja usar métodos numéricos, especialmente el método de Newton-Raphson*.

Las nuevas políticas fiscales establecidas por la UE y la incertidumbre de cómo impactarán los conflictos en Oriente Medio y la guerra de Ucrania en la economía de
la UE, hace necesario establecer una función de control de cada una de las variables en función del incremento de la inflación ($u(t)$ y $v(t)$). En este sentido, se establecen dos funciones de control:
$$
\frac{\partial \Delta PIB_t}{\partial t} = u(t) \quad \rightarrow \quad \frac{\partial \Delta CH_t}{\partial t} = v(t)
$$
Aplicando técnicas de control óptimo, el equipo económico necesita conocer las curvas
optimizadas de la función $J$, así como las funciones $u$ y $v$ optimizadas en función de $t$.
En este caso, dejar la solución en función de las constantes de integración.

Dado el caso de uso, enumeras tres conclusiones desde el punto de vista economico y matematico.
