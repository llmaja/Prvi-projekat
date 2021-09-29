"""Napisati kod koji ucitava dva cijela broja m i n i stampa poruku " 
    x je djeljiv sa y 
ili x nije djeljiv sa y """




m=int(input( " Unesi cio broj: "))
n=int(input( " Unesi cio broj: "))

if m%n ==0:
    print (m, "je djeljiv sa", n)
else :
    print (m, "nije djeljiv sa", n)
