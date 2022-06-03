#!/usr/bin/env python
# coding: utf-8

# # Manipulation des listes et tuples
# 
# :::{admonition} Rappel sur les listes
# 
# Nous avons vu que :
# - En Python, une liste est créée en plaçant des éléments entre crochets `[]` , séparés par des virgules(`,`);
# - Les éléments de la liste peuvent d'être des objets différents,
# - Une liste vide est une list qui contient 0 élément (`[]` ou `list()`);
# - Pour créer une liste et l'affecter a une variable :
# 
# ```python
# une_liste = [1, 'bonjour', 4.5, True]
# ```
# 
# :::
# 
# :::{admonition} Tuples
# 
# Les tuples (ou encore uplets) sont des types construits. Tout comme les listes, les tuples sont une collection ordonnée d'éléments.
# - En Python, un tuple est créée en plaçant des éléments entre parentheses `()` , séparés par des virgules(`,`);
# - Un tuple vide est un tuple qui contient 0 élément (`()` ou `tuple()`);
# - Pour créer un tuple et l'affecter a une variable :
# 
# ```python
# un_tuple = (1, 'bonjour', 4.5, True)
# ```
# 
# :::
# 
# 

# ## Opérations sur les listes et les tuples
# 
# Tout comme les chaines de caractères, on peut réaliser quelques opérations sur les listes (tuples). Par exemple, pour concaténer deux listes (deux tuples), on utilise `+`(`liste1+liste2` ou `tuple1+tuple2`), pour répéter une liste (un tuple) n fois, on multiplie n par la liste/tuple (`n*liste` ou `n*tuple`).
# 

# In[17]:


une_liste = [1, 'bonjour', 4.5, True]
autre_liste = [2, 4.5, 'tout le monde', False]
print(une_liste+ autre_liste)
print(une_liste*4)


# In[18]:


un_tuple = (1, 'bonjour', 4.5, True)
autre_tuple = (2, 4.5, 'tout le monde', False)
print(un_tuple+ autre_tuple)
print(un_tuple*4)            


# Une listes/un tuples est une séquence d'objets quelconques. Chacun de ceux-ci occupe une place précise dans cette séquence. Pour extraire un élément spécifique d'une liste/tuple, on utilise `[]`. Voici quelques exemple en utilisant `une_liste = [1, 'bonjour', 4.5, True]`. Nous utilisons aussi les indices négatifs : -1 désignera le dernier caractère, -2 l'avant dernier, et ainsi de suite. Nous utilisons le `slicing` aussi de la même manière que les chaines.
# ```{warning}
# Tout comme le cas des `strings`, l'élément ayant premier indice est inclus. Cependant, **l'élément ayant le dernier indice n'est pas inclus !!**. Si l'on veut, par exemple les trois premiers éléments, on doit indiquer 0 et 4 entre `[]` (`[0:4]`).
# - Si l'on veut les `n` premiers éléments : `[:n+1]`
# - Si l'on veut les éléments a partir de l'indice `n` jusqu'a la fin de la liste : `[n:]`
# ```
# 

# In[10]:


une_liste = [1, 'bonjour', 4.5, True]
print(une_liste[0])
print(une_liste[1])

print(une_liste[-1])
print(une_liste[-2])

print(une_liste[0:0])
print(une_liste[1:3])

print(une_liste[:3])
print(une_liste[2:])

print(une_liste[:])


# In[19]:


un_tuple = (1, 'bonjour', 4.5, True)
print(un_tuple[0])
print(un_tuple[1])

print(un_tuple[-1])
print(un_tuple[-2])

print(un_tuple[0:0])
print(un_tuple[1:3])

print(un_tuple[:3])
print(un_tuple[2:])

print(un_tuple[:])


# La fonction intégrée `len()` est aussi applicable pour les listes et les tuples. Si l'on désire déterminer le nombre d’éléments :

# In[20]:


une_liste = [1, 'bonjour', 4.5, True]
un_tuple = (1, 'bonjour', 4.5, True)
print(len(une_liste))
print(len(un_tuple))


# Les deux variables `une_liste` et `un_tuple` contiennent 4 éléments.

# Si l'on veut tester l'appartenance d'un élément a une liste/tuple on utilise l'opérateur `in`. L'expression est la suivante : `element in liste`. Cela nous renvoi `True` si `element` est dans `liste`, sinon `False`. On peut aussi écrire `element not in liste` pour tester si l'élément n'est pas dans `liste` (`True`) ou s'il est dans `liste` (`False`). Voici quelques exemples :

# In[22]:


une_liste = [1, 'bonjour', 4.5, True]

print(1 in une_liste)

print(2 in une_liste)

print('o' not in une_liste)

print('x' not in une_liste)


# In[23]:


un_tuple = (1, 'bonjour', 4.5, True)

print(1 in un_tuple)

print(2 in un_tuple)

print('o' not in un_tuple)

print('x' not in un_tuple)


