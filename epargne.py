# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:54:15 2022

@author: younes
"""

from compte import CompteBancaire 


class CompteEpargne(CompteBancaire):
    "Calculer la somme aprés capitalisation et autres opérations"
    
    def __init__(self, nom = "Belabid" , solde = 10):
        CompteBancaire.__init__(self, nom, solde)
        self.taux = .3
        self.nom = nom
        self.solde = solde

    def ChangerTaux(self):
        
        while True:   
            taux_personnel = input("Donnez un nouveau taux d'intérét (ex : .2 %) ou ENTER pour garder le taux par defaut : ")
            
            if len(taux_personnel) > 0:
                try:
                    taux_personnel = float(taux_personnel)
                    self.taux = taux_personnel
                    return self.taux
                except:
                    print("ERREUR ! Vous devez donner un chiffre !")
            else:
                print('Vous avez choisi de garder le taux par defaut qui est .3%')
                print()
                return
                
    
    def Capitalisation(self,nombredemois):
        self.nombredemois = nombredemois
        print(f"Capitalisation sur {self.nombredemois} au taux d'intérét de {self.taux} %")
       
        for i in range(self.nombredemois):
            interet = (self.solde) * self.taux
            self.solde += interet/100
     
        
        
c1 = CompteEpargne("BELABID", 600)
c1.depot(350)
c1.afficher()


c1.Capitalisation(12)
c1.afficher()


c1.ChangerTaux()
c1.Capitalisation(12)
c1.afficher()



        
        
        
                
        
        