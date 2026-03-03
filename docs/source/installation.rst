Installation
============

Cette page décrit comment installer et configurer le Projet 1 sur votre machine.

Prérequis
---------

Avant de commencer, assurez-vous d'avoir :

* Python 3.11 ou supérieur
* `uv <https://github.com/astral-sh/uv>`_ installé
* Git pour cloner le dépôt

Installation de uv
------------------

Si vous n'avez pas encore installé ``uv``, suivez ces instructions :

.. code-block:: bash

   # Sur macOS et Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Sur Windows (PowerShell)
   irm https://astral.sh/uv/install.ps1 | iex

Installation du Projet
----------------------

Étape 1: Cloner le dépôt
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/USERNAME/projet1.git
   cd projet1

Étape 2: Installer les dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Installation des dépendances de production
   uv sync

   # Installation avec les dépendances de développement
   uv sync --all-extras

Étape 3: Vérifier l'installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Exécuter l'application
   uv run python app/main.py

   # Lancer les tests
   uv run pytest

Si tout fonctionne correctement, vous devriez voir l'application s'exécuter sans erreur.

Installation avec Docker
------------------------

Si vous préférez utiliser Docker :

.. code-block:: bash

   # Construire l'image
   docker build -t projet1:latest .

   # Exécuter le conteneur
   docker run --rm projet1:latest

Configuration de l'Environnement de Développement
--------------------------------------------------

Pour le développement, il est recommandé d'installer les hooks pre-commit :

.. code-block:: bash

   # Installer pre-commit
   uv add --dev pre-commit

   # Installer les hooks
   uv run pre-commit install

Cela garantit que votre code est vérifié automatiquement avant chaque commit.

Dépannage
---------

Problème de Version Python
^^^^^^^^^^^^^^^^^^^^^^^^^^

Si vous obtenez une erreur liée à la version Python :

.. code-block:: bash

   # Vérifier la version Python
   python --version

   # Mettre à jour la version cible
   uv python pin 3.11

Problème d'Installation des Dépendances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si l'installation échoue :

.. code-block:: bash

   # Nettoyer le cache
   uv cache clean

   # Réessayer l'installation
   uv sync --reinstall

Étapes Suivantes
----------------

Maintenant que le projet est installé, consultez le :doc:`usage` pour apprendre à l'utiliser.
