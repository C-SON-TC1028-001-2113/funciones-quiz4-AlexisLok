#Se define la funcion que realiza la operación de cartas
def tarjetas(papel, plum):
    #En el primer if, se analiza si hay maayor numero de plumas o es el mismo nuemreo, debido a que se hacen menos cartas con papel
    if plum > papel or papel == plum:
        tarjetas = papel * 12
        return tarjetas
    #Si hay menos plumones, entonces se limita a la cantidad de plumones para hacer cartas
    else:
        tarjetas = plum *35
        return tarjetas
def main():
    #escribe tu código abajo de esta línea

    #Se definen las variables 
    papel = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones = int(input("Dame la cantidad de plumones: "))

    #Se llama a la funcion
    max= tarjetas(papel, plumones)

    #Se imprime la cantidad maxima de cartas
    print("El número máximo de tarjetas que se pueden hacer es: "+ str(max))
if __name__=='__main__':
    main()
