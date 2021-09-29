"""Dimenzije pravougaonika su 543 i 130. 
koliko kvadrata stranice 65 je moguce izrezati iz tog pravougaonika"""

a= 543
b= 130
c= 65


P_pravougaonika = a * b 
P_kvadrata = c**2

n=P_pravougaonika//P_kvadrata
print ("Može se izrezati", n," kvadrata" )