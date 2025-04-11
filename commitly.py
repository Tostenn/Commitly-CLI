from g4f.client import Client
from g4f.models import gpt_4o_mini
from prompt import PROMPT, STYLE_COMMIT, FORMAT_COMMIT, RECOMMANDATION
from subprocess import run
from pathlib import Path

class Commitly:
    
    """
    automatically generate a commit message based on the provided diff
    """
    
    def __init__(self, model=gpt_4o_mini, file_temp="commit.txt"):
        self.client = Client()
        self.model = model
        self.file_temp = Path(file_temp)
    
    def get_value(self, style_commit:str=None, format_commit:str=None, recommandation_commit:str=None):
        if not style_commit:
            style_commit = STYLE_COMMIT
        if not format_commit:
            format_commit = FORMAT_COMMIT
        if not recommandation_commit:
            recommandation_commit = RECOMMANDATION
        
        return PROMPT.format(STYLE_COMMIT=style_commit, FORMAT_COMMIT=format_commit, RECOMMANDATION=recommandation_commit)
        pass
    
    def add(self, file:str)-> bool:
        cmd = self.cmds(f"""git add {file} """, True)
        return cmd == 0
    
    def msg_commit(self, style_commit:str=None, format_commit:str=None, recommandation_commit:str=None)-> str:
        
        cmd = self.cmds("git diff --cached")
        
        response = self.client.chat.completions.create(
        # model="gpt-4o-mini",
        model=self.model,
        messages=[
            {"role": "system", "content": self.get_value(style_commit, format_commit, recommandation_commit) },
            
            {"role": "user", "content": cmd}
        ],
        web_search=False
    )
        return response.choices[0].message.content
    
    def save_msg_in_file(self, message:str)-> bool:
        try:
            with open(self.file_temp, "w", encoding="utf-8") as f:
                f.write(message.replace('\x00', ''))
            return True
        except: return False
    
    def commit(self)-> bool:
        cmd = self.cmds(f"git commit -F {self.file_temp.absolute()}", True)
        self.file_temp.unlink() # supprimer le fichier
        return cmd == 0
    
    def cmds(self, cmd, code=False):
        '''exercuter des commande shell'''
        cmd = run(cmd,capture_output=True,text=True,shell=True)
        if code: return cmd.returncode
        return cmd.stdout.strip()
