print("It's a trap")


def eingabe():
    file = open("output_encoded.txt", "r")
    file_data = str(file.read())
    file.close()

    return file_data

def zersteuckelung(file_data):
    file_data_liste = []

    leange = len(file_data)
    for n in range(leange):
        temp_var = file_data[n]
        file_data_liste.append(temp_var)
    
    return file_data_liste, leange

def key_auslesen():
    file = open("key.txt", "r")
    liste = file.read()
    liste_neu = liste.split("\n")
    liste_sort = liste_neu[0].split("|")
    liste_unsort = liste_neu[1].split("|")

    return liste_sort, liste_unsort

def codierung(file_data_liste, leange, liste_sort, liste_unsort):
    output_liste = []
    for n in range(leange):
        temp_var = file_data_liste[n]
        leange_liste = len(liste_sort)
        for v in range(leange_liste):
            if temp_var == liste_unsort[v]:
                output_liste.append(liste_sort[v])
            
    return output_liste

def ausgabe(output_liste):
    output = "".join(output_liste)
    new_file = open("output_decoded.txt", "w")
    new_file.write(output)
    new_file.close


def main():
    file_data = eingabe()
    file_data_liste, leange = zersteuckelung(file_data)
    liste_sort, liste_unsort = key_auslesen()
    output_liste = codierung(file_data_liste, leange, liste_sort, liste_unsort)
    ausgabe(output_liste)

main()
print("\ndone")

