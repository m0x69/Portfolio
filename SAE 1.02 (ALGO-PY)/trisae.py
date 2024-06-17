from numpy import *
from random import *

########### Algo perso ###############

def main (tab)->int:
    """
    pre-condition: len(tab)>1
    post-condition : tri tab par ordre croissant 
    """
    
####detection
    
    parcourt=len(tab)//2+len(tab)%2  # moitie du tableau (ou moitie+1 si longueur tableau impaire)
    
    for i in range (parcourt):
        minimum=i                   # initialisation du minimum
        maximum=len(tab)-i-1        # initialisation fu maximum
        
        for j in range(i,len(tab)-i):   # boucle qui diminue en longueur en fonction du nombre d'éléments deja tries
            if tab[j]<tab[minimum]:     # recherche du minimum dans le tableau
                minimum=j
            if tab[j]>tab[maximum]:     # recherche du maximum dans le tableau
                maximum=j

####invertion
                
        temp=tab[minimum]                   # échange du minimum avec le premier élément du tableau non trier
        tab[minimum]=tab[i]
        tab[i]=temp

        if i!=maximum:                      # échange du maximum avec le premier élément du tableau non trier
            temp=tab[maximum]
            tab[maximum]=tab[len(tab)-1-i]
            tab[len(tab)-1-i]=temp
        else:                               # si valeur maximum = premiére valeur non trier,alors elle à deja été échangée
            temp=tab[minimum]               # (à cause du minimum) donc échange avec sa nouvelle position
            tab[minimum]=tab[len(tab)-1-i]
            tab[len(tab)-1-i]=temp
    return tab


