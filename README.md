# Técnicas de Optimización y Control: Caso práctico.
## Introducción.
Este proyecto aplica técnicas de Cálculo de Variaciones y Control Óptimo para optimizar sistemas económicos. Se analiza la interacción entre el PIB, el consumo de los hogares y su impacto en la tasa de ahorro, utilizando modelos matemáticos avanzados.

El caso práctico incluye el uso del método de Newton-Raphson para calcular curvas óptimas bajo condiciones de contorno realistas. Además, se realiza un análisis gráfico para identificar puntos de equilibrio entre las trayectorias optimizadas.

Este enfoque combina teoría y práctica, demostrando cómo estas herramientas matemáticas pueden influir en la toma de decisiones económicas en entornos dinámicos y con incertidumbre.

## Estructura del Proyecto.
- Caso práctico: Este archivo Jupyter Notebook resuelve todo el ejercicio de manera interactiva. En él, se pueden visualizar las curvas, realizar simulaciones y analizar los resultados de forma clara y concisa.
- Newton-Raphson: La carpeta alberga el archivo `main.py`, punto de entrada del proyecto y ejecuta el algoritmo de Newton-Raphson. La carpeta modulos alberga las funciones y clases necesarias para resolver el problema, permitiendo que el proyecto se ejecute y funcione correctamente.
- Docs: Esta carpeta contiene una versión redactada del caso práctico en formato PDF, con la solución detallada y conclusiones ampliadas para una mejor comprensión del análisis.

### Estructura de Carpetas.
````
/toc_entregass/
│
├── docs/       # Contiene la versión redactada del documento en PDF, realizada en LaTeX.
│
├── newton_raphson/
│   ├── main.py          # Archivo principal que ejecuta el algoritmo de Newton-Raphson.
│   │
│   ├── modulos/
│      ├── funcion.py       # Contiene las clases necesarias para los cálculos.
│      │
│      ├── newton.py        # Implementación de la función de Newton-Raphson.
│
├── caso_practico.ipynb  # Notebook que resuelve todo el ejercicio.
│
└── requirements.txt      # Archivo con las dependencias del proyecto.
````
