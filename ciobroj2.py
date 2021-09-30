#Date su cifre 2 broja jednog trocifrenog (a3,a2,a1)
#i jednog dvocifrenog.
#Cifre a1 i b1 su cifre jedinice , cifre a2 i b2 su cifre desetica, a a3 je cifra stotina.
# ako je poznato da je zbir ta dva broja trocifren broj, odrediti cifre zbira 

a_3 = 9
a_2 = 8
a_1 = 0

b_2 = 2
b_1 = 1

n= a_1 + b_1
m= a_2 + b_2

jedinice = n %10

desetice_0 = n//10 

desetice = (desetice_0 + m)%10

stotine_0= (desetice_0 + m)//10 

stotine = a_3 + stotine_0


if stotine < 10 :
    print( stotine, desetice, jedinice)





