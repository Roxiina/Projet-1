# Utilisation d'une image Python légère basée sur Python 3.11
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances en premier pour optimiser le cache Docker
COPY pyproject.toml uv.lock ./

# Installer uv pour gérer les dépendances
RUN pip install --no-cache-dir uv

# Installer les dépendances du projet
RUN uv sync --frozen --no-dev

# Copier le code source de l'application
COPY app/ ./app/

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Exposer un port (si nécessaire pour des applications web futures)
# EXPOSE 8000

# Commande par défaut pour exécuter l'application
CMD ["uv", "run", "python", "app/main.py"]
