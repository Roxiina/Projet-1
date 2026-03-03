Guide de Contribution
=====================

Pour contribuer à ce projet, veuillez consulter le fichier complet de contribution sur GitHub :

`CONTRIBUTING.md <https://github.com/USERNAME/projet1/blob/main/.github/CONTRIBUTING.md>`_

Résumé des Étapes
-----------------

1. **Fork** le dépôt
2. **Créez** une branche de fonctionnalité (``feat/ma-fonctionnalite``)
3. **Développez** votre fonctionnalité avec des tests
4. **Committez** vos changements (``git commit -m 'feat: ajout de ...'``)
5. **Poussez** vers votre fork (``git push origin feat/ma-fonctionnalite``)
6. **Ouvrez** une Pull Request

Standards de Qualité
--------------------

Avant de soumettre votre contribution :

.. code-block:: bash

   # Vérifier le formatage
   uv run ruff check .
   uv run ruff format .

   # Exécuter les tests
   uv run pytest

   # Vérifier la couverture (>= 80%)
   uv run pytest --cov=app --cov-report=term-missing

Conventions de Commit
---------------------

Utilisez les préfixes suivants pour vos messages de commit :

* ``feat:`` - Nouvelle fonctionnalité
* ``fix:`` - Correction de bug
* ``docs:`` - Documentation
* ``test:`` - Tests
* ``refactor:`` - Refactoring
* ``style:`` - Formatage
* ``chore:`` - Maintenance

Exemple :

.. code-block:: bash

   git commit -m "feat: ajout de la fonction de calcul de moyenne"

Pour plus de détails, consultez le guide complet de contribution.
