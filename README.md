# Wordle

Cosas cambiadas.

Es mejor utilizar una lista en vez de 5 variables para guardar las letras
Es mejor utilizar una clase "Letra" para gestionar las letras e implementar la logica en ellas.
Los imports se hacen al principio del archivo, no donde te da la gana.
He parametrizado tanto el archivo de palabras, como la longitud de la palabra.
Mejor utilizar random.choice() si quieres un elemento aleatorio de una lista.
Aprovecha el init de Wordle para cargar la palabra del archivo.
He utilizado @Property para hacerlo mas limpio, pero la logica funciona igual con funciones.
Explicacion en detalle

Clase Letra

Letra guarda la letra que representa, y si se ha adivinado o no.
Si con el metodo check() comprubas si es la letra, y si lo es cambia a guessed.
El "to string" comprueba si la letra se ha descubierto, si se ha descubierto la muestra, si no muestra "_"

Clase Wordle

Se ha cambiado las 5 variables letra a una list de Clases letra.
El metodo elegir palabra ahora forma parte de la clase, y se llama en el init para autoiniciarse.
Las propiedades (pueden ser metodos) para control de fin de juego y para ver la palabra (que al interactuar con el to_string de la clase letra solo muestra las descubiertas
Main Loop

He hecho mas bonito el main loop, inicializando la palabra antes de loop, y haciendo captura de errores SOLO DE LAS ZONAS NECESARIAS


