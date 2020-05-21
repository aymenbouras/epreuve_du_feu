def escalier(nbr):
    compt=1
    while nbr > 0 :
        
        for i in range(nbr,1,-1):
            print(" ",end="")
        for j in range(0,compt):
            print("#",end="")
        print("")
        compt+=1 
        nbr-=1
        
        
    


escalier(4)
