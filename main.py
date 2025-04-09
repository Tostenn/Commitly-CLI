
"""
creer un outil qui genere des message de commit adapter 
a la structure de ton projet

les commandes git qui me seront utile :
    git add <file> | pour ajouter un fichier au commit
    git commit -m "<message>" | pour faire un commit avec un message
    git push | pour envoyer les commits sur le serveur distant

commandes :
    main.py --add <file>
        --commit-style <path_file (txt)> | pour ajouter de recommendations a l'ia
        --commit-format <path_file (txt)> | pour ajouter de recommendations a l'ia
        --push | pour envoyer les commits sur le serveur distant
        --help | pour afficher l'aide
        
"""

from prompt import PROMPT, STYLE_COMMIT, FORMAT_COMMIT
from argparse import ArgumentParser


# Initialize argument parser
parser = ArgumentParser(description="Automatically generate a requirements.txt file for your project.")
parser.add_argument("--add", type=str, help="Add a file to the commit")
parser.add_argument("--commit-format", type=str, help="Add a file of format commit")
parser.add_argument("--commit-style", type=str, help="Add a file of style commit")
parser.add_argument("--push", action="store_true", help="Push the commit to the remote repository")
parser.add_argument("--help", action="store_true", help="Display the help message")