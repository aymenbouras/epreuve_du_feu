def rectangle(fichier1,fichier2):
    f1 = open(fichier1)
    f2 = open(fichier2)

    fich1 = []
    fich2 = []
    while 1:
        ln = f1.readline().split()
        if ln:
            fich1.append(ln)
        else:
            break
        f1.close()
    while 1:
        ln = f2.readline().split()
        if ln:
            fich2.append(ln)
        else:
            break
        f2.close()

rectangle(./c1.txt,./c2.txt)
    
    

    