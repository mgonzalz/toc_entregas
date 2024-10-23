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
