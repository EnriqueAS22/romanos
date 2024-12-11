numeros_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def a_romanos(valor: int) -> str:
    romano = ''
    for clave, value in numeros_romanos.items():
        if value == valor:
            romano = clave
    return romano

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
    pass

def a_romanos(numero: int) -> str:
    lista_traducciones = []

    numero_str = str(numero)
    reves = numero_str[::-1]
    
    for posicion, cifra in enumerate(reves):
        valor = descomponer(posicion, cifra)
        valor_traducido = traducir(valor)
        lista_traducciones.append(valor_traducido)

    lista_traducciones_inversa = lista_traducciones.reverse() # Tambien se puede hacer -> lista_traducciones[::-1]

    num_romanos = ""
    for simbolo in lista_traducciones_inversa:
        num_romanos += simbolo

    return num_romanos

