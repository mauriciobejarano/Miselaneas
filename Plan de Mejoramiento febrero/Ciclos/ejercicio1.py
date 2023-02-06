#A continuacion veremos los primeros usos de los bucles en pithon con el ciclo for
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])