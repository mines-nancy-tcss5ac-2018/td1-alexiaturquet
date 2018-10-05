
##défintions des fonctions
#probleme_16
def somme_des_termes (n):
    chiffres = str (n)
    somme = 0
    for i in range (len (chiffres)):
        somme += int (chiffres[i])
    return (somme)
        

def solve_16(n):
    return (somme_des_termes(n))




#probleme_22
def cree_une_liste_avec_les_noms (fichier):
    for ligne in fichier:
        x=ligne.split('","')
    x[0]=x[0][1:]
    x[-1]=x[-1][:-1]
    return(x)

def tri_liste_par_ordre_alphabetique(liste):
    L=sorted(liste,key=None,reverse=False)
    return(L)

def somme_des_lettres (chaine):
    """il faut donner la chaîne de caractères en majuscule"""
    somme = 0
    for i in range (len (chaine)):
        somme += ord(chaine[i])-64
    return (somme) #le A majuscule commence au numéro 65
    
def solve_22 (fichier):
    liste_triee = tri_liste_par_ordre_alphabetique(cree_une_liste_avec_les_noms (fichier))
    resultat = 0
    for i in range (len (liste_triee)):
        somme = somme_des_lettres( liste_triee[i])
        resultat += somme*(i+1)
    return (resultat)


#probleme_55

def palindrome(n):
    chaine=str(n)
    for i in range(len(chaine)//2):
        if chaine[i]!=chaine[-i-1]:
            return (False)
    return(True)

def inverse (n):
    chaine = str(n)
    resultat=''
    for i in range(len(chaine)):
        resultat += chaine[-1-i]
    return(int(resultat))
        
def solve_55 (n):
    compteur=0
    for i in range(n):
        j=1
        a=i
        while j<=50 and not (palindrome (inverse (a) + a)):
            a = a + inverse (a)
            j += 1
        if j==51:
            compteur += 1
    return(compteur)
            
## code à exécuter
#probleme_16

assert somme_des_termes (123)==6
print (solve_16 (2**1000))

#probleme_22

f = open ('p022_names.txt', 'r')
assert somme_des_lettres ('AAA') == 3
assert tri_liste_par_ordre_alphabetique (['a','c','b']) == ['a','b','c']
print (solve_22 (f))

#probleme_55

assert palindrome(123)==False
assert palindrome(5)==True
assert inverse(123)==321
print(solve_55(10000))
