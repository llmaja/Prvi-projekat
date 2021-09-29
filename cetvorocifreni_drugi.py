"""12. dat je cetvorocifreni broj, 
napisi kod koji stampa stotine tog broja """

x=int(input("Unesi četvorocifreni broj: ",   ))

def prva_cifra(x):
    a = x//1000
    return a 

def druga_cifra (x):
    b= (x//100)%10
    return b 
def treca_cifra(x) :
    c= (x//10)%10
    return c

def cetvra_cifra (x) :
    d= (x%1000)%10
    return d

rezultat0= druga_cifra (x)

print ("Broj stotina je ",rezultat0  ) 




# Napisati kod koji stampa kvadrat cifara cetvorocifrenog broja

rezultat = prva_cifra(x) **2
rezultat1= druga_cifra(x) **2
rezultat2= treca_cifra(x) **2
rezultat3= cetvra_cifra(x) **2

print ("Kvadrat cifara cetvorocifrenog broja je ", rezultat +rezultat1 + rezultat2 + rezultat3)


# Stampati super ako vazi a c=b d 

rezultat5= ("Super")

if treca_cifra(x) == druga_cifra(x):
    print(rezultat5)
else:
    None
