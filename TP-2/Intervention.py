from Employe import Employe
class Intervention:
        
        def __init__(self, numero,date,duree,tarifkm,technicien):
        
                self.__numero = numero
                self.__date=date
                self.__duree=duree
                self.__tarifkm=tarifkm
                self.__technicien=Employe
                
                
        def affiche(self):
                print("Numéro : " , self.__numero ,
                        " \n Date : " , self.__date, 
                        "\n Duree : " , self.__duree,
                        "\n Tarifkm : " , self.__tarifkm,
                        '\n technicien : ' , self.__technicien)
               
                
        def fraisKm(self,dist):
                
                return self.__tarifkm * dist
                
        def fraisMo(self):
                if self.__technicien != None:
                        self.__duree * self.__technicien.coutHoraire(self.__duree)
                else:
                        return 0.0
                
         
         
   