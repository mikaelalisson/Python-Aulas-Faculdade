frase = input('Digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:]) #esse -2: foi para diminuir a string