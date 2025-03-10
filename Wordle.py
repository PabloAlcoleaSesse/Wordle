class Palabra:
    letra1 = ""
    letra2 = ""
    letra3 = ""
    letra4 = ""
    letra5 = ""
    
    def __init__(self, letra1, letra2, letra3, letra4, letra5):
        self.letra1 = letra1
        self.letra2 = letra2
        self.letra3 = letra3
        self.letra4 = letra4
        self.letra5 = letra5
    
    def __str__(self):
        return f"{self.letra1}{self.letra2}{self.letra3}{self.letra4}{self.letra5}"



def elegirPalabra():
    try:
        with open("palabras.txt", "r") as fichero:
            lineas = fichero.readlines()
            from random import randint
            numero = randint(0, len(lineas) - 1)
            palabra = lineas[numero].strip()
            
            letras = list(palabra)
            if len(letras) >= 5:
                miPalabra = Palabra(letras[0], letras[1], letras[2], letras[3], letras[4])
                return miPalabra
            else:
                raise ValueError("La palabra seleccionada es demasiado corta")
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo palabras.txt")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None



def numlineas():
    try:
        with open("palabras.txt", "r") as fichero:
            lineas = fichero.readlines()
            return lineas
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo palabras.txt")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def analizarPalabra(palabra, lineas):
    for palabras in lineas:
        if palabra == palabras.strip():
            return True
        else: 
            return False
    
    

 



def funcionamientoWordle():
    miPalabra = elegirPalabra()
    lineas = numlineas()
    print("Introduce una palabra de cinco letras")

    for i in range(5):
        strpalabraInput = input("Introduce una palabra de 5 letras: ")
        palabraInput = list(strpalabraInput.lower())
        miPalabraInput = Palabra(palabraInput[0], palabraInput[1], palabraInput[2], palabraInput[3], palabraInput[4])
        
        decision = analizarPalabra(strpalabraInput, lineas)
        if decision == False:
            print("La palabra no existe")
        else:
            if palabraInput == miPalabra:
                print("¡Felicidades! Has adivinado la palabra")
                break
            else:
                if miPalabraInput.letra1 == miPalabra.letra1:
                    print("X")
                elif miPalabraInput.letra1 != miPalabra.letra1 or miPalabra.letra2 or miPalabra.letra3 or miPalabra.letra4 or miPalabra.letra5:
                    print("O")
                else:
                    print("-")
                
   


def JuegoWordle():
    print(
        "\n"
        "################################\n"
        "      Bienvenido a Wordle\n"
        "################################\n"
        "\n"
        "Como Jugar: El jugador debera adivinar una palabra de 5 letras\n"
        "La palabra debera ser escrita en minusculas\n"
        "Si la letra esta en la palabra, se mostrara una 'X'\n"
        "Si la letra no esta en la palabra, se mostrara un '-'\n"
        "Si la letra esta en la palabra pero no en la posicion correcta, se mostrara un 'O'\n"
        "\n"
        "################################\n"
        "\n"
        "        ¡Buena Suerte\n"
        "\n"
        "################################\n")

    while(True):
        funcionamientoWordle()
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ")
        if respuesta.lower() != "n":
            continue
        else:
            print("Gracias por jugar")
            break


if __name__ == "__main__":
    JuegoWordle()