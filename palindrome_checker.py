'''
AQUÍ INICIAREMOS EL PROGRAMA

'''
def palindrome(word):
    word = word.replace(' ', '')
    word = word.upper()
    invert_word = word[::-1]
    if word == invert_word:
        return True
    else:
        return False



def run():
    word = input('ESCRIBE UNA PALABRA: ')
    es_pal = palindrome(word)
    if es_pal == True:
        print('ES PALÍNDROMO')
    else: 
        print('NO ES UN PALÍNDROMO')



#Python comienza a correr el código a partir de aquí
if __name__ == '__main__':
    run()
