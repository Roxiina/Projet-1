"""Tests pour le module main.

Ce module teste le bon fonctionnement de l'application principale.
"""

from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from app.main import main


def test_main_execution(capsys: pytest.CaptureFixture) -> None:
    """Teste l'exécution complète de la fonction main.

    Args:
        capsys: Fixture pytest pour capturer la sortie stdout.

    """
    # Créer un DataFrame de test
    df = pd.DataFrame(
        {
            "nom": ["Alice", "Bob", "Charlie"],
            "age": [25, 30, 35],
            "ville": ["Paris", "Lyon", "Marseille"],
            "score": [85, 92, 78],
        }
    )

    # Mock de pd.read_csv pour simuler la lecture du fichier
    with patch("app.main.pd.read_csv") as mock_read_csv:
        mock_read_csv.return_value = df

        # Exécuter la fonction main
        main()

        # Vérifier que read_csv a été appelé
        mock_read_csv.assert_called_once()

        # Capturer la sortie
        captured = capsys.readouterr()

        # Vérifications de la sortie
        assert "Démonstration des Fonctions Mathématiques" in captured.out
        assert "Addition: 10 + 2 = 12" in captured.out
        assert "Addition: 20 + 2 = 22" in captured.out
        assert "Soustraction: 10 - 2 = 8" in captured.out
        assert "Carré: 4^2 = 16" in captured.out
        assert "Traitement des Données CSV" in captured.out
        assert "Alice" in captured.out
        assert "Bob" in captured.out
        assert "Charlie" in captured.out
        assert "Nombre de lignes dans le DataFrame: 3" in captured.out


def test_main_with_actual_file(capsys: pytest.CaptureFixture, tmp_path) -> None:
    """Teste main avec un vrai fichier CSV temporaire.

    Args:
        capsys: Fixture pytest pour capturer la sortie stdout.
        tmp_path: Fixture pytest fournissant un répertoire temporaire.

    """
    # Créer un fichier CSV temporaire
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("nom,age,ville,score\nTest,20,City,90\n")

    # Mock du chemin du fichier CSV
    with patch("os.path.join", return_value=str(csv_file)):
        main()

        captured = capsys.readouterr()

        # Vérifications
        assert "Test" in captured.out
        assert "Nombre de lignes dans le DataFrame: 1" in captured.out
