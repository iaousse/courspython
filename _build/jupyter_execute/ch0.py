#!/usr/bin/env python
# coding: utf-8

# Avant de commencer
# =======================
# 
# Le présent Chapitre contiendra :
# 
# - Liens utiles
# - Guide d'installation
# - interpréteur Python
# - IPython
# - Jupyter notebook
# - Google Colab
# 
# # Liens utile:
# 
# - [python.org](https://www.python.org/)
# - [telecharger python pour windows](https://www.python.org/downloads/windows/)
# - [telecharger python pour max os](https://www.python.org/downloads/macos/)
# 
# - [anaconda](https://www.anaconda.com/)
# - [telecharger anaconda pour windows](https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.exe)
# - [telecharger vscode](https://code.visualstudio.com/Download)
# - [atom](https://atom.io/)
# - [pycharm](https://www.jetbrains.com/pycharm/)
# - [Google colab](https://research.google.com/colaboratory/) (compte google necessaire)
# 
# # Guide d'installation:
# - [python](https://realpython.com/installing-python/)
# - [vscode](https://code.visualstudio.com/docs/setup/setup-overview)
# - [pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)
# - [atom](https://flight-manual.atom.io/getting-started/sections/installing-atom/)
# - [anaconda](https://docs.anaconda.com/anaconda/install/windows/)
# 
# # interpréteur Python
# 
# Apres l'installation de python sur machine, On peut utiliser l'interpréteur Python  de manière interactive. On tape `python` dans  le terminal et on y est. Ensuite, on peut directement lui fournir du code Python à exécuter et nous allons recevoir les résultats immédiatement. 
# 
# :::{figure-md} markdown-fig
# <img src="interpwindows.PNG" alt="interpwin" class="bg-primary mb-1" width="400px">
# 
# Lancer l'interpréteur Python dans le terminal windows
# :::
# 
# 
# Cette option est très utile si on souhaite tester rapidement des bouts de code ou pour l'apprentissage.
# En revanche, si on souhaite ecrire un programe relativemnt long, on devrait ecrire notre programme dans un editeur de text (simple comme notpad, vim, ... ou un editeur avance comme vscode, pycharm, atom, ....) et on enregistre le fichier sous un intetule qui se termine par l'extension `.py`. 
# 
# :::{figure-md} markdown-fig1
# <img src="scriptnote.PNG" alt="interpwin" class="bg-primary mb-1" width="400px">
# 
# Les etapes pour ecrire et executer un programme avec Notepad
# :::
# 
# 
# # IPython
# IPython est un terminal interactif plus develope qui propose des fonctionnalités telles que l'introspection, une syntaxe additionnelle, la complétion et un historique riche. IPython doit etre installe a l'aide de la commande `pip install ipython` (voir [ici](https://ipython.org/install.html) pour plus de details).
# 
# # Jupyter notebook
# Les `notebooks Jupyter` sont des cahiers électroniques dont on peut, a la fois, produire du texte, inserer des images, des formules mathématiques et du code informatique exécutable. Ils sont manipulables interactivement dans un navigateur web. Jupyter est developpe dans un premier temps pour les langages de programmation Julia, Python et R (d'où le nom Jupyter). actuellement les notebooks supportent près de 40 langages différents.
# 
# La cellule est l'élément de base d'un notebook Jupyter. Elle peut contenir du texte formaté au format Markdown ou du code informatique qui pourra être exécuté. Le present cours est ecrit avec `jupyterbook` et chaque chapitre est un `notebook jupyter`. Le present text est ecrit dans une cellule markdown. la cellue suivante une cellule code ( qui est par defaut l'interpreteur IPython).

# In[1]:


# la presente cellule est une cellule code, en dessous de la cellule s'affiche le resultat du code
print("Hello world!")
5+2


# Voir [ici](https://docs.jupyter.org/en/latest/) pour plus de detail sur le projet `jupyter`.
# # Google Colab
# 
# Etant un projet incontournable dans le domaine du `machine learning` et `l'intellegence artificielle`, Google propose une version cloud de `jupyter`: **Google Colab**  ou **Colaboratory**: il s'agit un service cloud, offert par Google qui est essentiellement destiné à la formation et à la recherche dans les domaines susmentionnes. Google Colab permet d'entraîner des modèles de Machine Learning directement dans le cloud. Ceci dit, nous n'avons besoin d'installer quoi que ce soit (python, anaconda, editeur,...) sur la machine, la seule chose requise est un navigateur. (voir la section liens utiles pour les personnes interssees).
