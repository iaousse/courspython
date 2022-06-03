#!/usr/bin/env python
# coding: utf-8

# # Manipulation des dictionnaires (dictionnaries) et ensembles (sets)
# 
# ## Dictionnaire (dictionnary)
# 
# Contrairement au objets construits que nous avons vu (`strings`, `lists`, `tuples`), les dictionnaires (`dictionnary`) sont utilisés pour stocker des valeurs de données dans des paires clé:valeur. Un dictionnaire est une collection ordonnée, modifiable et qui n'autorise pas les doublons (Depuis la version 3.7 de Python, les dictionnaires demeurent ordonnés. Dans les versions antérieures (Python 3.6 et moins), les dictionnaires ne sont pas ordonnés).
# 
# - Les dictionnaires sont écrits avec des accolades et ont des clés et des valeurs.  Pour créer un dictionnaire et l'affecter a une variable : 
# ```python
# var_dict = {cle_1: valeur_1, cle_2:valeur_2,...., cle_n:valeur_n}
# ```
# - Un dictionnaire vide est un dictionnaire qui contient 0 élément ({} ou dict());
# - Les dictionnaires sont **mutable**, on peut modifier leur contenu et leur taille.
# 

# In[3]:


# dictionnaire vide
var = {} # ou var = dict()
print(type(var))
les_jours = {1:"lundi", 2:"mardi", 3:"mercredi", 4:"jeudi", 5:"vendredi", 6:"samedi", 7:"dimanche"}
print(les_jours)


# In[4]:


les_jours2 = {}

les_jours2[1] = 'lundi'
les_jours2[2] = 'mardi'
les_jours2[3] = 'mercredi'
les_jours2[4] = 'jeudi'
les_jours2[5] = 'vendredi'
les_jours2[6] = 'samedi'
les_jours2[7] = 'dimanche'

print(les_jours2)


# Les clés et les valeurs peuvent être de n'importe quel type de données. Par exemple on peut créer le dictionnaire suivant :

# In[5]:


les_jours3 = {}

les_jours3['lundi'] = 1
les_jours3['mardi'] = 2
les_jours3['mercredi'] = 3
les_jours3['jeudi'] = 4
les_jours3['vendredi'] = 5
les_jours3['samedi'] = 6
les_jours3['dimanche'] = 7

print(les_jours3)


# Contrairement aux chaines de caractères et aux listes, pour accéder à une valeur dans un dictionnaire nous devons utiliser les clés. Par exemple, si nous voulons accéder a la valeur associée a la clé `jeudi` dans `les_jours3`, la manière de le faire est la suivante :

# In[8]:


print(les_jours3['jeudi'])


# Les dictionnaires ne peuvent pas avoir des clés dupliquées (les valeurs peuvent être dupliquées). En effet, les valeurs en double écraseront les valeurs existantes. Illustrons ça avec l'exemple suivant :

# In[10]:


les_jours4 = {}

les_jours4['lundi'] = 0
les_jours4['mardi'] = 1
les_jours4['mardi'] = 2
les_jours4['mercredi'] = 3
les_jours4['jeudi'] = 4
les_jours4['vendredi'] = 5
les_jours4['samedi'] = 6
les_jours4['dimanche'] = 7

print(les_jours4)


# In[11]:


les_jours5 = {}

les_jours5['lundi'] = 0
les_jours5['mardi'] = 0
les_jours5['mercredi'] = 0
les_jours5['jeudi'] = 5
les_jours5['vendredi'] = 0
les_jours5['samedi'] = 0
les_jours5['dimanche'] = 0

print(les_jours5)


# ## Opérations sur les dictionnaires
# 
# Python possède un ensemble de méthodes intégrées que nous pouvons utiliser pour manipuler les dictionnaires :
# 
# | Méthode       | Description                                                                                                 |
# |--------------|-------------------------------------------------------------------------------------------------------------|
# | `clear()`      | Supprime tous les éléments du dictionnaire                                                                |
# | `copy()`       | Renvoie une copie du dictionnaire                                                                            |
# | `fromkeys()`   | Renvoie un dictionnaire avec les clés et la valeur spécifiées                                                      |
# | `get()`        | Renvoie la valeur de la clé spécifiée                                                                      |
# | `items()`      | Renvoie une liste contenant un tuple pour chaque paire clé-valeur                                                   |
# | `keys()`       | Retourne une liste contenant les clés du dictionnaire                                                             |
# | `pop()`        | Supprime l'élément avec la clé spécifiée                                                                  |
# | `popitem()`    | Supprime la dernière paire clé-valeur insérée                                                                   |
# | `setdefault()` | Renvoie la valeur de la clé spécifiée. Si la clé n'existe pas : insérez la clé, avec la valeur spécifiée |
# | `update()`     | Met à jour le dictionnaire avec les paires clé-valeur spécifiées                                                   |
# | `values()`     | Renvoie une liste de toutes les valeurs du dictionnaire                                                         |
# 

