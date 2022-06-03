#!/usr/bin/env python
# coding: utf-8

# # Les chaînes de caractères (strings)
# 
# :::{admonition} Rappel
# 
# Nous avons vu que :
# - Une chaîne est une liste ordonnée de caractères ;
# - un caractère est tout ce que vous pouvez taper sur le clavier en une seule frappe,
# Comme une lettre (a, b, c, ...), un chiffre (0, 1, 3, ...), symboles (@, %, #,...), espace ou une backslash (\);
# - une chaîne vide est une chaîne qui contient 0 caractères ('') ;
# - Python reconnaît comme chaînes tout ce qui est délimité par des guillemets
# (" " ou alors ' ') ;
# - pour affecter une chaîne de caractères a une variable :
# 
# ```python
# var = "bonjour"
# ```
# 
# :::
# 

# Maintenant, nous Nous allons voir quelques caractères spéciaux
# 
# Sous Python, la backslash `"\"` est un caractère spécial, également appelé caractère `d'échappement`. Il est utilisé pour représenter certains caractères d'espacement : "\t" est une tabulation, "\n" est une nouvelle ligne et "\r" est un retour chariot. Supposons que nous voulons afficher cette chaine `"\nous\tenons à vous remercier"`.

# In[1]:


print("\nous\tenons à vous remercier")


# Python ne comprend que `'\n'` dons `"\nous\tenons à vous remercier"` est un retour à linge. La même chose pour `'\t'` : c’est une tabulation (nous allons voir en détails caractère dits `caractères spéciaux`). Pour lui informer que nous ne voulons pas ça, on doit ajouter `\` avant `\` dans les deux cas (c'est-à-dire `\\`). Voilà comment le faire :

# In[2]:


print("\\nous\\tenons à vous remercier")


# Aussi, lorsque nous voulons afficher une chaine de caractères comme `'c'est magnifique'`

# In[19]:


