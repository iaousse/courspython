#!/usr/bin/env python
# coding: utf-8

# # Essayez vous-meme!
# 
# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 1. 
# Soit la variable suivante `all_alphabet = "the quick brown fox jumps over the lazy dog"`. 
# - afficher les 10 premiers caracteres de cette vaiable (espaces comris)
# - afficher les 5 derniers caracters de cette variable (espaces compris)
# - Déterminez ce qui se passe lorsque l’un ou l’autre des indices de découpage est erroné, et décrivez cela le mieux possible. (Exemple: Si le second indice est plus petit que le premier, ou bien si le second indice est plus grand que la taille de la chaîne. Vous pouvez tester d'autres situations).

# In[12]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 2.
# Afficher la phrase suivantes `'bonjour tout le monde'` dans les trois figures suivantes (ajouter les caracters speciaux dans la chaines):
# - retour a lingne :
# 
# ```python
# bonjour
# tout
# le
# monde
# ```
# - tabulation :
# 
# ```python
# bonjour	tout	le	monde
# ```
# - tabulation et retour a la linge :
# 
# ```python
# bonjour
#     tout
#         le
#             monde
# ```

# In[4]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 3. 
# tester les methodes suivantes a l'aide d'une chaines de caracters contenant des lettres, des chiffres, et des symboles (exemple `'my_n@me%is$meth0s!'`): `.isalpha()` et `.isdigit()` (emple: qui sera l'output de cette instruction: `'my_n@me%is$meth0s!'[0].islpha()`? Faite ca avec d'autres elements de la chaines et affecter la a une variable avant de faire ces tests).
# 
# Compter toutes les lettres, chiffres et symboles spéciaux d'une chaîne donnée
# 
# Exemple:
# 
# Pour la chaine `'my_n@me%is$meth0s!'`:
# 
# Nombre total de caractères, chiffres et symboles
# 
# Caractères = 12
# 
# Chiffres = 1
# 
# Symbole = 5

# In[1]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 4. 
# donner plusieurs technique (slincing, boucle for, boucle while, ...)d'inverser une chaine de caractere (utiliser la chaine `bonjour`).

# In[35]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 5. 
# A l'aide de `'*'` et la boucle `for`, afficher les trois modèles suivants: 
# 
# 
# 
# ```
# *****
# *****
# *****
# *****
# *****
# ```
# 
# 
# 
# ```
# ******
# *****
# ****
# ***
# **
# *
# ```
# 
# 
# 
# ```
#      *
#     **
#    ***
#   ****
#  *****
# ******
# ```
# 

# In[7]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 6. 
# - Écrire un programme Python pour obtenir le plus petit nombre d'une liste (appliquer le programme sur la liste `ma_liste =[39, 35, 53, 21, 19, 33, 22]`. Comparer votre resulat avec `min(liste)`.
# - Écrire un programme Python pour obtenir le plus gand nombre d'une liste (appliquer le programme sur la liste `ma_liste =[39, 35, 53, 21, 19, 33, 22]`. Comparer votre resulat avec `max(liste)`.
# 
# - Écrire un programme Python qui permet a l'utilisateur d'entrer des nombre. Apres vous donner la somme, le max, le min, le produit, et la moyenne de ces nombres (ne pas utiliser les fonctions `sum(), min(),...`) et qui affiche l'ordre croissant et l'ordre decroissant (ne pas utilise des fonctions et methodes qui permettent que d'ordonner les nombres comme `sorted()` et `.sort()`) .
# - Refaire le meme programme en utilisant les fonctions qui vous convient (`sum(), min()`,`sorted()` ou `.sort()` etc.).

# In[45]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 7. 
# Executer le programme suivant:
# ```python
# var1 = [1, 4, 4, 3]
# var2 = var1
# print(var1)
# print(var2)
# var2[0] = 111
# print(var2)
# print(var1)
# ```
# Expliquer ce qui c'est passe (faite une petite recherche) et proposer une solution pour remidier a ce probleme.

# In[47]:


## votre code ici


# <hr style="border:2px solid gray"> </hr>
# 
# ## Exercice 8. 
# La table suivante contient les notes des étudiants d'une classe.
# 
# | apogee   | math | python | java | gestion | algorithmique |
# |----------|:----:|:------:|:----:|:-------:|:-------------:|
# | 19021549 |   -   |   14   |  13  |    9    |       15      |
# | 19021547 |  12  |   16   |  14  |    10   |       14      |
# | 19021563 |  11  |   15   |  12  |    10   |       15      |
# | 19021545 |  15  |   17   |  16  |    12   |       17      |
# | 19021553 |  14  |   15   |  14  |    12   |       16      |
# | 19021559 |  11  |   14   |  12  |    9    |         -      |
# | 19021557 |  13  |   15   |  14  |    12   |       12      |
# | 19021550 |   8  |   -     |  10  |    8    |       12      |
# | 19021548 |  10  |   14   |  11  |    8    |       13      |
# 
# - Créer 5 listes et les affecter aux variables `apogee`, `math`, `python`, `java`, `gestion`, `algorithmique` contenant les notes de chaque matière (penser à remplir les éléments manquants par un mot-clé qui montre que les valeurs sont vides).
# - créer les dictionnaires nommes `notes_math`, `notes_info`, et `notes_gestion`.
# - Créer un dictionnaire nomme `notes` contenant les notes des étudiants ;
# 
# Pour Les étudiants ayant des notes non saisies, la table suivante contient leurs notes :
# 
# | apogee   | math | python | java | gestion | algorithmique |
# |----------|:----:|:------:|:----:|:-------:|:-------------:|
# | 19021549 |   12   |   14   |  13  |    9    |       15      |
# | 19021559 |  11  |   14   |  12  |    9    |         12     |
# | 19021550 |   8  |   10    |  10  |    8    |       12      |
# 
# 
# - créer un autre dictionnaire vide nomme `note_actualisee`, puis remplir en utilisant les données de la table ci-dessus :
# - Actualiser les notes manquantes dans `notes` en utilisant `notes_actualisee`.
# 
# - L'étudiant ayant le code apogée `19021545` n'appartient pas a cette classe, supprimer le du dictionnaire `notes` ;
# - En utilisant une boucle, calculer :
#     - la note moyenne de la classe en math, et en python
#     - la note moyenne de chaque étudiant
# 
# 
# _NB: les codes apogées sont fictifs et toute ressemblance avec des étudiants existant ou ayant existé serait purement fortuite._
# 

