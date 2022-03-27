import random


menu = """
   //Bienvenido al generador de contraseñas//

**deberas escribir tu usuario, el programa te genera
         una contraseña automatica**

"""
print(menu)
usuario = input("escribe tu usuario: ")

def generator_pasword():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    characters  = MAYUS + MINUS + NUMS + CHARS
    pasword = []

    for i in range(15):
        character_random = random.choice(characters)
        pasword.append(character_random)

    pasword = ''.join(pasword) 
    return pasword   

def run():
    pasword = generator_pasword()
    print('tu usuario es: ' + usuario + ' y tu nueva contraseña es: ' + pasword)


if __name__=='__main__':
    run()