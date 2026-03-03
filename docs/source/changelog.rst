Changelog
=========

Toutes les modifications notables de ce projet seront documentées dans cette section.

Le format est basé sur `Keep a Changelog <https://keepachangelog.com/fr/1.0.0/>`_,
et ce projet adhère au `Versionnage Sémantique <https://semver.org/lang/fr/>`_.

[0.1.0] - 2026-03-03
--------------------

Added
^^^^^

* **Configuration initiale du projet**

  * Initialisation avec ``uv``
  * Configuration de ``pyproject.toml`` avec Ruff et Pytest
  * Structure modulaire du projet

* **Fonctionnalités principales**

  * Module ``mon_module`` avec fonctions mathématiques (add, sub, square)
  * Fonction ``print_data`` pour traiter les DataFrames Pandas
  * Application principale dans ``main.py``
  * Fichier CSV d'exemple

* **Tests**

  * Suite de tests complète avec Pytest
  * Tests paramétrés pour les fonctions mathématiques
  * Fixtures pour les tests de DataFrame
  * Couverture de code >= 80%

* **Documentation**

  * Documentation Sphinx avec thème Furo
  * Docstrings au format Google pour toutes les fonctions
  * README complet avec badges
  * Guide de contribution (CONTRIBUTING.md)
  * Code de conduite (CODE_OF_CONDUCT.md)

* **Infrastructure**

  * Dockerfile pour conteneurisation
  * GitHub Actions pour CI/CD
  * Vérifications automatiques : linting, tests, sécurité
  * Build Docker automatique

* **Qualité de code**

  * Configuration Ruff pour linting et formatage
  * Configuration Pytest pour tests et couverture
  * Intégration continue validant la qualité

[Non publié] - À venir
----------------------

Planned
^^^^^^^

* Intégration de pre-commit hooks
* Ajout de tests d'intégration
* Amélioration de la documentation API
* Tutoriels interactifs
* Support pour Python 3.12+

Format du Changelog
-------------------

Les versions sont organisées de la plus récente à la plus ancienne.

Chaque version utilise les catégories suivantes :

* **Added** : Nouvelles fonctionnalités
* **Changed** : Modifications de fonctionnalités existantes
* **Deprecated** : Fonctionnalités bientôt retirées
* **Removed** : Fonctionnalités retirées
* **Fixed** : Corrections de bugs
* **Security** : Corrections de sécurité

Références
----------

* `Keep a Changelog <https://keepachangelog.com/fr/1.0.0/>`_
* `Semantic Versioning <https://semver.org/lang/fr/>`_
