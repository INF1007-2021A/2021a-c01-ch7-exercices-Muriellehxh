[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect-0.herokuapp.com/)

# Exercices en vrac (chapitre 7)

Avant de commencer, consultez les instructions à suivre dans [instructions.md](instructions.md)

## Objectifs

Compléter les quelques exercices suivants en modifiant le code de [exercice.py](exercice.py):

1. Écrire une fonction qui retourne le volume et la masse d’un ellipsoïde grâce à un tuple. Les paramètres sont les trois demi-axes et la masse volumique. 
   On donnera à ces quatre paramètres des valeurs par défaut. On donne : 𝑉=4/3 𝜋𝑎𝑏𝑐. Tester cette fonction par des appels avec différents nombres d’arguments.
2. En reprenant le 5e exercice du chapitre 6 sur les fréquences de lettres dans une phrase, écrivez un programme qui trie les lettres à partir du dictionnaire 
   et qui retourne la lettre avec la fréquence la plus haute, en utilisant une fonction lambda (fichier chap 6 RENOMMEZ FICHIER CHAP 6).
3. En utilisant la librairie « Turtle », dessinez un arbre en utilisant la récursivité.
    Ressources : https://docs.python.org/3.3/library/turtle.html
   (OBERVER PATTERN -> TRAIT DE Y DEVIENT DE + EN + PETIT)
   
   ![alt text](tree.png)
5. Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c"). 
    
    a) Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux sinon.
    
    b) Écrire une fonction saisie qui effectue une saisie valide et renvoie la valeur saisie sous forme d'une chaîne de caractères.
    
    c) Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la séquence et qui retourne la proportion de séquence dans la chaîne.

Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche le résultat.

Exemple d’affichage:
```python
chaîne : attgcaatggtggtacatg
séquence : ca
Il y a 10.53 % de "ca".
```


