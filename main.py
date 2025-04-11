
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

from argparse import ArgumentParser
from pathlib import Path
from commitly import Commitly, FORMAT_COMMIT, STYLE_COMMIT, RECOMMANDATION


# Initialize argument parser
parser = ArgumentParser(description="Automatically generate a commit message based on the provided diff.")

parser.add_argument("--add", type=str, help="Add a file to the commit", nargs="+", default=".") # ! pour ignorer le git add
parser.add_argument("--format", type=str, help="Add a file of format commit")
parser.add_argument("--style", type=str, help="Add a file of style commit")
parser.add_argument("-r","--recommandation", type=str, help="Add a file of style commit")
parser.add_argument("-p", "--push", action="store_true", help="Push the commit to the remote repository")

parser.add_argument("--show-format", action="store_true", help="Show the format commit")
parser.add_argument("--show-style", action="store_true", help="Show the style commit")
parser.add_argument("--show-recommandation", action="store_true", help="Show the recommandation commit")


    

options = parser.parse_args()
# print(options)

if options.format:
    print(FORMAT_COMMIT)
if options.style:
    print(STYLE_COMMIT)
if options.recommandation:
    print(RECOMMANDATION)


# Check if the user provided a file to add to the commit
if options.add:
    
    commitly = Commitly()
    # Add the file to the commit
    add = ', '.join(options.add)
    
    cmd_status = commitly.add(add) if add != '!' else True
    
    if cmd_status:
        print("File added to the commit.")
        
        # Check if the user provided a commit format file
        format_commit = Path(options.format) if options.format else None
        style_commit = Path(options.style) if options.style else None
        recommandation_commit = Path(options.recommandation) if options.recommandation else None
        
        if style_commit and style_commit.exists():
            style_commit = style_commit.read_text().replace("ÿþ", "")
            
        if format_commit and format_commit.exists():
            format_commit = format_commit.read_text().replace("ÿþ", "")
            
        if recommandation_commit and recommandation_commit.exists():
            recommandation_commit = recommandation_commit.read_text().replace("ÿþ", "")
        
        msg = commitly.msg_commit(style_commit, format_commit, recommandation_commit)
        print(msg)
        
        if msg:
            commitly.save_msg_in_file(msg)
            
            commitly.commit()
            
            if options.push:
                commitly.cmds("git push")
        
    else:
        print("Error adding file to the commit.")
else:
    print("No file provided to add to the commit.")