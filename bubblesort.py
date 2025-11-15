import random

def bubble_sort(liste):
    
    count = 0
    
    n = len(liste)
    for i in range(n):
        for j in range(n-1):
            count += 1
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
    return liste, count


################## MAIN ###################

count = 0
listensize = 100
liste = []

for i in range(listensize):
    liste.append(random.randint(1, 1000))

print(bubble_sort(liste))