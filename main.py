
from argparse import ArgumentParser
from pathlib import Path
from commitly.commitly import Commitly, FORMAT_COMMIT, STYLE_COMMIT, RECOMMANDATION
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from logo import LOGO, VERSION

# Initialize argument parser
parser = ArgumentParser(description="Automatically generate a commit message based on the provided diff.")

parser.add_argument("--add", type=str, help="Add a file to the commit", nargs="+", default=".") # ! pour ignorer le git add
parser.add_argument("--format", type=str, help="Add a file of format commit")
parser.add_argument("--style", type=str, help="Add a file of style commit")
parser.add_argument("-r","--recommandation", type=str, help="Add a file of style commit")
parser.add_argument("-p", "--push", action="store_true", help="Push the commit to the remote repository")
parser.add_argument("-t", "--ticket", type=str, help="Add a ticket number to the commit message")

parser.add_argument("--show-format", action="store_true", help="Show the format commit")
parser.add_argument("--show-style", action="store_true", help="Show the style commit")
parser.add_argument("--show-recommandation", action="store_true", help="Show the recommandation commit")

parser.add_argument("--comfirm", action="store_true", help="Comfirm the message of the commit")
parser.add_argument("--path-file-temp", action="store_true", help="Show the path of the temporary file", default="commit.txt")
parser.add_argument("--del-temp", action="store_true", help="Delete the temporary file")
parser.add_argument("-c","--continue",dest="continues", action="store_true", help="Continue the commit")

options = parser.parse_args()

console = Console()

console.print(
    Panel.fit(
        console.render_str(LOGO),
        subtitle="version " + VERSION,
        border_style="bold black"
    ),
    justify="center"
)

if options.show_format or options.show_style or options.show_recommandation:
    if options.show_format:
        console.print(
            Panel.fit(
                console.render_str(FORMAT_COMMIT),
                title="Format commit"
            )
        )
    if options.show_style:
        console.print(
            Panel.fit(
                console.render_str(STYLE_COMMIT),
                title="Style commit"
            )
        )
    if options.show_recommandation:
        console.print(
            Panel.fit(
                console.render_str(RECOMMANDATION),
                title="Recommandation commit"
            )
        )
        
    exit()


# Check if the user provided a file to add to the commit
if options.add:
    
    commitly = Commitly(
        file_temp=options.path_file_temp
    )
    # Add the file to the commit
    add = ', '.join(options.add)
    
    cmd_status = commitly.add(add) if add != '!' else True
    
    if cmd_status:
        console.print("[green]✔️  File added to the commit.[/green]")
        
        if not options.continues:
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
            
            msg = commitly.generate_commit_message(
                style_commit=style_commit, 
                format_commit=format_commit,
                recommandation_commit=recommandation_commit,
                ticket=options.ticket
            )
        else :
            try:
                with open(commitly.file_temp, "r", encoding="utf-8") as f:
                    msg = f.read()
            except: 
                console.print(f"file {commitly.file_temp} not found.")
                exit()
        if msg:
            
            console.print("[green]✔️  Commit message generated.[/green]")
            console.print(
                Panel.fit(
                    console.render_str(msg),
                    title="Commit message"
                )
            )
            
            save = commitly.save_message_to_file(msg)
            if not save:
                console.print("[bold red]❌  Error saving commit message. [/bold red]")
                exit()
                
            if options.comfirm:
                c = Prompt.ask(
                    prompt="Comfirm the message of the commit ? ",
                    default="y", 
                    show_default=True,
                    show_choices=True,
                    choices=["y", "n"],
                )
                
                if c.lower() != "y":
                    if options.del_temp:
                        commitly.file_temp.unlink()
                    
                    if add != '!': commitly.unstage(add)
                    
                    console.print("[bold red]❌  Commit message not comfirmed. [/bold red]")
                    
                    exit()
                    
            
            commitly.commit()
            console.print("[green]✔️  Commit message committed.[/green]")
            
            
            if options.push: 
                commitly.push()
                console.print("[green]✔️  Commit message pushed.[/green]")
        else:
            console.print("[bold red]❌  Error generating commit message. [/bold red]")
        
    else:
        console.print("[bold red]❌  Error adding file to the commit. [/bold red]")
else:
    console.print("[bold red]❌  no file provided. [/bold red]")