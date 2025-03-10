import random

class Letra():
    letra:str
    
    def __init__(self, letra):
        self.letra = letra
        self.guessed = False
        
    def check(self, letra:str):
        if letra == self.letra:
            self.guessed = True
            
    def __str__(self): return self.letra if self.guessed else '_'
    
    

class Wordle:
    letras: list[Letra]
    
    # CONST
    WORDS_FILE = "palabras.txt"
    
    def __init__(self, _len:int = 5):
        self.len = _len
        self.letras = [Letra(w) for w in self.elegirPalabra()]
        
    def check(self, word:str):
        if len(word) != self.len: raise IndexError('Word must have {} letters'.format(self.len))
        
        for i in range(self.len): self.letras[i].check(word[i])
        
    def elegirPalabra(self):
        with open(self.WORDS_FILE, "r") as fichero:
            return list(random.choice([word.strip() for word in fichero.readlines() if len(word.strip()) == self.len]))

        
    @property
    def result(self): return ''.join([str(l) for l in self.letras])
    
    @property
    def completed(self): return all([l.guessed for l in self.letras])


if __name__ == "__main__":
    try: wordle = Wordle()
    except IndexError as e: print(e)
    
    _try = 0
    while not wordle.completed:
        _try += 1
        print('#' * 20)
        print('Try: {}'.format(_try))
        print('Wordle: {}'.format(wordle.result))
        word = input('WORD:   ')
        try: wordle.check(word)
        except IndexError: print('Word must have {} letters'.format(wordle.len))
    print('Result: "{}" in {} trys'.format(wordle.result, _try))