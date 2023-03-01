from Employe import Employe
from Intervention import Intervention
technicien =  Employe(1,"Danie","Developpeur","1/02/2023")


intervention = Intervention(1,"1/03/2023",3,900,technicien)

frais_mo = intervention.fraisMo()

