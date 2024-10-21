from modulos.funcion import Funcion
from modulos.newton import newton_raphson
import sympy as sp

if __name__ == "__main__":
    # Definir variables simbólicas
    C2, C3 = sp.symbols('C2 C3')

    # Definir las ecuaciones del sistema
    f1_sym = C2 + (2 * (3 + C3)**(3/2)) / 27 - 1
    f2_sym = C2 + (2 * (1.5 + C3)**(3/2)) / 27 - 0.5

    # Crear una instancia de la clase Función para definir las funciones numéricas y sus derivadas.
    solver = Funcion(f1_sym, f2_sym, C2, C3)

    # Valores iniciales
    C2_0 = 0.5
    C3_0 = 0.5

    # Newton-Raphson
    C2_final, C3_final = newton_raphson(solver, C2_0, C3_0)

    print(f"Solución: C2 = {C2_final}, C3 = {C3_final}")
