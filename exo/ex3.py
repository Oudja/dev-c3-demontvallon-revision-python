import re

# Calculatrice simple : Écrivez un programme qui prend une chaine de caractère et effectue les opérations de base : addition, soustraction, multiplication, division.

print("Ecrivez votre opération : ")
operation = input()

def calculatrice(chaine):

    match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)', chaine)

    if match:
        chiffre1 = int(match.group(1))
        operateur = match.group(2)
        chiffre2 = int(match.group(3))

        if operateur == '+':
            result = chiffre1 + chiffre2
        elif operateur == '-':
            result = chiffre1 - chiffre2
        elif operateur == '*':
            result = chiffre1 * chiffre2
        elif operateur == '/':

            if chiffre2 != 0:
                result = chiffre1 / chiffre2
            else:
                print("Erreur : Division par zéro")
                return None

        return f"Résultat : {result}"
    else:
        print("Format d'opération incorrect")
        return None


resultat = calculatrice(operation)


print(resultat)
