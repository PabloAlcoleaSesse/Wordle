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

def funcionamientoWordle():
    miPalabra = elegirPalabra()
    if miPalabra:
        print(miPalabra)

if __name__ == "__main__":
    funcionamientoWordle()