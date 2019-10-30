from typing import Dict


def contar_como_holas(texto: str) -> Dict[str, int]:
    holas = texto.count("holas")
    como = texto.count("como")
    d = {'holas': holas, 'como': como}
    return d

def extrae_nombre_funcion(texto: str):
    resultado = []
    indice_par = texto.find('(')
    indice_par+=1
    texto_aux = texto[indice_par:]
    indice_2ptos = texto_aux.find(':')
    texto_aux = texto_aux[:indice_2ptos]
    resultado.append(texto_aux)
    return resultado
