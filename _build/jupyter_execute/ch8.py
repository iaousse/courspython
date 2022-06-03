#!/usr/bin/env python
# coding: utf-8

# # Les execptions
# 
# ## Dictionnaire (dictionnary)
# 
# Contrairment au objets construits que nous avons vu (`strings`, `lists`, `tuples`), les dictionnaires (`dictionnary`) sont utilisés pour stocker des valeurs de données dans des paires clé:valeur. Un dictionnaire est une collection ordonnée , modifiable et qui n'autorise pas les doublons (Depuis la version 3.7 de Python, les dictionnaires demeurent ordonnés. Dans les versions antérieures (Python 3.6 et moins), les dictionnaires ne sont pas ordonnés).
# 
# - Les dictionnaires sont écrits avec des accolades et ont des clés et des valeurs.  Pour creer un dictionnaire et l'affecter a une variable : 
# ```python
# var_dict = {cle_1: valeur_1, cle_2:valeur_2,...., cle_n:valeur_n}
# ```
# - Un dictionnaire vide est un dictionnaire qui contient 0 element ({} ou dict());
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


# les cles et les valeurs peuvent etre de n'importe quel types de donnees. Par exemple on peut creer le dictionnaire suivant:

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


# Contrairment aux chaines de caracteres et aux listes, pour acceder a une valeur dans un dictionnaire nous deveons utiliser les cles. Par exemple, si nous voulons acceder a la valeur associee a la cle `jeudi` dans `les_jours3`, la maniere de le faire est la suivante:

# In[8]:


print(les_jours3['jeudi'])


# Les dictionnaires ne peuvent pas avoir des cles dupliqee (les valeurs peuvent etre dupliquees). En effet, les valeurs en double écraseront les valeurs existantes. Illustrons ca avec l'exemple suivant:

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


# ## Operations sur les dictionnaires
# 
# Python possède un ensemble de méthodes intégrées que nous pouvons utiliser pour manipuler les dictionnaires:
# 
# | Methode       | Description                                                                                                 |
# |--------------|-------------------------------------------------------------------------------------------------------------|
# | clear()      | Supprime tous les éléments du dictionnaire                                                                |
# | copy()       | Renvoie une copie du dictionnaire                                                                            |
# | fromkeys()   | Renvoie un dictionnaire avec les clés et la valeur spécifiées                                                      |
# | get()        | Renvoie la valeur de la clé spécifiée                                                                      |
# | items()      | Renvoie une liste contenant un tuple pour chaque paire clé-valeur                                                   |
# | keys()       | Retourne une liste contenant les clés du dictionnaire                                                             |
# | pop()        | Supprime l'élément avec la clé spécifiée                                                                  |
# | popitem()    | Supprime la dernière paire clé-valeur insérée                                                                   |
# | setdefault() | Renvoie la valeur de la clé spécifiée. Si la clé n'existe pas : insérez la clé, avec la valeur spécifiée |
# | update()     | Met à jour le dictionnaire avec les paires clé-valeur spécifiées                                                   |
# | values()     | Renvoie une liste de toutes les valeurs du dictionnaire                                                         |

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


# La varaible `les_jours` contient 7 elements.

# Si l'on veut tester l'appartenece d'un element a une liste/tuple on utilise l'operateur `in`. L'expression est la suivante : `element in liste`. Cela nous renvoi `True` si `element`est dans `liste`, sinon `False`. On peut aussi ecrire `element not in liste` pour tester si l'element n'est pas dans `liste` (`True`) ou s'il est dans `liste` (`False`). Voici quelques exemples:

# In[15]:


les_jours


# In[21]:


les_jours.values()


# In[23]:


un_tuple = (1, 'bonjour', 4.5, True)

print(1 in un_tuple)

print(2 in un_tuple)

print('o' not in un_tuple)

print('x' not in un_tuple)


# ## Quelle est la difference entre listes et tuples?
# 
# Les listes et les tuples sont pareils dans la plupart des contextes. Cepandant, la difference primordiale entre les deux et que les listes sont des **objets mutables** (modifiables) alors que les tuples sont des **objets immuables** (ne sont pas modifiable). La question qui se pose est donc: qu'est-ce qu'un objet mutable et un objet immuable?
# Parmi les objet immuable en python, on trouve:
# - Les nombres entiers (int)
# - Les nombres décimaux (float)
# - Les chaînes de caractères (str)
# - Les booléens (bool)
# - Les tuples (tuple)
# La plus part des autres objets que vous allez confronter en python sont mutables.
# 
# Nous allons illustre ca dans les exemples suivant:
# 1. nous allons creer les variables suivantes:
# - `var_chaine = "bonjour tout le monde"`, 
# - `var_liste = [1, 2, True, 'bonjour']`,
# - `var_tuple = (1, 2, True, 'bonjour')`.
# 2. nous qllons essayer de changer (par exemple) le premier element de chaque variable (par un autre element).

# In[26]:


var_chaine = "bonjour tout le monde"
var_liste = [1, 2, True, 'bonjour']
var_tuple = (1, 2, True, 'bonjour')


# In[29]:


var_chaine[0] = 'B'
print(var_chaine)


# In[30]:


var_liste[0] = 3333
print(var_liste)


# In[31]:


var_tuple[0] = 3333
print(var_tuple)


# Les listes ont une taille variable, les tuples et les chaines de caracteres ont une taille fixe. Enfin, les listes ont plus de fonctionnalités que les tuples. Cependant, c'est le contexte qui nous force a utiliser les listes ou les tuples. Nous allons rencontrer plusieurs contextes ou on est amener a choisir l'un des deux types.

# ## quelques methodes utiles pour les listes et les tuples
# Dans cette sections nous allons voir qulques `methodes`  pour les liste et/ou les tuples (les methodes communes et les methodes propres aux listes seulement). Les deux methodes suivantes sont communes aux listes et au tuples:
# - count: cette methode est utlisee pour compter le nombre d'elements de la liste/tuple.
# - index: cette method est utilisee pour chercher une valeur spécifiée dans la liste/tuple et renvoie la position de l'endroit où il a été trouvé.

# In[53]:


var_liste = [1, 2, 2, True, 'bonjour', 2]
var_tuple = (1, 2, 2, True, 'bonjour', 2)

print(var_liste.count(2)) ## print(var_tuple.count(2))

print(var_tuple.index(2))  ## print(var_tuple.index(2))


# In[48]:


var_tuple.index(44) # var_tuple.index(44)


# In[57]:





# Les methodes decrites dans la table suivante sont appliquee au lites seulement:
# 
# 
# | Méthode    | Description                                                                  |
# |-----------|------------------------------------------------------------------------------|
# | append()  | Ajoute un élément en fin de liste                                       |
# | clear()   | Supprime tous les éléments de la liste                                       |
# | copy()    | Renvoie une copie de la liste                                                   |
# | count()   | Renvoie le nombre d'éléments avec la valeur spécifiée                      |
# | extend()  | Ajouter les éléments d'une liste, à la fin de la liste actuelle |
# | index()   | Renvoie l'indice du premier élément avec la valeur spécifiée              |
# | insert()  | Ajoute un élément à la position spécifiée                                   |
# | pop()     | Supprime l'élément à la position spécifiée                                |
# | remove()  | Supprime le premier élément avec la valeur spécifiée                              |
# | reverse() | Inverse l'ordre de la liste                                               |
# | sort()    | Trie la liste                                                               |

# In[ ]:





# ## sets
# 
# On a vu que les chaines de caracteres, les liste et tuples sont des sequences ordonnees d'elements
# 
# 
# 
