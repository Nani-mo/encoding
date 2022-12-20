print("It's a trap")
import random

def key_auslesen():
    file = open("key.txt", "r")
    liste = file.read()
    liste_neu = liste.split("\n")
    liste_sort = liste_neu[0].split("|")

    return liste_sort

def key_generate(liste_sort):
    liste_random = liste_sort
    random.shuffle(liste_random)
    liste_random = "|".join(map(str, liste_random))
    print(liste_random)

    liste_random = "".join(liste_random)
    new_file = open("new_key.txt", "w")
    new_file.write(liste_random)
    new_file.close

def main():
    liste_sort = key_auslesen()
    key_generate(liste_sort)

main()