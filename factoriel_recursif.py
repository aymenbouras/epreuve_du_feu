def factoriel(nbr):
    if nbr<2:
        return 1
    else:

        return nbr*(factoriel(nbr-1))

print(factoriel(3))
