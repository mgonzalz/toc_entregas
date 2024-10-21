import sympy as sp
import numpy as np
'''
Resuelve un sistema de ecuaciones no lineales utilizando el método de Newton-Raphson.

Parámetros:
solver : object - Una instancia de la clase Funcion que contiene los métodos necesarios para calcular los valores de las funciones y sus derivadas parciales.
C2_0 : float - Valor inicial de la variable C2.
C3_0 : float - Valor inicial de la variable C3.
tol : float, opcional - Tolerancia para el criterio de convergencia. Por defecto, precisión hasta el octavo decimal.
max_iter : int, opcional - Número máximo de iteraciones permitidas. Por defecto, número máximo de iteraciones 400.

Retorna:
tuple - Una tupla (C2, C3) con las soluciones aproximadas para las variables del sistema.

'''

def newton_raphson(solver, C2_0, C3_0, tol=1e-8, max_iter=400):
    C2 = C2_0
    C3 = C3_0

    for i in range(max_iter):
        # VECTOR F.
        F1_val = solver.f1(C2, C3)
        F2_val = solver.f2(C2, C3)
        F = np.array([F1_val, F2_val])

        # JACOBIANO.
        J = np.array([
            [solver.df1_dC2(C2, C3), solver.df1_dC3(C2, C3)],
            [solver.df2_dC2(C2, C3), solver.df2_dC3(C2, C3)]
        ])
        J_inv = np.linalg.inv(J)

        # X_N+1 = X_N - J^-1 * F
        delta = np.dot(J_inv, F)
        C2 -= delta[0]
        C3 -= delta[1]

        # CRITERIO DE CONVERGENCIA
        if np.linalg.norm(F) < tol:
            break

    return C2, C3
