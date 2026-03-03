"""Tests unitaires pour le module mon_module.

Ce module contient les tests pour toutes les fonctions de mon_module,
incluant la paramétrisation pour les fonctions mathématiques et
l'utilisation de fixtures pour les tests de DataFrame.
"""

import pandas as pd
import pytest

from app.modules.mon_module import add, print_data, square, sub


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 12),
        (20, 2, 22),
        (0, 2, 2),
        (-5, 3, -2),
        (100, -50, 50),
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    """Teste la fonction add avec plusieurs cas.

    Args:
        a: Premier nombre.
        b: Deuxième nombre.
        expected: Résultat attendu.

    """
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 8),
        (20, 5, 15),
        (0, 2, -2),
        (100, 100, 0),
        (-5, -3, -2),
    ],
)
def test_sub(a: float, b: float, expected: float) -> None:
    """Teste la fonction sub avec plusieurs cas.

    Args:
        a: Premier nombre.
        b: Deuxième nombre.
        expected: Résultat attendu.

    """
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    "a, expected",
    [
        (4, 16),
        (5, 25),
        (0, 0),
        (-3, 9),
        (10, 100),
    ],
)
def test_square(a: float, expected: float) -> None:
    """Teste la fonction square avec plusieurs cas.

    Args:
        a: Le nombre à élever au carré.
        expected: Résultat attendu.

    """
    assert square(a) == expected


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Fixture créant un DataFrame de test en mémoire.

    Returns:
        Un DataFrame Pandas contenant des données de test.

    """
    return pd.DataFrame(
        {
            "nom": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "score": [85, 92, 78],
        }
    )


@pytest.fixture
def empty_dataframe() -> pd.DataFrame:
    """Fixture créant un DataFrame vide.

    Returns:
        Un DataFrame Pandas vide.

    """
    return pd.DataFrame()


def test_print_data_with_data(
    sample_dataframe: pd.DataFrame, capsys: pytest.CaptureFixture
) -> None:
    """Teste print_data avec un DataFrame contenant des données.

    Args:
        sample_dataframe: Le DataFrame de test fourni par la fixture.
        capsys: Fixture pytest pour capturer la sortie stdout.

    """
    result = print_data(sample_dataframe)

    # Vérifier que la fonction retourne le bon nombre de lignes
    assert result == 3

    # Vérifier que le DataFrame a bien été affiché
    captured = capsys.readouterr()
    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "Charlie" in captured.out


def test_print_data_empty(
    empty_dataframe: pd.DataFrame, capsys: pytest.CaptureFixture
) -> None:
    """Teste print_data avec un DataFrame vide.

    Args:
        empty_dataframe: Le DataFrame vide fourni par la fixture.
        capsys: Fixture pytest pour capturer la sortie stdout.

    """
    result = print_data(empty_dataframe)

    # Vérifier que la fonction retourne 0 pour un DataFrame vide
    assert result == 0

    # Vérifier que quelque chose a été affiché
    captured = capsys.readouterr()
    assert "Empty DataFrame" in captured.out


def test_print_data_single_row(capsys: pytest.CaptureFixture) -> None:
    """Teste print_data avec un DataFrame d'une seule ligne.

    Args:
        capsys: Fixture pytest pour capturer la sortie stdout.

    """
    df = pd.DataFrame({"col1": [1], "col2": [2]})
    result = print_data(df)

    # Vérifier le nombre de lignes
    assert result == 1

    # Vérifier l'affichage
    captured = capsys.readouterr()
    assert "col1" in captured.out
    assert "col2" in captured.out
