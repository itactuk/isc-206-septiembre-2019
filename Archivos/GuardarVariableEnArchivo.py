import pickle

lista_estudiante = [
    {'nombre': 'jose'},
    {'nombre': 'miguel'},
    {'nombre': 'alexandra'},
]

with open("mivar.pickle", "wb") as archivo:
    pickle.dump(lista_estudiante, archivo)
