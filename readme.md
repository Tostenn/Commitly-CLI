
# commitly-cli 🚀🤖

> _Plus jamais de "commit final" ou "modifs 2" dans tes logs Git._

**commitly-cli** est une interface en ligne de commande (CLI) stylée avec `Rich`, construite sur la bibliothèque [commitly](https://github.com/Tostenn/commitly), qui génère pour toi des messages de commit automatiques, clairs, contextuels… et même élégants.

---

## 🧠 Pourquoi commitly-cli ?

Tu tapes `git commit -m ""`, puis tu bloques.

😩 Tu penses : “Je mets quoi là-dedans ?”

Avec **commitly-cli**, laisse l'IA s’en charger ! Elle lit les modifications (`git diff --cached`), comprend ce que tu as fait, et te propose un message propre et structuré.

> Utilise-la comme ton copilote de commit ✈️

## 🧰 Prérequis

- Python 3.7+
- Git installé sur votre système

---

## 🧪 Installation

```bash
pip install commitly-cli  # bientôt disponible sur PyPI
```
Ou clone localement :

```bash
git clone https://github.com/Tostenn/commitly-cli.git
cd commitly-cli
python main.py --help
```

---

> Assure-toi aussi d'avoir installé [`commitly`](https://github.com/Tostenn/commitly) :
> ```bash
> pip install commitly
> ```

---

## ✨ Fonctionnalités principales

- Analyse automatique des changements (diffs)
- Messages de commit adaptés à ton style et format
- Ajout de numéros de tickets
- Option `--confirm` avec fichier modifiable `commit.txt`
- Intégration directe avec Git (`git add`, `git commit`, `git push`)
- Sorties stylées avec [rich](https://github.com/Textualize/rich)
- Et un joli logo, parce que pourquoi pas ? 😎

---

## 🛠️ Utilisation basique

```bash
commitly-cli --add . --comfirm
```

Cela :
- ajoute tous les fichiers au staging
- génère un message de commit via l’IA
- affiche le message généré
- crée un fichier `commit.txt` que tu peux modifier à la main si tu veux
- te demande de confirmer avant de faire le commit
### Avec un ticket0.0

```bash
python main.py --add . --comfirm --ticket #25
```
Ajoute automatiquement le ticket dans le message !

---

## 🧪 Exemple avancé

```bash
commitly-cli \
  --add fichier.py README.md \
  --style style.txt \
  --format format.txt \
  --recommandation conseils.txt \
  --ticket #42 \
  --push \
  --comfirm
```

👉 Ce que ça fait :
- Ajoute `fichier.py` et `README.md` à l’index
- Utilise tes fichiers de style/format/conseils pour guider l'IA
- Associe le commit au ticket `#42`
- Te propose un message et te laisse l’éditer dans `commit.txt`
- Envoie le commit sur le dépôt distant après confirmation


### Si tu veux peaufiner ton message
Quand tu utilises `--comfirm`, un fichier `commit.txt` est créé dans le dossier courant.
Tu peux l'éditer avant de confirmer. Ensuite, relance avec :
```bash
python main.py --continue
```

---

## 🔍 Options

| Argument | Description |
|----------|-------------|
| `--add` | Fichiers à ajouter (par défaut `.`) |
| `--format` | Fichier texte décrivant le format de commit souhaité |
| `--style` | Fichier texte décrivant le style d’écriture |
| `--recommandation` | Conseils personnalisés pour guider l’IA |
| `--ticket` | Numéro de ticket (ex: `#12`) |
| `-p` `--push` | Push automatique après le commit |
| `--comfirm` | Demande confirmation + possibilité de modifier le message dans `commit.txt` |
| `--continue` | Utilise le message présent dans `commit.txt` sans le régénérer |
| `--show-format` | Affiche le format par défaut |
| `--show-style` | Affiche le style par défaut |
| `--show-recommandation` | Affiche les recommandations par défaut |
| `--del-temp` | Supprime `commit.txt` après usage |

> 🤓 Petit hack : utilise `--add !` pour **ne pas faire de `git add` automatique**

---

## ✍️ Personnalisation

Tu peux adapter la génération à ton style de projet grâce aux fichiers :
- `style.txt` : pour un ton plus sérieux, technique, fun…
- `format.txt` : structure des messages (type, module, titre…)
- `conseils.txt` : notes ou contraintes supplémentaires

---

## 🧪 Cas d’usage quotidien

### 🧹 Un petit fix rapide

```bash
commitly-cli --add . --ticket "#123" --comfirm
```

> Ajoute tout, associe au ticket, te propose un message, tu confirmes. Boom 💥

---

### 🧱 Un gros chantier avec style

```bash
commitly-cli --add . \
  --style mon-style.txt \
  --format mon-format.txt \
  --recommandation mon-cadre.txt \
  --ticket "#88" \
  --push \
  --comfirm
```

> Tu veux une cohérence sur toute une base de commits ? Tu es servi 🍽️

---

## 🧠 Fun fact : l'outil s’est auto-amélioré ! 🤖

Tu veux une preuve que `commitly-cli` fonctionne ? Ce projet est littéralement **son propre terrain d’entraînement**.

🛠️ Au tout début, **les 2 premiers commits** ont été écrits à la main… à l’ancienne.  
Mais dès le **3ᵉ commit**, `commitly-cli` a pris le relais.

Et là… 💥  
Au lieu d’un beau message bien structuré, il a fièrement pondu ça :

```bash
git commit -m "```"
```

Oui, tu lis bien : **trois backticks comme message de commit**.  
Pourquoi ? Parce que dans les données d’exemple, on avait mis `"message de commit ici"`, et notre jeune padawan commitly l’a pris **au pied de la lettre** 🥲

Mais bon… c’était ses débuts ! Depuis, l’outil a appris, s’est amélioré, et maintenant il génère des messages de commit bien plus clairs, utiles, et même élégants.

💬 Tu veux voir son évolution ?  
> Va jeter un œil à l’historique Git du projet et observe comment `commitly-cli` est passé de 🐣 à 🧙‍♂️ :  
> [`git log`](https://github.com/Tostenn/commitly-cli/commits/main)

Et oui, aujourd’hui ce projet utilise `commitly-cli` **pour générer ses propres messages de commit**.  
C’est du **commit-inception**, et c’est beau 😎

---


## 🔮 À venir

🚧 Des features en préparation, accrochons-nous :

- ✨ **Scission intelligente de commits** : Si tu développes plusieurs fonctionnalités en même temps, le programme détectera les zones indépendantes dans le `diff` et te proposera **plusieurs messages** adaptés pour scinder ton commit en plusieurs commits plus petits.
- 📁 **Détection automatique des fichiers pertinents**
- 🧪 Intégration facile avec des hooks Git (`pre-commit`)
- 💡 Suggestions de tags ou de branches
- 🎨 Interface web minimale

---

## 🤝 Basé sur

Ce projet repose sur :

📦 [commitly](https://github.com/Tostenn/commitly) : une bibliothèque magique qui transforme ton `diff` en message clair grâce à l’IA. C’est le moteur, commitly-cli est juste le volant 🛞

---

## 💬 Conclusion

Utilise `commitly-cli`, et dis adieu à :

```bash
git commit -m "changement"
git commit -m "test encore"
git commit -m "fix"
```

Fais briller ton historique Git comme un pro 💎


---

## 🐛 Bugs ? Idées ?

Ouvre une [issue](https://github.com/Tostenn/commitly-cli/issues) ou contacte-moi directement.
Excellent 😄 ! Voici une section toute prête à intégrer au README, avec une **anecdote rigolote** et instructive sur l'évolution de l'outil, basée sur l’historique de commit du projet :
