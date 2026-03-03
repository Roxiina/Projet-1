Guide d'Utilisation
===================

Ce guide vous montre comment utiliser les différentes fonctionnalités du Projet 1.

Exécution de l'Application
---------------------------

L'application principale peut être exécutée de plusieurs manières.

Exécution Locale
^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Avec uv
   uv run python app/main.py

   # Avec l'environnement virtuel activé
   source .venv/bin/activate  # Linux/macOS
   # ou
   .venv\Scripts\activate  # Windows
   python app/main.py

Exécution avec Docker
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Construire et exécuter
   docker build -t projet1 .
   docker run --rm projet1

Utilisation des Fonctions Mathématiques
----------------------------------------

Le module ``mon_module`` fournit plusieurs fonctions mathématiques.

Addition
^^^^^^^^

.. code-block:: python

   from app.modules.mon_module import add

   result = add(10, 5)
   print(result)  # Affiche: 15

Soustraction
^^^^^^^^^^^^

.. code-block:: python

   from app.modules.mon_module import sub

   result = sub(10, 5)
   print(result)  # Affiche: 5

Carré
^^^^^

.. code-block:: python

   from app.modules.mon_module import square

   result = square(4)
   print(result)  # Affiche: 16

Traitement de Données CSV
--------------------------

La fonction ``print_data`` permet d'afficher et d'analyser des DataFrames Pandas.

Exemple Simple
^^^^^^^^^^^^^^

.. code-block:: python

   import pandas as pd
   from app.modules.mon_module import print_data

   # Créer un DataFrame
   df = pd.DataFrame({
       'nom': ['Alice', 'Bob'],
       'age': [25, 30]
   })

   # Afficher et compter les lignes
   nb_lignes = print_data(df)
   print(f"Nombre de lignes: {nb_lignes}")

Lecture depuis un Fichier CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import pandas as pd
   from app.modules.mon_module import print_data

   # Charger le CSV
   df = pd.read_csv('app/moncsv.csv')

   # Traiter les données
   nb_lignes = print_data(df)

Tests
-----

Le projet utilise Pytest pour les tests automatisés.

Exécuter Tous les Tests
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   uv run pytest

Tests avec Couverture
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Rapport dans le terminal
   uv run pytest --cov=app --cov-report=term-missing

   # Rapport HTML
   uv run pytest --cov=app --cov-report=html
   # Ouvrir htmlcov/index.html

Tests Spécifiques
^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Tester un fichier spécifique
   uv run pytest tests/test_math_csv.py

   # Tester une fonction spécifique
   uv run pytest tests/test_math_csv.py::test_add

   # Mode verbose
   uv run pytest -v

Qualité du Code
---------------

Vérification avec Ruff
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Vérifier le code
   uv run ruff check .

   # Corriger automatiquement les problèmes
   uv run ruff check . --fix

   # Vérifier le formatage
   uv run ruff format --check .

   # Formater le code
   uv run ruff format .

Comprendre les Erreurs Ruff
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ruff vérifie plusieurs catégories d'erreurs :

* **E/W** : Erreurs et avertissements de style (PEP 8)
* **F** : Erreurs de logique détectées par Pyflakes
* **I** : Problèmes d'imports (ordre, utilisation)
* **D** : Problèmes de docstrings

Exemple de correction :

.. code-block:: python

   # ❌ Avant (erreur D)
   def ma_fonction(x):
       return x * 2

   # ✅ Après
   def ma_fonction(x: int) -> int:
       """Double la valeur d'entrée.

       Args:
           x: La valeur à doubler.

       Returns:
           Le double de x.
       """
       return x * 2

Documentation
-------------

Générer la Documentation
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   cd docs
   uv run sphinx-build -b html source build

La documentation sera générée dans ``docs/build/html/``.

Ouvrir la Documentation
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Linux/macOS
   open docs/build/html/index.html

   # Windows
   start docs/build/html/index.html

Workflow de Développement
--------------------------

Workflow Git Recommandé
^^^^^^^^^^^^^^^^^^^^^^^

1. Créer une branche de fonctionnalité :

   .. code-block:: bash

      git checkout -b feat/ma-fonctionnalite

2. Développer et tester :

   .. code-block:: bash

      # Coder
      # ...

      # Vérifier
      uv run ruff check .
      uv run ruff format .
      uv run pytest

3. Committer :

   .. code-block:: bash

      git add .
      git commit -m "feat: ajout de ma fonctionnalité"

4. Pousser et créer une Pull Request :

   .. code-block:: bash

      git push origin feat/ma-fonctionnalite

Bonnes Pratiques
^^^^^^^^^^^^^^^^

* ✅ Toujours tester avant de committer
* ✅ Maintenir une couverture de tests >= 80%
* ✅ Documenter toutes les fonctions publiques
* ✅ Suivre les conventions de nommage
* ✅ Utiliser des messages de commit descriptifs

Dépannage
---------

Problèmes Courants
^^^^^^^^^^^^^^^^^^

**Erreur d'Import de Module**

Si vous obtenez une erreur ``ModuleNotFoundError`` :

.. code-block:: bash

   # Vérifier que l'environnement est synchronisé
   uv sync

   # Définir PYTHONPATH
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/macOS
   $env:PYTHONPATH = "$(pwd)"  # Windows PowerShell

**Tests qui Échouent**

Si les tests échouent :

1. Vérifier que toutes les dépendances sont installées
2. Lire attentivement le message d'erreur
3. Exécuter les tests en mode verbose : ``uv run pytest -v``
4. Isoler le test qui échoue

Ressources Supplémentaires
---------------------------

* :doc:`api/modules` - Documentation API complète
* :doc:`contributing` - Guide de contribution
* `Documentation Pytest <https://docs.pytest.org/>`_
* `Documentation Ruff <https://docs.astral.sh/ruff/>`_
