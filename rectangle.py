def rectangle(filepath_1,filepath_2):
    f1=open(filepath_1,"r")
    f2=open(filepath_2,"r")
    
    firstfile=str(f1.read())
    secondfile=str(f2.read())

    firstfile=firstfile.split("\n")
    secondfile=secondfile.split("\n")

    compt=0
    for i in firstfile:
        firstfile[compt]=list(i)
        compt+=1
    compt=0
    for j in secondfile:
        secondfile[compt]=list(j)
        
        compt+=1
    
    aligne=False
    isinall=0
    isinline=False
    ecart=0
    li=0
    
    for li in range(len(firstfile)-1) :
        for co in range(0,len(secondfile)-1):
            if(compt==i and li<2):
                isinline=True
                li+=1
            else:isinline=False
            compt=-1
            if isinline:isinall+=1
            for i in range(0,len(firstfile)):
            
            
                for j in range(0,len(secondfile)):
                    #print(li,co,i,j,isinline,isinall,compt,"|",firstfile[li][i],secondfile[co][j])
                    if(firstfile[li][i]==secondfile[co][j]):
                        if(i==0 and li==0):
                            coord=(j,co)
                            ecart=j
                        elif(i==0 and j==ecart):
                            aligne=True
                        elif(i==0 and j!=ecart):
                            aligne=False
                        compt+=1
                        
                        break
    f1.close()
    f2.close()
    if(aligne and isinall==len(firstfile) ):
        return print(coord)
    else: print("Rectangle Introuvable")
    
    
    
     

rectangle("c1.txt","c2.txt")
    
    

    