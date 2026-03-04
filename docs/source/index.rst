.. Projet 1 documentation master file

🎯 Projet 1 : Template Professionnel Python
============================================

.. image:: https://github.com/Roxiina/Projet-1/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/Roxiina/Projet-1/actions/workflows/ci.yml
   :alt: CI Status

.. image:: https://github.com/Roxiina/Projet-1/actions/workflows/docs.yml/badge.svg
   :target: https://Roxiina.github.io/Projet-1/
   :alt: Documentation Status

.. image:: https://img.shields.io/badge/coverage-97%25-brightgreen.svg
   :target: https://github.com/Roxiina/Projet-1
   :alt: Test Coverage

.. image:: https://img.shields.io/badge/python-3.11+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/code%20style-ruff-000000.svg
   :target: https://docs.astral.sh/ruff/
   :alt: Code style: ruff

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

.. raw:: html

   <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 10px; margin: 2rem 0; color: white;">
      <h2 style="margin-top:0; color: white;">Toolbox de Référence pour l'IA</h2>
      <p style="font-size: 1.1rem; margin-bottom: 0;">
         Un environnement de développement moderne, automatisé et documenté servant de template 
         pour tous vos projets d'Intelligence Artificielle et Data Science.
      </p>
   </div>

----

🚀 Démarrage en 30 secondes
---------------------------

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         git clone https://github.com/Roxiina/Projet-1.git
         cd Projet-1
         uv sync
         uv run python app/main.py

   .. tab-item:: Windows

      .. code-block:: powershell

         git clone https://github.com/Roxiina/Projet-1.git
         cd Projet-1
         uv sync
         uv run python app/main.py

   .. tab-item:: Docker

      .. code-block:: bash

         git clone https://github.com/Roxiina/Projet-1.git
         cd Projet-1
         docker build -t projet1 .
         docker run --rm projet1

----

✨ Caractéristiques Principales
-------------------------------

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: 📦 Gestion Moderne des Dépendances
      :text-align: center

      Utilise **uv**, le gestionnaire ultra-rapide pour Python.
      Installation en quelques secondes, verrouillage reproductible.

   .. grid-item-card:: 🎨 Qualité de Code Automatisée
      :text-align: center

      **Ruff** pour le linting et formatage. 
      10-100x plus rapide que les outils traditionnels.

   .. grid-item-card:: 🧪 Tests Exhaustifs
      :text-align: center

      **Pytest** avec couverture de code.
      Tests paramétrés, fixtures, et rapports détaillés.

   .. grid-item-card:: 📚 Documentation Complète
      :text-align: center

      **Sphinx** avec thème **Furo** moderne.
      Documentation auto-générée depuis votre code.

   .. grid-item-card:: 🐳 Conteneurisation
      :text-align: center

      **Docker** pour des déploiements reproductibles.
      Images optimisées et sécurisées.

   .. grid-item-card:: ⚙️ CI/CD Automatique
      :text-align: center

      **GitHub Actions** pour tests et déploiements.
      Pipeline complet de qualité.

      **GitHub Actions** pour tests et déploiements.
      Pipeline complet de qualité.

----

📖 Guide de Documentation
-------------------------

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card:: 🎯 Guide de Démarrage
      :link: installation
      :link-type: doc

      Installation, configuration et premiers pas avec le projet.

   .. grid-item-card:: 💻 Guide d'Utilisation
      :link: usage
      :link-type: doc

      Exemples d'utilisation, API et bonnes pratiques.

   .. grid-item-card:: 📚 Référence API
      :link: api/modules
      :link-type: doc

      Documentation complète de toutes les fonctions et classes.

   .. grid-item-card:: 🤝 Contribuer
      :link: contributing
      :link-type: doc

      Comment contribuer au projet et guidelines.

----

🎓 Fonctionnalités Implémentées
--------------------------------

Le projet inclut des exemples concrets :

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Module
     - Description
   * - **🔢 Fonctions Mathématiques**
     - Addition, soustraction, carré avec type hints complets
   * - **📊 Traitement CSV**
     - Lecture et manipulation de données avec Pandas
   * - **🧪 Tests Paramétrés**
     - Suite complète avec pytest, fixtures et 97% de couverture
   * - **📝 Documentation**
     - Docstrings Google format, génération Sphinx automatique
   * - **🐳 Docker**
     - Conteneurisation avec optimisation d'image
   * - **⚙️ CI/CD**
     - Workflows GitHub Actions pour tests et qualité

----

Table des Matières
------------------

.. toctree::
   :maxdepth: 2
   :caption: 📘 Documentation Utilisateur

   installation
   usage

.. toctree::
   :maxdepth: 2
   :caption: 🔧 Référence Technique

   api/modules

.. toctree::
   :maxdepth: 1
   :caption: 🤝 Contribution & Communauté

   contributing
   code_of_conduct

.. toctree::
   :maxdepth: 1
   :caption: 📄 Informations Légales

   changelog
   license

----

🔍 Recherche Rapide
-------------------

* :ref:`genindex` - Index général
* :ref:`modindex` - Index des modules
* :ref:`search` - Rechercher dans la documentation
