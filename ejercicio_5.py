# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

#NOTA 1: tpl = tres primeras letras
#NOTA 2: dpl = dos  primeras letras

tpl_palabra_1 = palabra_1[0:3]
dpl_palabra_2 = palabra_2[0:2]


palabra_3 = tpl_palabra_1 + dpl_palabra_2
print (palabra_3)