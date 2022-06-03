Instructions composées
=======================
Sous Python (tout comme dans les autres langages de programmation, il arrive (plus c'est le cas standard) qu'une instruction ne soit pas simple (une seule ligne). Une instruction peut être composée de plusieurs lignes (bloc d'instructions).

Un bloc d'instruction est (instruction composées) a une structure standard : 
- une ligne d'en-tête terminée par un double point, 
- suivie d'une ou de plusieurs instructions indentées sous cette ligne d'en-tête.

**Bloc d'instructions - Indentation**: En python, on définit un bloc d'instructions par une indentation. Ceci dit, on décale le début des instructions vers la droite à l'aide des espaces en début de chaque ligne du bloc (le nombre standard est 4 espaces mais ce n'est pas obligatoire). Toutes les instructions d'un même bloc doivent être indentées exactement au même niveau. Voici une illustration d'un bloc d'instructions :

```python
Ligne d'en-tête :
 Première instruction du bloc
 ... ...
 ... ...
 Dernière instruction du bloc

Une instruction en dehors du bloc précédant
```

Il se peut qu'un bloc d'instructions fait partie d'un autre bloc. Il est aussi d'avoir des blocs d'instructions imbriquées (plusieurs fois) :

```python
Ligne d'en-tête pour bloc1:
 Ligne d'en-tête pour bloc2:
    Première instruction du bloc2
    ... ... (bloc2)
    Ligne d'en-tête pour bloc3:
        Première instruction du bloc3
         ... ... (bloc3)
         ... ... (bloc3)
         Dernière instruction du bloc3
    ... ... (bloc2)
    Dernière instruction du bloc2
 ... ...(bloc1)
 ... ...(bloc1)
 Dernière instruction du bloc1

Une instruction en dehors de tous les blocs précédents
```


Nous le présent chapitre nous allons deux cas de ces blocs d'instructions : 
- les instructions conditionnelles
- les boucles
