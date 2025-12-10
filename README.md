# Mini-Projet : Analyse exploratoire du catalogue Netflix

Analyse exploratoire du catalogue Netflix avec un dataset de 8 807 titres.

## Installation

Le projet utilise UV pour gérer les dépendances.

```bash
# Pour installer les dépendances
source .venv/bin/activate
uv pip install -r pyproject.toml
```

## Utilisation

### Notebook Jupyter

Ouvrir le fichier `main.ipynb` dans Jupyter ou directement dans VS Code.

### Application Streamlit

Application déployée : https://lapoulepunto-netflix-eda-analyse-app-obtr78.streamlit.app/

Pour lancer localement :

```bash
streamlit run app.py
```

## Fichiers

- `main.ipynb` : Notebook principal avec toutes les analyses
- `app.py` : Application Streamlit interactive
- `netflix_titles.csv` : Dataset Netflix
- `pyproject.toml` : Dépendances du projet
