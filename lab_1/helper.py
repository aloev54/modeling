def getdiff(massU, mass1, mass2):
    for i in range(len(mass1)):
        if round(mass2[i], 2) - round(mass1[i], 2) != 0:
            return round(massU[i-1], 2)