# ## Quelle est la différence entre listes et tuples ?
# 
# Les listes et les tuples sont pareils dans la plupart des contextes. Cependant, la différence primordiale entre les deux et que les listes sont des **objets mutables** (modifiables) alors que les tuples sont des **objets immuables** (ne sont pas modifiable). La question qui se pose est donc : qu'est-ce qu'un objet mutable et un objet immuable ?
# Parmi les objets immuables en python, on trouve :
# - Les nombres entiers (`int`)
# - Les nombres décimaux (`float`)
# - Les chaînes de caractères (`str`)
# - Les booléens (`bool`)
# - Les tuples (`tuple`)
# La plupart des autres objets que vous allez confronter en python sont mutables.
# 
# Nous allons illustre ça dans les exemples suivants :
# 1. nous allons créer les variables suivantes :
# - `var_chaine = "bonjour tout le monde"`, 
# - `var_liste = [1, 2, True, 'bonjour']`,
# - `var_tuple = (1, 2, True, 'bonjour')`.
# 2. nous allons essayer de changer (par exemple) le premier élément de chaque variable (par un autre élément).
# 

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


# Les listes ont une taille variable, les tuples et les chaines de caractères ont une taille fixe. Enfin, les listes ont plus de fonctionnalités que les tuples. Cependant, c'est le contexte qui nous force à utiliser les listes ou les tuples. Nous allons rencontrer plusieurs contextes ou on est amené a choisir l'un des deux types.

# ## Quelques méthodes utiles pour les listes et les tuples
# Dans cette section nous allons voir quelques `méthodes` pour les listes et/ou les tuples (les méthodes communes et les méthodes propres aux listes seulement). Les deux méthodes suivantes sont communes aux listes et au tuples :
# - `count` : cette méthode est utilisée pour compter le nombre d'éléments de la liste/tuple.
# - `index` : cette méthode est utilisée pour chercher une valeur spécifiée dans la liste/tuple et renvoie la position de l'endroit où il a été trouvé.
# 

# In[2]:


var_liste = [1, 2, 2, True, 'bonjour', 2]
var_tuple = (1, 2, 2, True, 'bonjour', 2)

print(var_liste.count(2)) ## print(var_tuple.count(2))

print(var_tuple.index(2))  ## print(var_tuple.index(2))


# In[3]:


print(var_tuple.index(44))


# Les méthodes décrites dans la table suivante sont appliquées au lites seulement :
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
# 

# In[40]:


liste_mois1 = ['Janvier', 'Février', 'Février', 'Avril', 'bonjour', 'Mai',  'Juin',  'Juillet',  'Août', 'Septembre',  'Octobre',  'Novembre']
print(liste_mois1)


# In[41]:


liste_mois1.append('Décembre')
print(liste_mois1)


# In[42]:


liste_mois2 = liste_mois1.copy()

print(liste_mois2)


# In[43]:


liste_mois1.clear()
print(liste_mois1)


# In[44]:


liste_mois2.count('Février')


# In[45]:


liste_mois2.index('Février')


# In[46]:


liste_mois2.index('Février', 2)


# In[47]:


liste_mois2.insert(2, 'Mars')
print(liste_mois2)


# In[48]:


liste_mois2.pop(3)
print(liste_mois2)


# In[49]:


liste_mois2.remove('bonjour')
print(liste_mois2)


# In[50]:


liste_mois2.reverse()
print(liste_mois2)


# In[51]:


liste_mois2.sort()
print(liste_mois2)


# ## Slicing
# Dans cette partie nous allons quelques techniques de `slicing` avec des exemples. Cette technique peut être appliquée sur toute séquence ordonnée (liste, tuples, chaine de caractères). Voici une illustration pour le cas d'une liste (la même logique pour toute séquence ordonnée) :
# 
# :::{figure-md} markdown-fig3
# <img src="slicing.PNG" alt="interpwin" class="bg-primary mb-1" width="400px">
# 
# La position des éléments dans une liste
# :::
# 
# - Tous les éléments `[:]` :
# 

# In[23]:


print(liste_mois2[:])


# - Obtenir tous les éléments après une position spécifique `[n:]` (n étant la position en comptant de gauche à droite en commençant par 0) ou `[-n:]` (n étant la position de droite à gauche en commençant par 1):

# In[28]:


print(liste_mois2[4:])
print(liste_mois2[-8:])


# - Obtenir tous les éléments avant une position spécifique `[:n]`(n étant la position en comptant de gauche à droite en commençant par 0) ou `[:-n]` (n étant la position de droite à gauche en commençant par 1):

# In[29]:


print(liste_mois2[:4])
print(liste_mois2[:-8])


# - Obtenir tous les éléments d'une position à une autre position `[m:n]` (m étant la position de départ et n la position finale (non inclus) en comptant de gauche à droite en commençant par 0) ou `[-m:-n]` (m étant la position de départ et n la position finale (non inclus) en comptant de droite à gauche en commençant par 1):

# In[30]:


print(liste_mois2[5:10])
print(liste_mois2[-7:-2])


# - Obtenir tous les éléments d'une position à une autre position à des intervalles spécifiés `[m:n:k]`:

# In[39]:


print(liste_mois2[2:10:2])
print(liste_mois2[9:3:-1])
print(liste_mois2[-3:-10:-1])
print(liste_mois2[-3:-10:-1])

