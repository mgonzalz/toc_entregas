import sympy as sp
"""
Inicializa la clase Funcion, definiendo las funciones numéricas y sus derivadas.

Parámetros:
f1_sym : sympy.Expr - Ecuación simbólica 1. Representa la primera ecuación del sistema.
f2_sym : sympy.Expr - Ecuación simbólica 2. Representa la segunda ecuación del sistema.
C2 : sympy.Symbol - Variable simbólica C2. Variable que queremos resolver del sistema.
C3 : sympy.Symbol - Variable simbólica C3. Variable que queremos resolver del sistema.

"""

class Funcion():
    def __init__(self, f1_sym, f2_sym, C2, C3):
        # Definir las ecuaciones del sistema en formato numérico.
        self.f1 = sp.lambdify([C2, C3], f1_sym, 'numpy')
        self.f2 = sp.lambdify([C2, C3], f2_sym, 'numpy')
        self.df1_dC2 = sp.lambdify([C2, C3], sp.diff(f1_sym, C2), 'numpy')
        self.df1_dC3 = sp.lambdify([C2, C3], sp.diff(f1_sym, C3), 'numpy')
        self.df2_dC2 = sp.lambdify([C2, C3], sp.diff(f2_sym, C2), 'numpy')
        self.df2_dC3 = sp.lambdify([C2, C3], sp.diff(f2_sym, C3), 'numpy')
