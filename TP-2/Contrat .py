class Contrat:
        def __init__(self, numero, date, client, montantContrat):
                self.__numero = numero
                self.__date = date
                self.__client = client
                self.__montantContrat = montantContrat
                self.__interventions = []
                self.__nbIntervention = 0
        
        def montant(self):
                
                return self.__montantContrat
                
        def ecart(self):
        
                pass