# In[6]:


## votre code ici


# Les variables suivantes contiennent les nomes des quelques étudiants (des prénoms sélectionnés aléatoirement dans le monde entier), leur sexe et l'appartenance à l'une des trois classes : `classe_a`, `classe_b` et `classe_c`. Les classes ne sont pas mutuellement exclusives. Ceci dit, un étudiant peut être dans deux, voire trois, classe a la fois.
# 
# - 
# ```python
# hommes = {'Jakhi', 'Arjen', 'Davidmichael', 'Albert', 'Staton', 'Konstantinos', 'Rasheen', 'Thalamus', 'Gabryel', 'Ladavian', 
#          'Lendel', 'Sargon', 'Artadius', 'Tyer', 'Ignacio', 'Mckale', 'Jarvin', 'Raydrick', 
#          'Renn', 'Rony', 'Yasine'}
# ```
# 
# - 
# ```python
# femmes = {'Geryl', 'Khamyah', 'Comelia', 'Joneka', 'Teia', 'Sameria', 'Lourinda', 'Martrice', 'Bettianne', 'Blandy', 'Allynn', 
#           'Dashia', 'Neneh', 'Jovanka', 'Valeriana', 'Zhanasia', 'Naiyma', 'Kerrah', 'Ayaa', 'Johanna', 'Tawasha', 'Roxi', 
#           'Shaughnessy', 'Nyema', 'Janene', 'Diamyn', 'Carly', 'Giner', 'Efthymia'}
# ```
# 
# - 
# ```python
# classe_a = {'Geryl', 'Comelia', 'Joneka', 'Lendel', 'Artadius', 'Mckale','Teia', 'Martrice', 'Allynn', 'Neneh', 'Shaughnessy', 'Diamyn', 'Jakhi', 'Davidmichael', 
#             'Thalamus', 'Ladavian', 'Renn'}
# ```
# - 
# ```python
# classe_b = {'Geryl', 'Comelia', 'Joneka', 'Teia', 'Martrice', 'Allynn','Lourinda', 'Bettianne', 'Blandy', 'Jovanka', 'Kerrah', 'Johanna', 'Tawasha', 'Roxi', 'Janene', 'Giner', 'Efthymia', 
#             'Staton', 'Konstantinos', 'Rasheen', 'Sargon', 'Tyer', 'Ignacio', 'Jarvin', 'Yasine'}
# ```
# 
# - 
# ```python
# classe_c = {'Geryl', 'Comelia', 'Joneka', 'Teia', 'Martrice', 'Allynn','Khamyah', 'Sameria', 'Dashia', 'Valeriana', 'Zhanasia', 'Naiyma', 'Ayaa', 'Nyema', 'Carly', 'Arjen', 'Albert', 'Gabryel', 
#              'Lendel', 'Artadius', 'Mckale', 'Raydrick', 'Rony', 'Rasheen', 'Sargon', 'Tyer', 'Ignacio', 'Jarvin', 'Yasine'}
# ```
# - Copier les ensembles ci-dessus dans la cellule code (ou dans votre éditeur que vous utilisez).
# - Créer un ensemble `etudiant` contenant tous les étudiants.
# - A quelle(s) classe(s) `Yassin` appartient-il ?
# - Quelles sont les étudiants de sexe masculin qui appartiennent à la classe `classe_a` ? 
# - Quelles sont les étudiants de sexe féminin qui appartiennent à la classe `classe_c` ?
# - Quelles sont les étudiants de sexe masculin qui appartiennent à la classe `classe_a` et la classe `classe_c` ?
# - Quelles sont les étudiants de sexe féminin qui appartiennent a la classe `classe_b` et n'appartiennent pas à la classe `classe_c` ?
# - L'étudiant `Mohamed` appartient à la classe la classe `classe_b`. Ajouter le aux ensembles adéquats.
# - Utiliser une boucle pour afficher pour chaque étudiantes le message suivant :
#      - Si l'étudiante appartient à la classe `classe_c` : ` L'étudiante 'nom' appartient à la classe classe_c`.
#      - Si l'étudiante n'appartient à la classe `classe_c` : ` L'étudiante 'nom' n'appartient pas à la classe classe_c`.
# 

# In[14]:


## votre code ici


# 
