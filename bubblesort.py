import random
import copy
import time

def insertion_sort(liste):
    
    count = sort = 0
    
    n = len(liste)
    for i in range(1, n):
        einzusortierender_wert = liste[i]
        j = i
        count += 1
        while j > 0 and einzusortierender_wert < liste[j-1]:
            liste[j] = liste[j-1]
            j -= 1
            sort += 1
        liste[j] = einzusortierender_wert
        
    return liste, count, sort

def bubble_sort(liste):
    
    count = sort = 0
    
    n = len(liste)
    for i in range(n):
        for j in range(n-1):
            count += 1
            if liste[j] > liste[j + 1]:
                sort += 1
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
    return liste, count, sort

def bubble_sort2(liste):
    
    count = sort = 0
    
    n = len(liste)
    for i in range(n):
        for j in range(n-i-1):
            count += 1
            if liste[j] > liste[j + 1]:
                sort += 1
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
    return liste, count, sort

################## MAIN ###################

listensize = 20000
liste = []
liste2 = []
liste3 = []

zeitanfang = time.time()
for i in range(listensize):
    liste.append(random.randint(1, 200000))
liste2 = copy.deepcopy(liste)
liste3 = copy.deepcopy(liste)
zeitende = time.time()
print("Dauer Programmausführung:",zeitende-zeitanfang)

zeitanfang = time.time()    
liste, durchlaeufe, sort = bubble_sort(liste)
print("Bubble Sort:",durchlaeufe, sort)
zeitende = time.time()
print("Dauer Programmausführung:",zeitende-zeitanfang)
zeitanfang = time.time() 
liste, durchlaeufe, sort = bubble_sort2(liste2)
print("Bubble Sort2:",durchlaeufe, sort)
zeitende = time.time()
print("Dauer Programmausführung:",zeitende-zeitanfang)
zeitanfang = time.time() 
liste, durchlaeufe, sort = insertion_sort(liste3)
print("Insertion sort:",durchlaeufe, sort)
zeitende = time.time()
print("Dauer Programmausführung:",zeitende-zeitanfang)