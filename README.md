<div align="center">

# 🎯 Projet 1 : Python Template Professionnel

### **Template moderne pour projets Python et IA avec fondations solides**

[![CI Status](https://github.com/Roxiina/Projet-1/actions/workflows/ci.yml/badge.svg)](https://github.com/Roxiina/Projet-1/actions/workflows/ci.yml)
[![Documentation Status](https://github.com/Roxiina/Projet-1/actions/workflows/docs.yml/badge.svg)](https://Roxiina.github.io/Projet-1/)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://docs.astral.sh/ruff/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen.svg)](https://github.com/Roxiina/Projet-1)

[Documentation](https://Roxiina.github.io/Projet-1/) •
[Installation](#-installation-rapide) •
[Fonctionnalités](#-fonctionnalités) •
[Contribution](.github/CONTRIBUTING.md) •
[Changelog](docs/source/changelog.rst)

</div>

---

## 📖 Table des Matières

- [À propos](#-à-propos)
- [Pourquoi ce projet](#-pourquoi-ce-projet)
- [Installation rapide](#-installation-rapide)
- [Fonctionnalités](#-fonctionnalités)
- [Utilisation](#-utilisation)
- [Docker](#-docker)
- [Structure du projet](#-structure-du-projet)
- [Développement](#-développement)
- [Tests](#-tests)
- [Documentation](#-documentation)
- [Contribution](#-contribution)
- [Roadmap](#-roadmap)
- [Support](#-support)
- [Licence](#-licence)
- [Remerciements](#-remerciements)

---

## 🎯 À propos

**Projet 1** est un template de référence pour le développement d'applications Python professionnelles et de projets d'Intelligence Artificielle. Il implémente les meilleures pratiques de l'industrie et fournit une base solide avec tous les outils modernes pré-configurés.

### ✨ Points forts

| Catégorie | Technologies | Description |
|-----------|-------------|-------------|
| **📦 Gestion de dépendances** | [`uv`](https://github.com/astral-sh/uv) | Gestionnaire ultra-rapide (10-100x plus rapide que pip) |
| **🎨 Qualité de code** | [`Ruff`](https://docs.astral.sh/ruff/) | Linter et formatter moderne, remplace Flake8 + Black + isort |
| **🧪 Tests** | [`Pytest`](https://docs.pytest.org/) + [`pytest-cov`](https://pytest-cov.readthedocs.io/) | Suite de tests complète avec 97% de couverture |
| **📚 Documentation** | [`Sphinx`](https://www.sphinx-doc.org/) + [`Furo`](https://pradyunsg.me/furo/) | Documentation interactive et moderne |
| **🐳 Conteneurisation** | [`Docker`](https://www.docker.com/) | Images optimisées avec multi-stage builds |
| **⚙️ CI/CD** | [`GitHub Actions`](https://github.com/features/actions) | Pipeline complet automatisé |

---

## 💡 Pourquoi ce projet

### 🚀 Démarrage instantané

Passer de zéro à un environnement de développement complet en **moins de 2 minutes**. Plus besoin de configurer manuellement chaque outil.

### 🏆 Meilleures pratiques intégrées

- ✅ Structure de projet standardisée et scalable
- ✅ Configuration centralisée (`pyproject.toml`)
- ✅ Pre-commit hooks pour la qualité du code
- ✅ Tests automatisés avec couverture élevée
- ✅ Documentation auto-générée depuis les docstrings
- ✅ Déploiement reproductible (Docker + uv.lock)

### 🎓 Valeur pédagogique

Idéal pour apprendre et enseigner les pratiques de développement professionnel Python. Chaque composant est documenté et expliqué.

---

## ⚡ Installation rapide

### Prérequis

- **Python 3.11+** - [Télécharger Python](https://www.python.org/downloads/)
- **uv** - [Guide d'installation](https://github.com/astral-sh/uv#installation)
- **Git** - [Télécharger Git](https://git-scm.com/)

### Installation en 3 commandes

```bash
# 1. Cloner le repository
git clone https://github.com/Roxiina/Projet-1.git
cd Projet-1

# 2. Installer les dépendances
uv sync

# 3. Lancer l'application
uv run python app/main.py
```

<details>
<summary>📦 <strong>Installer uv</strong> (si non installé)</summary>

**Linux/macOS**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**Alternative (via pip)**
```bash
pip install uv
```

</details>

---

## 🎨 Fonctionnalités

### 🔢 Modules implémentés

```python
from app.modules.mon_module import add, sub, square, print_data

# Opérations mathématiques avec type hints
result = add(10.5, 5.5)  # 16.0
squared = square(4)       # 16

# Traitement de données avec Pandas
import pandas as pd
df = pd.read_csv('app/moncsv.csv')
row_count = print_data(df)  # Affiche et retourne le nombre de lignes
```

### 📊 Exemple de sortie

```bash
=== Démonstration des Fonctions Mathématiques ===
Addition: 10 + 2 = 12
Addition: 20 + 2 = 22
Soustraction: 10 - 2 = 8
Carré: 4^2 = 16

=== Traitement des Données CSV ===
       nom  age      ville  score
0    Alice   25      Paris     85
1      Bob   30       Lyon     92
2  Charlie   35  Marseille     78
3    Diana   28   Toulouse     88
4      Eve   32       Nice     95

Nombre de lignes dans le DataFrame: 5
```

### 🧪 Tests et Qualité

| Métrique | Valeur | Statut |
|----------|--------|--------|
| **Couverture de code** | 97% | ✅ Excellent |
| **Tests unitaires** | 20/20 passés | ✅ Tous validés |
| **Linting (Ruff)** | 0 erreur | ✅ Conforme |
| **Formatage** | 100% | ✅ Normalisé |

---

## 🎯 Utilisation

### Exécution de l'application

```bash
# Méthode 1 : Avec uv (recommandé)
uv run python app/main.py

# Méthode 2 : Avec environnement virtuel activé
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
python app/main.py
```

### Qualité du code

```bash
# Vérifier le code
uv run ruff check .

# Formater automatiquement
uv run ruff format .

# Vérifier et corriger
uv run ruff check . --fix
```

---

## 🐳 Docker

### Build et exécution

```bash
# Construire l'image
docker build -t projet1:latest .

# Lancer le conteneur
docker run --rm projet1:latest
```

### Image optimisée

- 🐧 Base : `python:3.11-slim`
- 📦 Taille : ~200 MB
- ⚡ Build time : ~25 secondes
- 🔒 `.dockerignore` configuré pour exclure les fichiers inutiles

---

---

## 📂 Structure du projet

```plaintext
Projet-1/
├── 📁 .github/
│   ├── workflows/
│   │   ├── ci.yml                    # Pipeline de test et qualité
│   │   └── docs.yml                  # Déploiement documentation
│   ├── CONTRIBUTING.md               # Guide de contribution
│   └── CODE_OF_CONDUCT.md            # Code de conduite
│
├── 📁 app/                           # Code source principal
│   ├── modules/
│   │   ├── __init__.py
│   │   └── mon_module.py             # Logique métier (add, sub, square, print_data)
│   ├── __init__.py
│   ├── main.py                       # Point d'entrée de l'application
│   └── moncsv.csv                    # Données d'exemple
│
├── 📁 tests/                         # Suite de tests
│   ├── __init__.py
│   ├── test_math_csv.py              # Tests paramétrés (18 tests)
│   └── test_main.py                  # Tests d'intégration (2 tests)
│
├── 📁 docs/                          # Documentation Sphinx
│   ├── source/
│   │   ├── conf.py                   # Configuration Sphinx + Furo
│   │   ├── index.rst                 # Page d'accueil moderne
│   │   ├── installation.rst          # Guide d'installation
│   │   ├── usage.rst                 # Guide d'utilisation
│   │   └── api/                      # Documentation API auto-générée
│   └── build/                        # Documentation HTML compilée
│
├── 📄 pyproject.toml                 # Configuration centralisée (deps, ruff, pytest)
├── 📄 uv.lock                        # Verrouillage des dépendances
├── 📄 Dockerfile                     # Image Docker optimisée
├── 📄 .dockerignore                  # Exclusions Docker
├── 📄 .gitignore                     # Exclusions Git
├── 📄 LICENSE                        # Licence MIT
└── 📄 README.md                      # Ce fichier
```

---

## 🔧 Développement

### Configuration de l'environnement de développement

```bash
# Installation complète (dépendances de dev incluses)
uv sync

# Vérifier l'installation
uv run pytest
uv run ruff check .
```

### Workflow de développement recommandé

1. **Créer une branche** : `git checkout -b feat/ma-fonctionnalite`
2. **Développer** : Écrire du code avec docstrings Google format
3. **Tester** : `uv run pytest` (couverture > 80%)
4. **Vérifier** : `uv run ruff check . --fix`
5. **Commiter** : Messages conventionnels (feat:, fix:, docs:, etc.)
6. **Pusher** : `git push origin feat/ma-fonctionnalite`
7. **Pull Request** : Créer une PR vers `main`

### Standards de code

- **Docstrings** : Format Google (obligatoire pour toutes les fonctions publiques)
- **Type hints** : Obligatoires pour tous les paramètres et retours
- **Line length** : 88 caractères (Ruff)
- **Import order** : isort via Ruff
- **Formatage** : Automatique avec `ruff format`

---

## 🧪 Tests

### Exécuter les tests

```bash
# Tous les tests
uv run pytest

# Avec couverture détaillée
uv run pytest --cov=app --cov-report=html
# Ouvrir htmlcov/index.html pour le rapport visuel

# Verbose + affichage des logs
uv run pytest -v -s

# Un fichier spécifique
uv run pytest tests/test_math_csv.py

# Une fonction spécifique
uv run pytest tests/test_math_csv.py::test_add
```

### Structure des tests

```python
# tests/test_math_csv.py - Exemple de test parametré
import pytest
from app.modules.mon_module import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, 1, 0),
    (0.5, 0.5, 1.0),
])
def test_add(a, b, expected):
    """Test de la fonction add avec différentes valeurs."""
    assert add(a, b) == expected
```

---

## 📚 Documentation

### Documentation en ligne

🌐 **[Lire la documentation complète](https://Roxiina.github.io/Projet-1/)**

La documentation est automatiquement déployée sur GitHub Pages à chaque push sur `main`.

### Générer localement

```bash
cd docs
uv run sphinx-build -b html source build
```

**Linux/macOS** : `open build/html/index.html`  
**Windows** : `start build/html/index.html`

### Fonctionnalités de la documentation

- ✨ Design moderne avec thème Furo
- 🌙 Mode sombre/clair
- 📱 Responsive (mobile-friendly)
- 🔍 Recherche en texte intégral
- 📋 Boutons "Copier" sur les blocs de code
- 🎨 Grilles, cards, et onglets interactifs
- 🔗 Liens GitHub dans le footer

---

## 🤝 Contribution

Les contributions sont **chaleureusement accueillies** ! 🎉

### Comment contribuer

1. 📖 Lisez le [Guide de Contribution](.github/CONTRIBUTING.md)
2. 📜 Respectez le [Code de Conduite](.github/CODE_OF_CONDUCT.md)
3. 🍴 Forkez le projet
4. 🌿 Créez votre branche : `git checkout -b feat/amazing-feature`
5. ✍️ Commitez vos changements : `git commit -m 'feat: add amazing feature'`
6. 📤 Poussez vers la branche : `git push origin feat/amazing-feature`
7. 🎯 Ouvrez une Pull Request

### Types de contributions acceptées

- 🐛 Correction de bugs
- ✨ Nouvelles fonctionnalités
- 📝 Amélioration de la documentation
- 🎨 Améliorations UX/UI
- 🧪 Ajout de tests
- 🔧 Optimisations de performance

---

## 🗺️ Roadmap

### ✅ Version 0.1.0 (Actuelle)

- [x] Structure de projet complète
- [x] Tests avec 97% de couverture
- [x] Documentation Sphinx moderne
- [x] CI/CD GitHub Actions
- [x] Docker optimisé

### 🚀 Version 0.2.0 (À venir)

- [ ] Pre-commit hooks automatiques
- [ ] Support Python 3.12+
- [ ] Intégration avec Poetry (optionnelle)
- [ ] Badges de couverture dynamiques
- [ ] Templates de PR/Issues GitHub

### 🔮 Version 1.0.0 (Future)

- [ ] CLI avec Typer ou Click
- [ ] API REST avec FastAPI
- [ ] Déploiement Heroku/Azure/AWS
- [ ] Monitoring avec Prometheus
- [ ] Internationalisation (i18n)

---

## 💬 Support

### 🐛 Rapporter un bug

Ouvrez une [issue](https://github.com/Roxiina/Projet-1/issues/new) avec :
- Description détaillée du problème
- Étapes pour reproduire
- Comportement attendu vs obtenu
- Environnement (OS, Python version, etc.)

### 💡 Proposer une fonctionnalité

Ouvrez une [discussion](https://github.com/Roxiina/Projet-1/discussions) ou une issue avec le tag `enhancement`.

### 📧 Contact

- **Développeur principal** : [@Roxiina](https://github.com/Roxiina)
- **Email** : via GitHub
- **Issues** : [GitHub Issues](https://github.com/Roxiina/Projet-1/issues)

---

## 📄 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2025 Roxiina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Remerciements

Un grand merci à :

- 🌟 **[uv](https://github.com/astral-sh/uv)** – Gestionnaire de dépendances ultra-rapide
- 🔍 **[Ruff](https://github.com/astral-sh/ruff)** – Linter et formateur Python blazing fast
- 🧪 **[Pytest](https://pytest.org)** – Framework de test élégant et puissant
- 📚 **[Sphinx](https://www.sphinx-doc.org)** – Générateur de documentation de référence
- 🎨 **[Furo](https://pradyunsg.me/furo/)** – Thème Sphinx moderne et élégant
- 🐋 **[Docker](https://www.docker.com)** – Conteneurisation standardisée
- 🚀 **[GitHub Actions](https://github.com/features/actions)** – CI/CD intégré
- 📊 **[Pandas](https://pandas.pydata.org)** – Bibliothèque de manipulation de données
- 🔢 **[NumPy](https://numpy.org)** – Calcul numérique de haute performance

### Inspirations

Ce projet s'inspire des meilleures pratiques de projets open-source reconnus :

- [numpy](https://github.com/numpy/numpy) – Structure de documentation et tests
- [diun](https://github.com/crazy-max/diun) – Design du README et badges
- [FastAPI](https://github.com/tiangolo/fastapi) – Standards de qualité de code
- [pytest](https://github.com/pytest-dev/pytest) – Approche de testing modulaire

---

<div align="center">

**⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !**

[![GitHub stars](https://img.shields.io/github/stars/Roxiina/Projet-1?style=social)](https://github.com/Roxiina/Projet-1/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Roxiina/Projet-1?style=social)](https://github.com/Roxiina/Projet-1/network/members)

**Fait avec ❤️ par [Roxiina](https://github.com/Roxiina)**

</div>


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