# In[46]:


# clear
les_jours.clear()

print(les_jours)


# In[47]:


# copy
les_jours2_copie = les_jours2.copy()

print(les_jours2_copie)


# In[48]:


# fromkeys
# creer un dictionnaire avec des cles mais pas de valeurs (None)

cles = range(6)
dict_vide = dict.fromkeys(cles)
print(dict_vide)


# In[49]:


# fromkeys
# creer un dictionnaire avec des cles a la meme valeur
var = ['a', 'e', 'i', 'o', 'u', 'y']
valeur = 'voyelle'
dict_voyelles = dict.fromkeys(var, valeur)

print(dict_voyelles)


# In[50]:


# get
print(les_jours2.get(3))


# In[51]:


# items
print(les_jours2.items())


# In[54]:


# keys
print(les_jours2.keys())


# In[55]:


# values
print(les_jours2.values())


# In[56]:


# pop
les_jours2.pop(4)

print(les_jours2)


# In[58]:


# popitem 
# inserer une cles-valeur arbitraire
les_jours2['la dirniere cles ajoutee'] = 'La valeur associee a la derniere cles'

print(les_jours2)


# In[59]:


# popitem
les_jours2.popitem()

print(les_jours2)


# In[61]:


# setdefault()
# si la cles existe
print(les_jours2.setdefault(1, "LUNDI"))
# pusique la cles existe, la valeur ne va pas changer. Elle va etre affichee. Le dictionnaire ne va pas changer aussi.
print(les_jours2)


# In[62]:


# setdefault()
# si la cles existe
# puisque la cles 4 n'existe pas. La valeur 'mercredi' va etre affichee. Le dictionnaire va etre modifie aussi
print(les_jours2.setdefault(4, "mercredi"))
print(les_jours2)


# In[ ]:


# update
premier


# La fonction intégrée `len()` est aussi appliquable pour les dictionnaires. Si l'on désire déterminer le nombre d'elements:

# In[13]:


len(les_jours)


# La variable `les_jours` contient 7 éléments.

# ## Ensembles (sets)
# 
# On a vu que les chaines de caractères, les liste et tuples sont des séquences ordonnées d'éléments dans les éléments peuvent être dupliquée. Nous avons besoins (dans certaines situations) d’un type de données composite dont l'ordre n'est pas tenu en compte et les répétitions ne sont pas permises : il s'agit des ensembles (`sets`).
# 
# - Les ensembles sont utilisés pour stocker plusieurs éléments dans une seule variable. Un ensemble est une collection non ordonnée, non modifiable* et non indexée. Toutefois, il est à noter que malgré que les éléments de l'ensemble ne soient pas modifiables, on peut supprimer des éléments et en ajouter de nouveaux.
# 
# 
# - Les ensemble sont écrits avec des accolades (comme les dictionnaires) mais ils n’ont pas des clés et des valeurs (juste des éléments).  Pour créer un ensemble et l'affecter a une variable : 
# ```python
# var_set = {valeur_1, valeur_2,...., valeur_n}
# ```
# - Un ensemble vide est un ensemble qui contient 0 élément (`set()`);
# 

# In[2]:


ensemble = {"bonjour", False, False, 'bonjour', 1, 2, 3, True, 3, 3, 3}
print(ensemble)


# In[5]:


ensemble = set(("bonjour", False, False, 'bonjour', 1, 2, 3, True, 3, 3, 3))
print(ensemble)
print(type(ensemble))


# On peut déterminer la taille d'un ensemble avec `len()`:

# In[4]:


print(len(ensemble))


