.. Projet 1 documentation master file

Bienvenue dans la Documentation de Projet 1
============================================

.. image:: https://img.shields.io/badge/python-3.11+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/code%20style-ruff-000000.svg
   :target: https://docs.astral.sh/ruff/
   :alt: Code style: ruff

**Projet 1** est une toolbox de référence pour le développement professionnel en IA, 
intégrant les meilleures pratiques de l'industrie.

Caractéristiques Principales
-----------------------------

* ✅ Gestion de dépendances moderne avec ``uv``
* ✅ Qualité de code automatisée avec ``Ruff``
* ✅ Tests unitaires et couverture avec ``Pytest``
* ✅ Documentation technique avec ``Sphinx`` et ``Furo``
* ✅ Conteneurisation avec ``Docker``
* ✅ CI/CD avec ``GitHub Actions``

Guide de Démarrage Rapide
--------------------------

Installation
^^^^^^^^^^^^

.. code-block:: bash

   # Cloner le dépôt
   git clone https://github.com/USERNAME/projet1.git
   cd projet1

   # Installer les dépendances
   uv sync

Utilisation
^^^^^^^^^^^

.. code-block:: bash

   # Exécuter l'application
   uv run python app/main.py

   # Lancer les tests
   uv run pytest

   # Vérifier la qualité du code
   uv run ruff check .

Table des Matières
------------------

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   installation
   usage
   api/modules

.. toctree::
   :maxdepth: 1
   :caption: Contribution

   contributing
   code_of_conduct

.. toctree::
   :maxdepth: 1
   :caption: Référence

   changelog
   license

Indices et Tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
