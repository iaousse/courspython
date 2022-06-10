#!/usr/bin/env python
# coding: utf-8

# # Les modules
# 
# ## Définition
# Les modules sont des programmes Python qui contiennent des fonctions qui peuvent être réutilisées souvent. Les modules sont aussi dits bibliothèques ou librairies. Les modules peuvent être considérés comme des **boîtes à outils** qui vont être très utiles.
# 
# La communauté des développeurs de Python a réalisé plusieurs (PLUSIEURS !) modules qui effectuent beaucoup (BEAUCOUP !) de tâches. Pour cette raison, lors de la réalisation d'un programme on doit s'assurer qu'il n'existe pas déjà sous forme de module !
# 
# La plupart de ces modules sont déjà installés dans les versions standards de Python. [Voici](https://docs.python.org/fr/3/py-modindex.html) une documentation sur les modules python.
# 

# ## Importation de modules
# Nous pouvons importer un module qui existe déjà dans notre machine (installé ou crée par nous-même) via plusieurs manières.
# 
# Nous allons les illustrer avec l'exemple suivant : 
# - le nombre $\pi =3.14...$ n'existe pas dans python,

# In[1]:


print(pi)


# - Cependant, il existe un module appelé `math` qui contient ce nombre $\pi$: `pi`. D'ailleurs, le module math contient plusieurs fonctionnalités liées aux mathématiques. Voici plusieurs techniques pour utiliser les fonction (généralement les objets) d'un module (importation):

# In[2]:


# importer le module
import math
# utiliser le point après le nom du module puis l'objet que l'on veut dans ce module
print(math.pi)


# In[3]:


# importer le module sous un nom que l'on veut et l'utiliser dans le reste du programme
import math as m
print(m.pi)


# In[4]:


# importer un objet spécifique depuis le module. On ne va pas utiliser le point (comme math.pi)
from math import pi
print(pi)


# In[5]:


# importer un objet spécifique depuis le module sous un nom 
# que l'on veut et l'utiliser dans le reste du programme
from math import pi as le_nombre_pi
print(le_nombre_pi)


# In[6]:


# importer plusieurs objets depuis le module
from math import pi, sqrt # sqrt est un fonction dans math qui calcul la racine carrée d'un nombre
print(sqrt(pi))


# Finalement, on peut aussi faire :
# ```python
# # importer tous les éléments du module avec *
# from math import *
# print(pi)
# ```
# Mais il est déconseillé d'utiliser cette méthode pour ne pas avoir des chevauchement avec des objets dans un autre module.

# Il existe une panoplie de modules que nous serons souvent amenés à utiliser en programmant en Python. Un échantillon est le suivant :
# 
# - `math` : plusieurs fonctions et constantes mathématiques de base (`sin`, `cos`, `exp`, $\pi$...).
# - `sys` : interaction avec l'interpréteur Python.
# - `os` : interaction avec le système d'exploitation.
# - `random` : simulation et génération de nombres aléatoires.
# - `numpy`: plusieurs fonctions mathématiques complètes, des générateurs de nombres aléatoires, veteurs, matrices, algèbre linéaire,...
# - `matplotlib`: un module pour la visualisation des données.
# - `time` : accès à l'heure de l'ordinateur et aux fonctions gérant le temps.
# - `urllib` : récupération de données sur internet depuis Python.
# - `re` : manipulation des expressions régulières.

# ## Création d'un module
# 
# En Python, la création d'un module est simple. Il suffit d'écrire un ensemble de fonctions (et/ou de constantes) dans un fichier, puis d'enregistrer ce dernier avec une extension `.py`  Et voilà! Nous allons illustrer ça avec L'exemple suivant :
# - nous allons créer un module simple que nous enregistrerons sous le nom `mon_module.py`
# 
# - le fichier `mon_module.py` contient le code suivant :
# ```python
# """L module suivant contient des fonctions pour 
# addition, multiplication, soustraction et 
# Une chaine de caractères"""
# message = "bonjour tout le monde"
# pi = 3.14
# def addition(x, y):
#     """Cette fonction fait permet de 
#     claculer la somme de deux nombres"""
#     return x+y  
# def multip(x, y):
#     """Cette fonction fait permet de 
#     claculer la multiplication de deux nombres"""
#     return x*y
# def soustra(x,y):
#     """Cette fonction fait permet de 
#     claculer la soustraction de deux nombres"""
#     return x-y
# ```

# Pour importer ce fichier, nous allons utiliser `import`:

# In[7]:


import mon_module


# Nous pouvons maintenant utiliser toute les fonctions et constantes dans ce module. Pour savoir les composante de ce module, on peut utiliser la fonction `help()`.
# 
# _NB: Les chaînes de caractères entre triple guillemets `""" """` en tête du module et en tête de chaque fonction sont facultatives mais elles jouent néanmoins un rôle essentiel dans la documentation du code.

# In[8]:


print(help(mon_module))


# Les chaines de caractères susmentionné sont dites `docstrings` (chaînes de documentation). Ces `docstrings` (comme nous nous avons vu dans `help(mon_module)`) permettent notamment de fournir de l'aide lorsqu'on invoque la commande `help()`.
# Pour utiliser une fonction dans le module `mon_module`, on procède comme dans le cas des modules qui existent déjà dans python (comme `math` que nous avons vu). Supposons que nous voulons utiliser les fonctions `addtion`, `multip`, et `soustra` qui existe dans `code1` pour les valeurs 5 et 10 et nous voulons utiliser la constante `pi ` :
# 

# In[9]:


print(mon_module.addition(5, 10))
print(mon_module.multip(5, 10))
print(mon_module.soustra(5, 10))
print(mon_module.pi)


# ## Bonnes pratiques en programmation Python
# Les bonnes pratiques en programmation Python sont résumées dans un module qui s'appelle `this`. Nous allons l'importer.

# In[10]:


import this

