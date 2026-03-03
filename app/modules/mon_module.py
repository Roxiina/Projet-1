"""Module contenant les fonctions mathématiques et de traitement de données.

Ce module fournit des opérations mathématiques de base ainsi qu'une fonction
pour afficher et analyser des DataFrames Pandas.
"""

import pandas as pd


def add(a: float, b: float) -> float:
    """Additionne deux nombres.

    Args:
        a: Premier nombre.
        b: Deuxième nombre.

    Returns:
        La somme de a et b.

    Examples:
        >>> add(10, 2)
        12
        >>> add(20, 2)
        22

    """
    return a + b


def sub(a: float, b: float) -> float:
    """Soustrait deux nombres.

    Args:
        a: Premier nombre (le minuende).
        b: Deuxième nombre (le diminuende).

    Returns:
        La différence entre a et b.

    Examples:
        >>> sub(10, 2)
        8
        >>> sub(5, 3)
        2

    """
    return a - b


def square(a: float) -> float:
    """Calcule le carré.

    Élève un nombre au carré.

    Args:
        a: Le nombre à élever au carré.

    Returns:
        Le carré de a.

    Examples:
        >>> square(4)
        16
        >>> square(5)
        25

    """
    return a**2


def print_data(df: pd.DataFrame) -> int:
    """Affiche un DataFrame et retourne le nombre de lignes.

    Cette fonction affiche le contenu complet d'un DataFrame Pandas
    et retourne le nombre total de lignes qu'il contient.

    Args:
        df: Le DataFrame Pandas à afficher.

    Returns:
        Le nombre de lignes dans le DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> print_data(df)
           A  B
        0  1  4
        1  2  5
        2  3  6
        3

    """
    print(df)
    return len(df)
