a = int(input("digite um valor inteiro "))
b = 1
c = 0
if(a<=0):
    print("Número inválido")
else:
    while(b<=a):
        if((a%b)==0):
            c = c + 1 
        b = b + 1 
    if(c == 1 or c > 2):
        print("Não primo")
    else:
        print("Primo")
        
