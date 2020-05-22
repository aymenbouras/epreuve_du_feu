def anagramme(base,file):
    fich=open(file,"r")
    mots=str(fich.read())
    mots=list(mots.split("\n"))
    compt=0
    for i in mots:
        mots[compt]=list(i)
        
        compt+=1
    compt=0
    result=list()
    for i in range(len(base)):
        compt=0
        if len(mots[i])!=len(base):
            continue
        for j in range(len(base)):
            if base[i]==mots[i][j]:
                compt+=1
                print(mots[i][j])
        if(compt==len(base)-3):result.append(mots[i])
            
        
    

anagramme("arbre","fr.txt")