# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:01:13 2022

@author: younes

"""

    
class CompteBancaire(object):
    
    def __init__(self, nom = "Belabid", solde = 1000):
        self.nom = nom
        self.solde = solde
        
    def depot(self, somme):
        
        self.solde += somme
        
    def retrait(self, somme):
        self.solde -= somme
        
    def afficher(self):
        print("Le solde du compte bancaire de M.", self.nom, "est de", self.solde, "euros")
        
if __name__ == "__main__":    
    compte = CompteBancaire("BELABID", 10000)
    compte.depot(4000)
    compte.retrait(1000)
    compte.afficher()

    
