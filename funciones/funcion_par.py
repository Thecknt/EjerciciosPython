

def pares(numeros):
    pares = [x for x in numeros if x %2 == 0]
    return pares

numeros = range(10+1)

if __name__ == '__main__':
    print('---------------funciones pares----------------')
    print(f'Los numeros pares son {pares(numeros)}')