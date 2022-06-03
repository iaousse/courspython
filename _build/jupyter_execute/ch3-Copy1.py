#!/usr/bin/env python
# coding: utf-8

# Point sur les chaînes de caractères, les listes, les tuples et les dictionnaires: 
# ===========
# 
# ## Manupilation des chaînes de caractères (strings)
# 
# ```{admonition} Rappel
# Nous avons vu que:
# - Une chaîne est une liste ordonnee de caractères;
# - Un caractère est tout ce que vous pouvez taper sur le clavier en une seule frappe,
# comme une lettre (a, b, c, ...), un chiffre (0, 1, 3, ...), symboles (@, %, #,...), espace ou une backslash (\);
# - Une chaîne vide est une chaîne qui contient 0 caractères ('');
# - Python reconnaît comme chaînes tout ce qui est délimité par des guillemets
# (" " ou alors ' ').
# - Pour affecter une chaîne de caractères a une variable:
# ```python
# var = "bonjour"
# ```
# ```

# Maintenat nous Nous allons voir quelques caracteres speciaux
# 
# Sous Python, la backslash `"\"` est un caractère spécial, également appelé caractère `d'échappement`. Il est utilisé pour représenter certains caractères d'espacement : "\t" est une tabulation, "\n" est une nouvelle ligne et "\r" est un retour chariot. Supposons que nous voulons afficher cette chaine `"\nous\tenons a vous remericer"`.

# In[17]:


print("\nous\tenons a vous remericer")


# Python ne comprend que `'\n'` dons `"\nous\tenons a vous remericer"` est un retour a linge. La meme chose pour `'\t'` est une tabulation (nous allons voir en details caractère dits `caractères speciaux`). Pour lui informer que nous ne voulons pas ca, on doit ajouter `\` avant `\` dans les deux cas (c'est-a-dire `\\`). Voila comment le faire:

# In[18]:


print("\\nous\\tenons a vous remericer")


# Aussi, lorsque nous voulons afficher une chaine de caracteres comme `'c'est magnifique'`

# In[19]:


