# Marche à suivre:

- Vérifier que python est installé  sur votre système 
```bash
which python #ou 
which python3
```
## Créer un environnement virtuel 

```bash
python -m venv .venv
```

## Activer l'environnement virtuel
```bash
source .venv/bin/activate
```
### Installer FastAPI
```bash
pip install "fastapi[standard]"
```

### Lancer 

```bash 
fastapi dev main.py
```