print('c'est magnifique')


# Python comprend que la deuxième apostrophe termine la chaine de caractères. Donc le reste de la chaine (`est magnifique`) n'est pas compris. Nous devons mettre `\` avant la deuxième apostrophe pour elle soit un caractère de cette chaine :

# In[20]:


print('c\'est magnifique')


# La même chose pour une chaine content `"` et déclarée par `" "` (comme `""bonjour""`).

# In[21]:


print(""bonjour"")


# In[22]:


print("\"bonjour\"")


# ```{note}
# On peut utiliser `"c'est magnifique"` ou `'"bonjour"'` sans utiliser `\` (entrer la chaine avec apostrophe s'elle contient des guillemets ou l'inverse).
# ```

# In[23]:


print("c'est magnifique")
print('"bonjour"')


# Voici une quelques des caractères spéciaux et leurs significations :
# - `\n` - Nouvelle ligne
# - `\t` - tabulation
# - `\r` - Retour chariot
# - `\b` - Retour en arrière
# - `\f` - Saut de page
# - `\'` - Apostrophe
# - `\"` - Guillemets
# - `\\` -Backslash

# In[65]:


print('Bon\njour', end='\n----\n')
print('Bon\tjour', end='\n----\n')
print('Bon\rjour', end='\n----\n')
print('Bon\bjour', end='\n----\n')
print('Bon\fjour', end='\n----\n')


# ## Opérations sur les chaînes de caractères
# 
# On peut réaliser quelques opérations sur les chaînes de caractères. Par exemple, pour concaténer deux chaînes de caractères on utilise `+`(`chaine1+chaine2`), pour répéter une chaîne de caractère n fois on multiplie n par la chaine (`n*chaine`).

# In[72]:


var1 = 'hello'
var2 = "world"
print(var1+var2)
print(var1+' '+var2)
print(5*var1)
print(4*(var1 + " "+ 2*var2))


# Si l'on désire déterminer le nombre de caractères présents dans une chaîne, on utilise la fonction intégrée `len()` :

# In[73]:


var = "bonjour tout le monde"
print(len(var))


# La variable `var` contient une chaine de 21 caractères (3 espace comptés).

# Les chaînes sont des séquences de caractères. Chacun de ceux-ci occupe une place précise dans cette séquence. Sous Python, les éléments d'une séquence sont toujours indicés (ou numérotés) de la même manière, c'est-à-dire à partir de zéro (python commence toujours avec 0 comme premier indice). Pour extraire un caractère spécifique (ou plusieurs caractères) on utilise `[]`. Voici quelques exemples en utilisant `var = "bonjour tout le monde"`.

# In[76]:


var = "bonjour tout le monde"

print(var[0])

print(var[1])

print(var[2])

print(var[3])

print(var[20])


# Dans certaines situations, Il est utile de pouvoir désigner l'emplacement d'un caractère par rapport à la fin de la chaîne.
# Pour cela, nous utilisons des indices négatifs : -1 désignera le dernier caractère, -2 l'avant dernier, et ainsi de suite.

# In[78]:



var = "bonjour tout le monde"

print(var[-1])

print(var[-2])

print(var[-3])

print(var[-21])


# Il arrive souvent que l'on souhaite extraire une sous-séquence de caractères d'une chaîne. Sous Python, on utilise une technique dite `slicing` (). La technique consiste à indiquer entre crochets `[]` les indices correspondant au début et à la fin de la sous-séquence que l'on souhaite extraire.
# ```{warning}
# Le caractère ayant premier indice est inclus. Cependant, **le caractère ayant le dernier indice n'est pas inclus !!**. Si l'on veut, par exemple les trois premiers caractères, on doit indiquer 0 et 4 entre `[]` (`[0:4]`).
# - Si l'on veut les `n` premier caractères : `[:n+1]`
# - Si l'on veut tous les caractères à partir de l'indice `n` jusqu'à la fin de la chaine : `[n:]`
# ```
# Illustrons ça avec un exemple :

# In[82]:



var = "bonjour tout le monde"

print(var[0:0])
print(var[2:5])
print(var[0:3])

print(var[:3])

print(var[5:21])

print(var[5:])

print(var[:])


# Si l'on veut tester l'appartenance d'un caractère à une chaine on utilise l'opérateur `in`. L'expression est la suivante : `caractere in chaine`. Cela nous renvoi `True` si `caractere` est dans `chaine`, sinon `False`. On peut aussi écrire `caractere not in chaine` pour tester si `caractere` n'est pas dans `chaine` (`True`) ou s'il est dans `chaine` (`False`). Voici quelques exemples :

# In[86]:


var = "bonjour tout le monde"

print('b' in var)

print('z' in var)

print('o' not in var)

print('x' not in var)


# ## Méthodes utiles pour les chaines des caractères
# Dans cette section nous allons voir quelques `méthodes` pour les chaines des caractères (lorsque nous allons étudier la programmation orientée objet, nous allons comprendre la signification de ce terme. Pour l'instant nous allons accepter que `method` signifie une fonction dont l'expression générale est `chaine.method(args)` ou `args` sont des arguments qui peuvent être obligatoires ou facultatifs selon la méthode).
# - split: cette méthode est utilisée pour nous rendre une liste dont les éléments sont les caractères de la chaine: `chaine.split(sep)`.  On peut choisir le caractère séparateur `sep` en le fournissant comme argument, sinon c'est un espace par défaut.

# In[102]:


var = "bonjour tout le monde"

splitted_var = var.split()
print(var)
print(splitted_var)
print(type(splitted_var))

var2 = "un, deux, trois, cinq-six, sept"
print(var2.split())
print(var2.split(','))
print(var2.split('-'))


# - count: lorsque elle est appliquée a un chaine de caractères avec un argument qui est aussi une chaine de caractères (éventuellement un seul caractère), elle renvoi le nombre d'occurrences la dernière chaine dans la première chaines. ` chaine1.count(chaine2)`.

# In[106]:


var = "bonjour tout le monde"
print(var.count("b"))

print(var.count("on"))

print(var.count(" "))


# - find, index : Lorsque l'une de ces méthodes est appliquée a une chaine de caractère avec un argument qui est aussi une chaine de caractères (éventuellement un seul caractère), elle renvoi l'indice de la chaine cherchée dans la première chaines (l'indice de la première occurrence). `find` renvoi -1 si la chaine cherchée n'existe pas alors que index revoit une erreur dans la même situation. ` chaine1.find(chaine2)` et ` chaine1.index(chaine2)`.

# In[143]:


var = "bonjour tout le monde"
print(var.find('b'))
print(var.find('e'))
print(var.find('tout'))
print(var.find('x'))


# In[144]:


var = "bonjour tout le monde"
print(var.index('b'))
print(var.index('e'))
print(var.index('tout'))
print(var.index('x'))


# - lower, upper, title, capitalize, swapcase: Lorsque l'une de ces méthodes est appliquée a une chaine de caractère, elle la convertit on minuscule (`lower`), majuscule (`upper`), majuscule a l'initial de chaque mot (`title`), majuscule a l'initial du premier mot (`capitalize`), et les majuscules en minuscules, et vice-versa (`swapecase`).

# In[138]:


var1 = "bonjour tout le monde"
var2 = "Bonjour tout le monde"
var3 = "BONJOUR tout le monde"

print(var1.upper())
print(var1.title())
print(var1.capitalize())
print(var3.lower())
print(var1.swapcase())


# - strip: enlève les espaces (s'ils existent) au début et à la fin de la chaîne.

# In[140]:


var1 = "bonjour tout le monde"
var2 = "   Bonjour tout le monde   "

print(var1.strip())
print(var2.strip())


# - replace : remplace une chaine de caractères (éventuellement un seul caractère) par une autre chaine de caractère.

# In[142]:


var = "bonjour tout le monde"
print(var.replace('b', 'B'))

print(var.replace('bonjour', 'bonsoir'))


# ## Formatage des chaînes de caractères
# ### Ancienne version
# Les chaines de caractères en python sont riches en termes de fonctionnalité (vous allez, au fur et mesure, découvrir des nouvelles méthodes et technique avancées). Dans cette section, nous allons présenter une autre technique de traitement très puissante, que l’on appelle formatage des chaînes. 
# 
# Les chaînes de caractères ont une opération intégrée unique accessible avec l'opérateur `%`. Cela vous permet d'effectuer très facilement un formatage simple (formatting). Si vous avez déjà travaillé avec une fonction de style `printf` en `C`, vous reconnaîtrez immédiatement comment cela fonctionne. Voici un exemple simple :

# In[3]:


langage = "Python"
print('%s est le meilleur langage de programmation'%langage)


# Cette technique n'est propre à `print` mais plutôt au chaines de caractères.

# In[4]:


langage = "Python"
message = '%s est le meilleur language de programmation'

print(message%langage)


# In[5]:


langage = "Python"
message = '%s est le meilleur language de programmation'%langage

print(message)


# %s, %d, %f .....

# In[20]:


langage ='Python'

version = 3.6

print('%s %s %d %f %g' % (langage, version, version, version, version))


# ### Nouvelle version 
# Python 3 a introduit une nouvelle façon de formater les chaînes. Ce formatage de chaîne n'utilise pas l'opérateur `%`. Le formatage est maintenant realise en appelant la methode `.format()` sur une chaîne de caracteres.

# In[11]:


langage = "Python"
print('{} est le meilleur langage de programmation'.format(langage))


# In[6]:


langage = "Python"
message = '{} est le meilleur language de programmation'

print(message.format(langage))


# In[7]:


langage = "Python"
message = '{} est le meilleur language de programmation'.format(langage)

print(message)


# ### f-Strings (Python 3.6+)
# Python 3.6 a ajouté une nouvelle approche de formatage de chaîne appelée `f-strings`. 

# In[12]:


langage = "Python"
print(f'{langage} est le meilleur langage de programmation')


# In[10]:


langage = "Python"
message = f'{langage} est le meilleur language de programmation'

print(message)

