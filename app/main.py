"""Point d'entrée principal de l'application.

Ce script démontre l'utilisation des fonctions du module mon_module
en effectuant des calculs mathématiques et en chargeant des données CSV.
"""

import os

import pandas as pd

from app.modules.mon_module import add, print_data, square, sub


def main() -> None:
    """Fonction principale de l'application.

    Cette fonction exécute une série d'opérations :
    - Effectue des calculs mathématiques
    - Charge et affiche les données d'un fichier CSV
    - Affiche les résultats
    """
    print("=== Démonstration des Fonctions Mathématiques ===")

    # Démonstration de la fonction add
    result_add = add(10, 2)
    print(f"Addition: 10 + 2 = {result_add}")

    result_add2 = add(20, 2)
    print(f"Addition: 20 + 2 = {result_add2}")

    # Démonstration de la fonction sub
    result_sub = sub(10, 2)
    print(f"Soustraction: 10 - 2 = {result_sub}")

    # Démonstration de la fonction square
    result_square = square(4)
    print(f"Carré: 4^2 = {result_square}")

    print("\n=== Traitement des Données CSV ===")

    # Chemin vers le fichier CSV
    csv_path = os.path.join(os.path.dirname(__file__), "moncsv.csv")

    # Chargement des données
    df = pd.read_csv(csv_path)

    # Affichage et comptage des lignes
    nb_lignes = print_data(df)
    print(f"\nNombre de lignes dans le DataFrame: {nb_lignes}")


if __name__ == "__main__":
    main()
