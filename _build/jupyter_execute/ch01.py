#!/usr/bin/env python
# coding: utf-8

# # Interpréteur Python, IPython, et notebooks
# 
# ## Interpréteur Python
# 
# Apres l'installation de python sur machine, On peut utiliser l'interpréteur Python de manière interactive. On tape `python` dans le terminal et on y est. Ensuite, on peut directement lui fournir du code Python à exécuter et nous allons recevoir les résultats immédiatement. 
# 
# :::{figure-md} markdown-fig
# <img src="interpwindows.PNG" alt="interpwin" class="bg-primary mb-1" width="400px">
# 
# Lancer l'interpréteur Python dans le terminal Windows
# :::
# 
# 
# Cette option est très utile si on souhaite tester rapidement des bouts de code ou pour l'apprentissage.
# En revanche, si on souhaite écrire un programme relativement long, on devrait écrire notre programme dans un éditeur de texte (simple comme Notepad, vim, ... ou un éditeur avance comme vscode, pycharm, atom, ....) et on enregistre le fichier sous un intitulé qui se termine par l'extension `.py`. 
# 
# :::{figure-md} markdown-fig1
# <img src="scriptnote.PNG" alt="interpwin" class="bg-primary mb-1" width="400px">
# 
# Les étapes pour écrire et exécuter un programme avec Notepad
# :::
# 
# 
# ## IPython
# IPython est un terminal interactif plus développé qui propose des fonctionnalités telles que l'introspection, une syntaxe additionnelle, la complétion et un historique riche. IPython doit être installe à l'aide de la commande `pip install ipython` (voir [ici](https://ipython.org/install.html) pour plus de détails).
# 
# ## Jupyter notebook
# Les `notebooks Jupyter` sont des cahiers électroniques dont on peut, à la fois, produire du texte, insérer des images, des formules mathématiques et du code informatique exécutable. Ils sont manipulables interactivement dans un navigateur web. Jupyter a été développé dans un premier temps pour les langages de programmation Julia, Python et R (d'où le nom Jupyter). Actuellement les notebooks supportent près de 40 langages différents.
# 
# La cellule est l'élément de base d'un notebook Jupyter. Elle peut contenir du texte formaté au format Markdown ou du code informatique qui pourra être exécuté. Le présent cours est écrit avec `jupyterbook` et chaque chapitre est un `notebook Jupyter`. Le présent texte est écrit dans une cellule Markdown. La cellule suivante une cellule code (qui est par défaut l'interpréteur IPython).

# In[1]:


# La présente cellule est une cellule code, en dessous de la cellule s'affiche le résultat du code
print("Hello world!")
5+2


# Voir [ici](https://docs.jupyter.org/en/latest/) pour plus de détails sur le projet `Jupyter`.
# ## Google Colab
# 
# Etant un projet incontournable dans le domaine du `machine learning` et `l'intelligence artificielle`, Google propose une version cloud de `Jupyter`: **Google Colab**  ou **Colaboratory**: il s'agit un service cloud, offert par Google qui est essentiellement destiné à la formation et à la recherche dans les domaines susmentionnés. Google Colab permet d'entraîner des modèles de Machine Learning directement dans le cloud. Ceci dit, nous n'avons besoin d'installer quoi que ce soit (python, anaconda, éditeur...) sur la machine, la seule chose requise est un navigateur. (Voir la section liens utiles pour les personnes intéressées).
