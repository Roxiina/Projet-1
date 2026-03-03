# Projet 1 : Fondations, Standardisation et Excellence Technique

![CI Status](https://github.com/Roxiina/Projet-1/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Toolbox de référence pour le développement professionnel en IA**  
> Un environnement de développement moderne, automatisé et documenté servant de template pour tous vos projets d'IA.

## 📋 Description

Ce projet constitue une base solide pour le développement d'applications Python professionnelles. Il intègre les meilleures pratiques de l'industrie :

- ✅ Gestion de dépendances moderne avec `uv`
- ✅ Qualité de code automatisée avec `Ruff`
- ✅ Tests unitaires et couverture avec `Pytest`
- ✅ Documentation technique avec `Sphinx` et `Furo`
- ✅ Conteneurisation avec `Docker`
- ✅ CI/CD avec `GitHub Actions`

## 🚀 Installation

### Prérequis

- Python 3.11 ou supérieur
- [uv](https://github.com/astral-sh/uv) installé sur votre système

### Configuration de l'environnement

```bash
# Cloner le dépôt
git clone https://github.com/Roxiina/Projet-1.git
cd Projet-1

# Installer les dépendances avec uv
uv sync

# Activer l'environnement virtuel (si nécessaire)
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate  # Windows
```

## 🎯 Utilisation

### Exécution de l'application

```bash
# Exécuter l'application principale
uv run python app/main.py
```

### Tests

```bash
# Exécuter tous les tests
uv run pytest

# Exécuter les tests avec rapport de couverture
uv run pytest --cov=app --cov-report=term-missing

# Exécuter les tests en mode verbose
uv run pytest -v
```

### Qualité du code

```bash
# Vérifier le code avec Ruff
uv run ruff check .

# Formater automatiquement le code
uv run ruff format .

# Vérifier et corriger en une commande
uv run ruff check . --fix
```

### Documentation

```bash
# Générer la documentation HTML
cd docs
uv run sphinx-build -b html source build

# Ouvrir la documentation
# Linux/macOS
open build/html/index.html
# Windows
start build/html/index.html
```

## 🐳 Docker

### Construction de l'image

```bash
docker build -t projet1:latest .
```

### Exécution du conteneur

```bash
docker run --rm projet1:latest
```

## 📁 Structure du Projet

```plaintext
.
├── .github/
│   ├── workflows/
│   │   └── ci.yml              # Pipeline CI/CD
│   ├── CONTRIBUTING.md         # Guide de contribution
│   └── CODE_OF_CONDUCT.md      # Code de conduite
├── app/
│   ├── modules/
│   │   ├── __init__.py
│   │   └── mon_module.py       # Logique métier
│   ├── __init__.py
│   ├── main.py                 # Point d'entrée
│   └── moncsv.csv              # Données d'exemple
├── tests/
│   ├── __init__.py
│   └── test_math_csv.py        # Tests unitaires
├── docs/                       # Documentation Sphinx
├── pyproject.toml              # Configuration centralisée
├── uv.lock                     # Verrouillage des dépendances
├── Dockerfile                  # Conteneurisation
├── LICENSE                     # Licence MIT
└── README.md                   # Ce fichier
```

## 🧪 Fonctionnalités

Le projet implémente les fonctionnalités suivantes :

- **Fonctions mathématiques** : Addition, soustraction, carré
- **Traitement de données** : Lecture et affichage de fichiers CSV avec Pandas
- **Tests paramétrés** : Validation exhaustive avec différents cas de test
- **Fixtures Pytest** : Tests isolés et reproductibles

## 👥 Contributeurs

- **Votre Nom** - Développeur principal - [@Roxiina](https://github.com/Roxiina)

Voir la liste complète des [contributeurs](https://github.com/Roxiina/Projet-1/contributors) ayant participé à ce projet.

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Consultez [CONTRIBUTING.md](.github/CONTRIBUTING.md) pour les guidelines
2. Lisez le [CODE_OF_CONDUCT.md](.github/CODE_OF_CONDUCT.md)
3. Créez une branche `feat/votre-fonctionnalite`
4. Soumettez une Pull Request

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🔗 Liens Utiles

- [Documentation complète](https://Roxiina.github.io/Projet-1/)
- [Rapport de bugs](https://github.com/Roxiina/Projet-1/issues)
- [Guide uv](https://github.com/astral-sh/uv)
- [Documentation Pytest](https://docs.pytest.org/)
- [Documentation Ruff](https://docs.astral.sh/ruff/)

## 📊 Statistiques

![GitHub issues](https://img.shields.io/github/issues/Roxiina/Projet-1)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Roxiina/Projet-1)
![GitHub stars](https://img.shields.io/github/stars/Roxiina/Projet-1?style=social)

---

**Note** : Remplacez `USERNAME` par votre nom d'utilisateur GitHub dans tous les liens.
