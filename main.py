'''
Genera una matrice di numeri casuali e la salva in un file di testo
l'applicazione deve chiedere all'utente:
- le dimensioni della matrice
- il range di valori da generare (devono essere interi relativi in
  un intervallo)
- il percorso del file in cui salvare la matrice
La matrice viene salvata nel seguente formato:
- sulla prima riga le dimensioni
- sulle righe successive gli elementi (una riga della matrice per
  ogni riga di testo) separati da uno spazio
'''

import random


def genera_matrice(righe, colonne, minimo, massimo):
    """
    Genera una matrice di interi casuali compresi
    tra minimo e massimo (estremi inclusi).
    """
    matrice = []

    for i in range(righe):
        riga = []
        for j in range(colonne):
            riga.append(random.randint(minimo, massimo))
        matrice.append(riga)

    return matrice


def salva_matrice(matrice, percorso):
    """
    Salva la matrice in un file di testo.
    La prima riga contiene le dimensioni.
    """
    with open(percorso, "w", encoding="utf-8") as file:
        righe = len(matrice)
        colonne = len(matrice[0])

        file.write(f"{righe} {colonne}\n")

        for riga in matrice:
            file.write(" ".join(str(x) for x in riga) + "\n")


def main():
    print("Generazione di una matrice casuale\n")

    righe = int(input("Numero di righe: "))
    colonne = int(input("Numero di colonne: "))

    minimo = int(input("Valore minimo: "))
    massimo = int(input("Valore massimo: "))

    percorso = input("Percorso del file di destinazione: ")

    if righe <= 0 or colonne <= 0:
        print("Errore: le dimensioni devono essere positive.")
        return

    if minimo > massimo:
        print("Errore: il minimo non può superare il massimo.")
        return

    matrice = genera_matrice(righe, colonne, minimo, massimo)

    try:
        salva_matrice(matrice, percorso)
    except OSError as e:
        print(f"Errore durante il salvataggio: {e}")
        return

    print(f"\nMatrice salvata nel file '{percorso}'")


if __name__ == "__main__":
    main()