print('c'est magnifique')


# Python comprend que la deuxiem apostrophe termine la chaine de caractere donc le reste de la chaine (`est magnifique`) n'est pas compris. Nous devons mettre `\` avant la deuxieme apostrophe pour elle soit un caractere de cette chaine:

# In[20]:


print('c\'est magnifique')


# La meme chose pour une chaine content `"` est declaree par `" "` (comme `""bonjour""`).

# In[21]:


print(""bonjour"")


# In[22]:


print("\"bonjour\"")


# ```{note}
# On peut utiliser `"c'est magnifique"` ou `'"bonjour"'` sans utiliser `\` (entrer la chaine avec apostrophe s'elle contien des gueimmet ou l'invers).
# ```

# In[23]:


print("c'est magnifique")
print('"bonjour"')


# Voici une qulques des caracteres speciaux et leurs significations:
# - `\n` - Nouvelle ligne
# - `\t` - tabulation
# - `\r` - Retour chariot
# - `\b` - Retour en arrière
# - `\f` - Saut de page
# - `\'` - Apostrophe
# - `\"` - Guiellmets
# - `\\` -Backslash

# In[65]:


print('Bon\njour', end='\n----\n')
print('Bon\tjour', end='\n----\n')
print('Bon\rjour', end='\n----\n')
print('Bon\bjour', end='\n----\n')
print('Bon\fjour', end='\n----\n')


# ### operations sur les chaînes de caractères
# 
# On peut realiser quelques orperations sur les chaînes de caractères. Par exemple, pour concatiner deux chaînes de caractères on utilise `+`(`chaine1+chaine2`), pour repeter une chaîne de caractère n fois on multiplie n par la chaine (`n*chaine`).

# In[72]:


var1 = 'hello'
var2 = "world"
print(var1+var2)
print(var1+' '+var2)
print(5*var1)
print(4*(var1 + " "+ 2*var2))


# Si l'on désire déterminer le nombre de caractères présents dans une chaîne, on utilise la fonction
# intégrée `len()` :

# In[73]:


var = "bonjour tout le monde"
print(len(var))


# La varaible `var` contient une chaine de  21 caracteres (3 espace comptés).

# Les chaînes sont des séquences de caractères. Chacun de ceux-ci occupe une place précise dans cette séquence. Sous Python, les éléments d'une séquence sont toujours indicés (ou numérotés) de la même manière, c'est-à-dire à partir de zéro (python commence toujours avec 0 comme premier indice). Pour extraire un caractère specifique (ou plusieurs caractères) on utilise `[]`. Voici quelques exemple en utilisant `var = "bonjour tout le monde"`.

# In[76]:


var = "bonjour tout le monde"

print(var[0])

print(var[1])

print(var[2])

print(var[3])

print(var[20])


# Dans certaines situations, Il est utile de pouvoir désigner l'emplacement d'un caractère par rapport à la fin de la chaîne.
# Pour cela, nous utilisons des indices négatifs: -1 désignera le dernier caractère, -2 l'avant dernier, et ainsi de suite.

# In[78]:



var = "bonjour tout le monde"

print(var[-1])

print(var[-2])

print(var[-3])

print(var[-21])


# Il arrive souvent que l'on souhaite extraire une sous-sequence de caracteres d'une chaîne. Sous Python, on utilise une technique dite `slicing` (). La technique consiste à indiquer entre crochets `[]` les indices correspondant au
# début et à la fin de la sous-sequence que l'on souhaite extraire.
# ```{warning}
# Le caracter ayant preimier indice est inclu. Cependant,**le caracter ayant le dernier indice n'est pas iclu!!**. Si l'on veut, par exemple les trois premiers caracters, on doit indiquer 0 et 4 entre `[]` (`[0:4]`).
# - Si l'on veut les `n` premier caracters: `[:n+1]`
# - Si l'on veut les caracters a partir de l'indice `n` jusqu'a la fin de la chaine: `[n:]`
# ```
# Illustrons ca avec un exemple:

# In[82]:



var = "bonjour tout le monde"

print(var[0:0])
print(var[2:5])
print(var[0:3])

print(var[:3])

print(var[5:21])

print(var[5:])

print(var[:])


# Si l'on veut tester l'appartenece d'un caracter a une chaine on utilise l'operateur `in`. L'expression est la suivante : `caractere in chaine`. Cela nous renvoi `True` si `caractere`est dans `chaine`, sinon `False`. On peut aussi ecrire `caractere not in chaine` pour tester si le caractere n'est pas dans `chaine` (`True`) ou s'il est dans `chaine` (`False`). Voici quelques exemples:

# In[86]:


var = "bonjour tout le monde"

print('b' in var)

print('z' in var)

print('o' not in var)

print('x' not in var)


# ### quelques methodes utiles pour les chaines des caracteres
# Dans cette sections nous allons voir qulques `methodes`  pour les chaines des caracteres (lorsque nous allons etudier la programmation orientee objet, nous allons comprendre la signification de ce terme. Pour l'instant nous allons accepter que `method` signifie une fonction dont l'expression generale est `chqine.method(separateur)`).
# - split: cette methode est utlisee pour nous rendre une liste dont les elements sont les caracteres de la chaine.  On peut choisir le caractère séparateur en le fournissant comme argument, sinon c'est un espace par défaut.

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


# - count: lorsque elle est appliquee a un chaine de caracteres avec un agrgument qui est aussi une chaine de caracteres (eventuellement un caractere), elle renvoi le nombre d'occurences la derniere chaine dans la premiere chaines. ` chaine1.count(chaine2)`.

# In[106]:


var = "bonjour tout le monde"
print(var.count("b"))

print(var.count("on"))

print(var.count(" "))


# - find, index : Lorsque l'une de ces methodes est appliquee a une chaine de caractere avec un agrgument qui est aussi une chaine de caracteres (eventuellement un caractere), elle renvoi l'indicee  la chaine cherchee dans la premiere chaines (l'indice de la primiere occurence). `find` renvoit -1 si la chaine cherchee n'existe pas alors que index revoit une erreur dans la meme situation. ` chaine1.find(chaine2)` et ` chaine1.index(chaine2)`.

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


# - lower, upper, title, capitalize, swapcase: Lorsque l'une de ces methodes est appliquee a une chaine de caractere, elle la convertit on minuscule (`lower`), majuscule (`upper`), majuscule a l'initial de chaque mot (`title`), mjuscule a l'initial du premier mot (`capitalize`), et les majuscules en minuscules, et vice-versa (`swapecase`).

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


# - replace: remplace une cahine de caracteres (eventuellement un seul caractere) par une autre cahine de caractere.

# In[142]:


var = "bonjour tout le monde"
print(var.replace('b', 'B'))

print(var.replace('bonjour', 'bonsoir'))


# Formatage des chaînes de caractères
# 
# Les chaines de caracters en python sont riche en terme de fonctionalite (vous allez, au fur et mesure, decouvrir des nouvelles methods et technique avancees). Dans cette section, nou allons presenter une derniere une technique de traitement très puissante, que l’on appelle formatage des chaînes. 
# 
# Nous pouvons, d'ailleurs, faire ce que cette technique fait avec la concatenation des chaines (avec `+`). Cependant le formatage est plus lisible est ne necessite pas du code additionel. Illustrons ca avec un exemple.
# 
# 
# 
# 3 %, format, f'

# In[152]:


message = ' est le meilleur language de programmation'
nom_du_langage = 'python'
print(nom_du_langage + message)


# In[153]:


message = '{} est le meilleur language de programmation'
nom_du_langage = 'python'
print(message.format(nom_du_langage))


# In[154]:


message = '%s est le meilleur language de programmation'
nom_du_langage = 'python'
print(message % nom_du_langage)


# In[157]:


nom_du_langage = 'python'
message = f'{nom_du_langage} est le meilleur language de programmation'

print(message)


# In[ ]:





# In[ ]:





# # Manupilation des liste
# 
