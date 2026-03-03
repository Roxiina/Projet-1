📦 Installation
===============

Cette page décrit comment installer et configurer le Projet 1 sur votre machine.

.. admonition:: ⚡ Installation Rapide
   :class: tip

   Pour les utilisateurs pressés :

   .. code-block:: bash

      git clone https://github.com/Roxiina/Projet-1.git
      cd Projet-1
      uv sync
      uv run python app/main.py

----

🔧 Prérequis
------------

Avant de commencer, assurez-vous d'avoir :

.. grid:: 1 1 2 3
   :gutter: 2

   .. grid-item-card:: 🐍 Python
      :text-align: center

      Version **3.11** ou supérieure

      `Télécharger Python <https://www.python.org/downloads/>`_

   .. grid-item-card:: ⚡ uv
      :text-align: center

      Gestionnaire de dépendances moderne

      `Installer uv <https://github.com/astral-sh/uv>`_

   .. grid-item-card:: 📂 Git
      :text-align: center

      Pour cloner le dépôt

      `Télécharger Git <https://git-scm.com/>`_

----

⚡ Installation de uv
---------------------

Si vous n'avez pas encore installé ``uv``, suivez ces instructions :

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         curl -LsSf https://astral.sh/uv/install.sh | sh

   .. tab-item:: Windows (PowerShell)

      .. code-block:: powershell

         irm https://astral.sh/uv/install.ps1 | iex

   .. tab-item:: Alternative (via pip)

      .. code-block:: bash

         pip install uv

----

🚀 Installation du Projet
--------------------------

.. grid:: 1

   .. grid-item::

      **Étape 1️⃣ : Cloner le dépôt**

      .. code-block:: bash

         git clone https://github.com/Roxiina/Projet-1.git
         cd Projet-1

   .. grid-item::

      **Étape 2️⃣ : Installer les dépendances**

      .. tab-set::

         .. tab-item:: Production

            .. code-block:: bash

               uv sync --no-dev

         .. tab-item:: Développement (Recommandé)

            .. code-block:: bash

               uv sync

   .. grid-item::

      **Étape 3️⃣ : Vérifier l'installation**

      .. code-block:: bash

         # Exécuter l'application
         uv run python app/main.py

         # Lancer les tests
         uv run pytest

      .. admonition:: ✅ Succès !
         :class: tip

         Si tout fonctionne correctement, vous devriez voir l'application s'exécuter avec la sortie des fonctions mathématiques et du traitement CSV.

----

🐳 Installation avec Docker
----------------------------

Si vous préférez utiliser Docker pour une installation isolée :

.. code-block:: bash

   # Construire l'image
   docker build -t projet1:latest .

   # Exécuter le conteneur
   docker run --rm projet1:latest

.. admonition:: 💡 Astuce Docker
   :class: note

   L'image Docker est optimisée avec un ``.dockerignore`` et utilise Python 3.11-slim pour une taille réduite.

----

🛠️ Configuration de l'Environnement de Développement
-----------------------------------------------------

Pour une expérience de développement optimale :

.. code-block:: bash

   # Installation complète avec outils de dev
   uv sync

   # Vérifier la configuration Ruff
   uv run ruff check .

   # Exécuter les tests avec couverture
   uv run pytest --cov=app --cov-report=html

----

🔴 Dépannage
------------

.. dropdown:: ❌ Problème de Version Python
   :color: danger

   Si vous obtenez une erreur liée à la version Python :

   .. code-block:: bash

      # Vérifier la version Python
      python --version

      # Mettre à jour la version cible avec uv
      uv python pin 3.11

.. dropdown:: ❌ Problème d'Installation des Dépendances
   :color: danger

   Si l'installation échoue :

   .. code-block:: bash

      # Nettoyer le cache uv
      uv cache clean

      # Réessayer l'installation
      uv sync --reinstall

.. dropdown:: ❌ Docker non disponible
   :color: danger

   Si Docker n'est pas installé :

   - Téléchargez `Docker Desktop <https://www.docker.com/products/docker-desktop/>`_
   - Démarrez Docker Desktop
   - Relancez la commande ``docker build``

----

📚 Prochaines Étapes
--------------------

Maintenant que l'installation est terminée, consultez :

.. grid:: 1 1 2 2
   :gutter: 2

   .. grid-item-card:: 📖 Guide d'Utilisation
      :link: usage
      :link-type: doc

      Découvrez comment utiliser les fonctionnalités du projet

   .. grid-item-card:: 📚 Référence API
      :link: api/modules
      :link-type: doc

      Documentation complète de toutes les fonctions

Étapes Suivantes
----------------

Maintenant que le projet est installé, consultez le :doc:`usage` pour apprendre à l'utiliser.
