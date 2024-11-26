tuple = ('abraco', 'gostar', 'penteado', 'cabelo', 'marmanjo', 'jaqueline', 'gustavo', 'encrenca', 'caneca', 'jorra', 'abriu', 'camelo')
vogais = ('a', 'e', 'i', 'o', 'u')
for i in range(0, len(tuple)):
    print('As vogais da palavra ' + tuple[i] + ' são: ', end = '')
    for j in range (0, len(vogais)):
        print(vogais[j] + ' ' if vogais [j] in tuple[i] else '', end = '')
    print(' ')
