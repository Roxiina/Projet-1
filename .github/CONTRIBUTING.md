# Guide de Contribution

Merci de votre intérêt pour contribuer à ce projet ! Ce document décrit les lignes directrices pour contribuer de manière efficace.

## 📋 Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Processus de Pull Request](#processus-de-pull-request)
- [Standards de Code](#standards-de-code)
- [Tests](#tests)
- [Documentation](#documentation)

## 📜 Code de Conduite

En participant à ce projet, vous acceptez de respecter notre [Code de Conduite](CODE_OF_CONDUCT.md).

## 🚀 Comment Contribuer

### Signaler des Bugs

Les bugs sont suivis via [GitHub Issues](https://github.com/USERNAME/projet1/issues). Avant de créer un nouveau rapport de bug :

1. **Vérifiez** que le bug n'a pas déjà été signalé
2. **Utilisez** le template de bug report fourni
3. **Incluez** :
   - Description claire et concise du problème
   - Étapes pour reproduire le bug
   - Comportement attendu vs comportement observé
   - Captures d'écran si applicable
   - Informations sur votre environnement (OS, version Python, etc.)

### Proposer des Améliorations

Les suggestions d'améliorations sont également suivies via GitHub Issues :

1. **Vérifiez** que la fonctionnalité n'a pas déjà été proposée
2. **Décrivez** clairement la fonctionnalité souhaitée
3. **Expliquez** pourquoi cette fonctionnalité serait utile
4. **Proposez** une implémentation si possible

### Contribuer du Code

1. **Fork** le dépôt
2. **Créez** une branche depuis `dev` :
   ```bash
   git checkout -b feat/nom-fonctionnalite
   ```
3. **Développez** votre fonctionnalité
4. **Committez** vos changements :
   ```bash
   git commit -m "feat: ajout de la fonctionnalité X"
   ```
5. **Poussez** vers votre fork :
   ```bash
   git push origin feat/nom-fonctionnalite
   ```
6. **Ouvrez** une Pull Request

## 🔄 Processus de Pull Request

1. **Testez** localement avant de soumettre :
   ```bash
   uv run ruff check .
   uv run ruff format .
   uv run pytest
   ```

2. **Mettez à jour** la documentation si nécessaire

3. **Assurez-vous** que la couverture de tests reste >= 80%

4. **Suivez** les conventions de nommage des commits :
   - `feat:` pour une nouvelle fonctionnalité
   - `fix:` pour une correction de bug
   - `docs:` pour la documentation
   - `test:` pour les tests
   - `refactor:` pour le refactoring
   - `style:` pour le formatage
   - `chore:` pour les tâches de maintenance

5. **Attendez** la revue de code :
   - Les PR sont automatiquement testées via GitHub Actions
   - Au moins une revue est requise avant la fusion
   - Les commentaires doivent être résolus

6. **Ne fusionnez jamais** vos propres PR sans validation

## 📏 Standards de Code

### Style Python

- **Suivre** PEP 8 et les règles Ruff configurées
- **Ligne maximale** : 88 caractères
- **Imports** : Triés avec `isort` intégré à Ruff
- **Docstrings** : Format Google pour toutes les fonctions publiques

Exemple de docstring :

```python
def ma_fonction(param1: int, param2: str) -> bool:
    """Brève description de la fonction.

    Description plus détaillée si nécessaire.

    Args:
        param1: Description du premier paramètre.
        param2: Description du deuxième paramètre.

    Returns:
        Description de la valeur retournée.

    Raises:
        ValueError: Si param1 est négatif.

    Examples:
        >>> ma_fonction(10, "test")
        True
    """
    # Implémentation
```

### Structure des Commits

```
type(scope): description courte

Corps du commit expliquant les changements en détail.

Fixes #123
```

## 🧪 Tests

### Exigences

- **Couverture minimale** : 80%
- **Tests unitaires** pour toute nouvelle fonction
- **Tests paramétrés** quand applicable
- **Fixtures** pour les ressources réutilisables

### Exécution des Tests

```bash
# Tous les tests
uv run pytest

# Avec couverture
uv run pytest --cov=app --cov-report=term-missing

# Tests spécifiques
uv run pytest tests/test_math_csv.py -v

# Mode watch (nécessite pytest-watch)
uv run ptw
```

### Écrire de Bons Tests

- **Un test = un concept**
- **Noms descriptifs** : `test_add_with_positive_numbers`
- **AAA Pattern** : Arrange, Act, Assert
- **Pas de logique complexe** dans les tests
- **Tests indépendants** : Ne dépendent pas les uns des autres

## 📚 Documentation

### Docstrings

- **Toutes les fonctions publiques** doivent avoir une docstring
- **Format Google** obligatoire
- **Exemples** encouragés pour les fonctions complexes

### Documentation Sphinx

- Génération automatique depuis les docstrings
- Mettez à jour `docs/` si vous ajoutez de nouveaux modules
- Testez la génération localement :
  ```bash
  cd docs
  uv run sphinx-build -b html source build
  ```

### README

- Maintenez le README à jour
- Ajoutez des exemples d'utilisation
- Documentez les nouvelles fonctionnalités

## 🔍 Revue de Code

### En tant que Revieweur

- **Soyez constructif** et respectueux
- **Vérifiez** :
  - La qualité du code
  - Les tests
  - La documentation
  - Les performances
  - La sécurité
- **Proposez** des alternatives si nécessaire
- **Approuvez** seulement si tous les critères sont remplis

### En tant qu'Auteur

- **Répondez** aux commentaires de manière constructive
- **Clarifiez** vos choix d'implémentation
- **Modifiez** selon les retours
- **Testez** après chaque modification

## ❓ Questions

Si vous avez des questions, n'hésitez pas à :

- Ouvrir une [Discussion GitHub](https://github.com/USERNAME/projet1/discussions)
- Contacter les mainteneurs
- Consulter la [documentation](https://username.github.io/projet1/)

## 🎉 Reconnaissance

Tous les contributeurs seront ajoutés à la section [Contributeurs](../README.md#contributeurs) du README.

Merci de contribuer à améliorer ce projet ! 🚀

---

**Note** : Ce guide peut évoluer. Les contributeurs sont encouragés à proposer des améliorations.
