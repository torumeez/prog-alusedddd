a = input('sisesta esimene number:')
b = input('sisesta teine number:')


def answer(x, y):
      
    if x <= y:
        return x
    else:
        return y

print('Nende kahe arvu miinimum on:', answer(a, b))
