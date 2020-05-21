def majuscule(chaine):
    i=1
    compt=1
    nvphrase=chaine[0].lower()

    while i < len(chaine):
        
        lettre=chaine[i]
        lettreavant=chaine[i-1]
        if lettreavant==" ": 
            compt-=1  #si le caractere d'avant est un espace alors il ne faut pas le comptabiliser dans l'index
        if compt%2!=0 :
                
                lettre=lettre.upper()
                nvphrase=nvphrase+lettre
            
        else:nvphrase=nvphrase+lettre
            
        compt+=1
        i+=1
    
    return nvphrase


print(majuscule("Bien le bonjour!"))