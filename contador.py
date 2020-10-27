
#!/usr/bin/python3
#-*-coding:utf-8 -*-
import sys
data = '0'

with open('contador.txt', 'w+') as f:
    f.seek(0)
    #import ipdb; ipdb.set_trace()
    list1 = f.readlines()
    print('list1_first', list1)

    #si el fichero esta vacío le escribe un cero y sino no hace nada
    if len(list1) == 0:
        f.write(data)
        f.seek(0)
        list1 = f.readlines()
        print('list1_second', list1)
        print(True)
    else:
        print(False) #NUNCA ENTRA ACAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAA
        pass    

    #leo el valor del contador del fichero
    counter = int(list1[0])
    print('counter:1', counter)

    #leo los argumentos ignorando el nombre del script
    arguments =  sys.argv[1:]

    if len(arguments) ==1:
        if arguments[0] == 'inc':
            counter +=1
        elif arguments[0] == 'dec':
            counter-=1
        else:
            print('Error: Command not found')
    else:
        print('El contador marca:', counter)
        
    print('counter:2', counter)


with open('contador.txt', 'w+') as f:
    f.seek(0) 
    f.write(str(counter))
    list1 = f.readlines()
    print('list1_third', list1)
#NO SOBREESCRIBEEEEEEEEEEEEE!!!!!!AAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGGGGGHHHHHHHHHH


