
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

from prompt import PROMPT, STYLE_COMMIT, FORMAT_COMMIT, RECOMMANDATION
from argparse import ArgumentParser
from pathlib import Path
from repertoire import cmds
from g4f.client import Client
from g4f import models
from time import time


# Initialize argument parser
parser = ArgumentParser(description="Automatically generate a commit message based on the provided diff.")

parser.add_argument("--add", type=str, help="Add a file to the commit", nargs="+", default=".") # ! pour ignorer le git add
parser.add_argument("--format", type=str, help="Add a file of format commit")
parser.add_argument("--style", type=str, help="Add a file of style commit")
parser.add_argument("-r","--recommandation", type=str, help="Add a file of style commit")
parser.add_argument("-p", "--push", action="store_true", help="Push the commit to the remote repository")

parser.add_argument("--show-format", action="store_true", help="Show the format commit")
parser.add_argument("--show-style", action="store_true", help="Show the style commit")

client = Client()
model = models.gemini_1_5_flash

def msg_commit(style_commit, format_commit, recommandation_commit):
    
    cmd = cmds("git diff --cached")
    response = client.chat.completions.create(
    # model="gpt-4o-mini",
    model=model,
    messages=[
        {"role": "system", "content": PROMPT.format(STYLE_COMMIT=style_commit, FORMAT_COMMIT=format_commit, RECOMMANDATION=recommandation_commit) },
        
        {"role": "user", "content": cmd}
    ],
    web_search=False
)
    
    commit = response.choices[0].message.content
    print('--------------------')
    print(commit)
    print('--------------------')
    
    if commit:
        cmd = cmds(f"""git commit -m "{commit}" """, True)
        if cmd == 0:
            print("Commit created.")
            if options.push:
                cmd = cmds("git push")
                if cmd == 0:
                    print("Commit pushed to remote repository.")
                else:
                    print("Error pushing commit to remote repository.")
        else:
            print("Error creating commit.")
    
    

options = parser.parse_args()
# print(options)

if options.format:
    print(FORMAT_COMMIT)
if options.style:
    print(STYLE_COMMIT)

# Check if the user provided a file to add to the commit
if options.add:
    # Add the file to the commit
    add = ', '.join(options.add)
    cmd = cmds("git add " + add, True) if add != '!' else 0
    
    if cmd == 0:
        print("File added to the commit.")
        # Check if the user provided a commit format file
        path_format = Path(options.format) if options.format else None
        path_style = Path(options.style) if options.style else None
        path_recommandation = Path(options.recommandation) if options.recommandation else None
        
        if path_style and path_style.exists():
            style_commit = path_style.read_text().replace("ÿþ", "")
        else:
            style_commit = STYLE_COMMIT
            
        if path_format and path_format.exists():
            format_commit = path_format.read_text().replace("ÿþ", "")
        else:
            format_commit = FORMAT_COMMIT
            
        if path_recommandation and path_recommandation.exists():
            recommandation_commit = path_recommandation.read_text().replace("ÿþ", "")
        else:
            recommandation_commit = RECOMMANDATION
        
        msg_commit(style_commit, format_commit, recommandation_commit)
    else:
        print("Error adding file to the commit.")
else:
    print("No file provided to add to the commit.")