# Manipulation de chaînes : Demandez à l'utilisateur de saisir une phrase, puis affichez la phrase en majuscules, en minuscules et le nombre de mots.

print("Ecrivez une phrase")

phrase = input()

phrase_en_majuscule = phrase.upper()
phrase_en_minuscule = phrase.lower()
liste_de_mot = phrase.split()
nombre_de_mot = len(liste_de_mot)

print(phrase_en_majuscule)
print(phrase_en_minuscule)
print("Nombre de mot :", nombre_de_mot)