# On ne peut pas accéder aux éléments d'un ensemble en se référant à un index (le cas des chaines de caractères, liste et tuples) ou à une clé (le cas des dictionnaires). Toutefois, on peut parcourir les éléments de l'ensemble à l'aide d'une boucle `for()` ou demander si une valeur spécifiée est présente dans un ensemble à l'aide du mot-clé (l'opérateur) `in`.

# In[6]:


for x in ensemble:
  print(x)


# In[7]:


print( 3 in ensemble)
print(100 in ensemble)
print( 555 not in ensemble)
print(False not in ensemble)


# ## Opérations sur les ensembles
# 
# ### Ajouter des éléments
# Comment nous avons dit, une fois créé, on ne peut pas modifier les éléments d'un ensemble, mais on peut ajouter de nouveaux éléments. Pour ce faire, on utilise la méthode `add()`.
# 

# In[8]:


ensemble.add(100)
ensemble.add("rebonjour")

print(ensemble)


# On peut aussi ajouter les éléments d'un ensemble a un autre en utilisant la méthode `update()`.

# In[9]:


autre_ensemble = {True, 555, "Python"}
ensemble.update(autre_ensemble)

print(ensemble)


# ### Retirer des éléments
# Pour supprimer un élément d'un ensemble, on utilise la méthode `remove()` ou `discard()`.
# 

# In[10]:


ensemble.remove(True)

print(ensemble)


# In[14]:


ensemble.discard(555)

print(ensemble)


# Si l'élément n'existe pas, `remove()` va renvoyer une erreur alors que `discard()` ne va pas la renvoyer.

# In[16]:


ensemble.remove(1000)

print(ensemble)


# In[17]:


ensemble.discard(1000)

print(ensemble)


# On peut utiliser la méthode `pop()` pour supprimer le dernier élément, **Cependant, les ensembles ne sont pas ordonnés**. Donc lorsqu'on utilise la méthode `pop()`, on va pas savoir quel élément est supprimé.

# In[18]:


ensemble.pop()

print(ensemble)


# La méthode `copy()` permet de copier l'ensemble. La méthode `clear()` vide l'ensemble. Le mot-clé `del` supprimera complètement l'ensemble.

# In[21]:


ensemble2 = ensemble.copy()

print(ensemble)
print(ensemble2)


# In[22]:


ensemble.clear()

print(ensemble)


# In[24]:


del ensemble

print(ensemble)


# Les ensembles ont des opérations similaires au même concept en mathématiques. On peut faire la réunion, l'intersection, la différence, tester l'inclusion d'un ensemble dans un autre et ainsi de suite.
# Voici une table contenant les méthodes des ensembles (quelques-unes sont déjà vues).
# 
# | Méthode                        | Description                                                                    |
# |-------------------------------|--------------------------------------------------------------------------------|
# | `add()`                         | Ajoute un élément à l'ensemble                                                    |
# | `clear()`                       | Supprime tous les éléments de l'ensemble                                          |
# | `copy()`                        | Renvoie une copie de l'ensemble                                                      |
# | `difference()`                  | Renvoie un ensemble contenant la différence entre deux ou plusieurs ensembles               |
# | `difference_update()`           | Supprime les éléments de cet ensemble qui sont également inclus dans un autre ensemble spécifié |
# | `discard()`                     |Supprimer l'élément spécifié                                                      |
# | `intersection()`                | Renvoie un ensemble, c'est-à-dire l'intersection de deux autres ensembles                      |
# | `intersection_update()`         | Supprime les éléments de cet ensemble qui ne sont pas présents dans d'autres ensembles spécifiés |
# | `isdisjoint()`                  | Renvoie si deux ensembles ont une intersection ou non                            |
# | `issubset()`                    | Retourne si un autre ensemble contient cet ensemble ou non                           |
# | `issuperset()`                  | Retourne si cet ensemble contient un autre ensemble ou non                           |
# | `pop()`                         | Supprime un élément de l'ensemble                                                |
# | `remove()`                      | Supprime l'élément spécifié                                                  |
# | `symmetric_difference()`        | Renvoie un ensemble avec les différences symétriques de deux ensembles                       |
# | `symmetric_difference_update()` | insère les différences symétriques de cet ensemble et d'un autre                    |
# | `union()`                       | Renvoie un ensemble contenant l'union d'ensembles                                      |
# | `update()`                      | Mettre à jour l'ensemble avec l'union de cet ensemble et d'autres                           |
# 
