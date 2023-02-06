#En los condicionales tenemos instrucciones la cuales definira
#lo que sebe hacer por ejemplo como vemos en el ejercicio
#el break dara pausa a la operacion segun la instruccio dada
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))