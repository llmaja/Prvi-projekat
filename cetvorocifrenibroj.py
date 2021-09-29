"""Dat je cetvorocifreni prirodan broj (abcd). 
ako su mu cifra jedinica i cifra hiljada jednake
stampati kvadrat dvocifrenog broja koji se dobije 
kad se uklone cifra jedinica i cifra hiljada


ako te dvije cifre nijesu jednake , stampati zbir kvadrata svih cifara """

x=int(input("Unesi četvorocifreni broj: ", ))

a= x//1000
b= (x//100)%10
c= (x//10)%10
d= (x%1000)%10

y= (x%1000)//10
z= a**2 + b**2 + c**2 + d **2

if a == d :
    print (y**2)
else :
    print (z)
