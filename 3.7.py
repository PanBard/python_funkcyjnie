def main():

    tuple_krotka = ("elo","belo","kolp","derko")
    print("Tuple before sort: ",tuple_krotka)

    lista = list(tuple_krotka)
    lista.sort()

    tuple_krotka_2 = tuple(lista)

    print("Tuple after sort: ",tuple_krotka_2)

if __name__ == '__main__':
    main()