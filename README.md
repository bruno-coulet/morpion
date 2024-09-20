# Jeu de Morpion

**Virtual environnement**
```bash
python -m venv .venv
```
> .venv is the name of the virtual environnement 

**Connect to the venv** 

- mac/linux
`source .venv/bin/activate.fish`
- windows
`.venv/Scripts/activate` or `.venv/Scripts/activate.ps1` 

**create requirements.txt from pip**
`pip freeze > requirements.txt`

in a new environnement install the librairies
**install librairies**
`pip install -r requirements.txt`

**quit venv**
`deactivate` 

## Mode d'emploi

1. Lancer le fichier play_game.py
2. Entrer les coordonnée dans le terminal : deux entiers de 1 à 3 séparés par un espace, puis valider avec la touche <entrée>
3. Répeter l'opération numéro 2 pour l'autre joueur jusqu'à la fin du jeu.
