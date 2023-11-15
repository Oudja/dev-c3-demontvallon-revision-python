# Listes : Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.
# Affichage de chaque opération

list = [24, 50, 86, 22, 3, 20, 33, 86, 11, 12]

print("Le nombre maximum de cette liste est : " + str(max(list)))
print("Le nombre minimum cette liste est : " + str(min(list)))


def calculerLaMoyenne(list):
    count = 0
    lengthList = len(list)
    for item in list:
        count += item
    count = count / lengthList
    print("La moyenne est de : " + str(count))


calculerLaMoyenne(list)
