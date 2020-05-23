def factoriel_retour(n):
    
    x=1
    for i in range(2,n+1):
        x*=i
    return x

 

print (factoriel_retour(49))