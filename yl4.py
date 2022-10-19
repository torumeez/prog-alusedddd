a = input('sisesta esimene number:')
b = input('sisesta teine number:')


def answer(a, b):
      
    if a <= b:
        return a
    else:
        return b

print('Nende kahe arvu miinimum on:', answer(a, b))
