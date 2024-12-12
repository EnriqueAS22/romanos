numeros_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

"""
a_romanos(int)

lista_traduciones = []
- Para cada posicion, cifra de int, de atras hacia delante
    - Valor = descomponer (posicion, cifra)
    - valor_traducido = traducir (valor)
    - añadir valor_raducido a lista_traducciones

- lista_traducciones_ordenada = darle la vuelta a lista_traducciones
- concatenar lista_traducciones
"""

def descomponer(posicion: int, cifra:str) -> int:
    """
    - Pasar cifra a numero entero (int)
    - Devolver cifra * 10 ** posicion
    """
    return int(cifra) * 10 ** posicion

def traducir(valor:int) -> str:
    simbolos = {
    1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
    10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
    100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
    1000:"M",2000:"MM",3000:"MMM"
    }

    return simbolos[valor]

def a_romanos(numero: int) -> str:
    lista_traducciones = []

    numero_str = str(numero)
    reves = numero_str[::-1]
    
    for posicion, cifra in enumerate(reves):
        valor = descomponer(posicion, cifra)
        valor_traducido = traducir(valor)
        lista_traducciones.append(valor_traducido)

    lista_traducciones_inversa = lista_traducciones[::-1]

    num_romanos = ""
    for simbolo in lista_traducciones_inversa:
        num_romanos += simbolo

    return num_romanos

