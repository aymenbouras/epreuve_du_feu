def tri(nbr):
    for i in range(len(nbr)-1,0,-1):
        for  j in range(i):
            if nbr [ j ] > nbr [ j +1]:
                     nbr [ j ] , nbr [ j +1] = nbr [ j +1] , nbr [ j ]
            

        
       
            

    return nbr

print(tri([2,4,6,7,1]))