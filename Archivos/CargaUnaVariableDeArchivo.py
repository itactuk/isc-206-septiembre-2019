import pickle



with open("mivar.pickle", "rb") as archivo:
    lista_estudiante = pickle.load(archivo)
    print(lista_estudiante)
