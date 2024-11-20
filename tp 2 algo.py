def entasser(arbre, i, l):
    j = i
    fils_gauche = 2 * j + 1
    fils_droit = 2 * j + 2

    if fils_gauche < l and arbre[j] < arbre[fils_gauche]:

        j = fils_gauche

    if fils_droit < l and arbre[j] < arbre[fils_droit]:

        j = fils_droit

   



    if j != i:    
        arbre[j], arbre[i] = arbre[i], arbre[j]
        entasser(arbre, j, l)







def tas_max(arbre):
    for i in range(len(arbre) // 2 - 1, -1, -1):
        entasser(arbre, i, len(arbre))
    return arbre
















arbre = [25, 60, 35, 10, 5, 20, 65, 45, 70, 40, 50, 55, 30, 15, 22, 62, 64, 4, 8]





tas = tas_max(arbre)
print("arbre tas_max", tas)
