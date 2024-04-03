import math
#set_methods
'''
set = {'olma', 'anor', 'uzum', 'orik'}
set2 = {'1olma', 'anor', '3uzum', 'orik'}
#set.update(set2)
#set.pop()
#newest = set.union(set2)
#newest = set.intersection(set2)
newest = set.symmetric_difference(set2)
print(newest)
'''

'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
newest = []
for i in set1:
    for j in set2:
        if i == j:
            newest.append(i)
print(set(newest))
'''
'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}
newest = []
for i in set1:
    if i not in set2:
        newest.append(i)
print(set(newest))
'''
'''
#string42
words = "OLMA, ANOR, SUV, SHAFTOLI, ANJIR"
numbers = 1, 2, 3, 4, 5, 6
dict = {}
for i in words:
    dict [numbers] = i
print(dict)
'''    
'''
#string 43
words = "OLMA SUV BANAN SHAFTOLI KITOB UZUM"
a = words.split()
for i in a:
'''   

'''
#series 7
numbers = [18.251, 4.573, 9.623, 23.440, 51.719]
new = []
s = 0
for i in numbers:
   x = round(i)
   new.append(x)
print('yaxlitlangan sonlar:',new)
for j in new:
    s+=j
print('sonlarning yigindisi:', s)
'''
'''
#series 10.1
numbers = [-42, -53, -68, -82, -95, -121]
new = []
for i in numbers:
'''

'''
#series 11        
numbers = [14, 27, 42, 53, 68, 79, 82, 95, 108, 117, 121, 136]
new = []
k = int(input('k ni kiriting: '))
for i in numbers:
    if i < k:
        print(True)
else:
    print(False)
'''    
  
   

'''
#series 13
numbers = [-20, -40, -70, -60, -120, -140, -150, -170, -180, -200]
new = []
for i in numbers:
    if i > 0 and i % 2 == 0:
        print(True)
    else:
        print(0)
'''
'''
#series 14
numbers = [50, 40, 70, 60, 120, 140, 150, 170, 180, 200]
k = int(input('k ni kiriting: '))
new = []
for i in numbers:
    if i < k:
        new.append(i)
print(f"{new}\n k dan kichik sonlar {len(new)} ta")
else:
    print(0)
'''
'''
#series 16
numbers = [50, 30, 140, 60, 190, 70, 150, 200, 120, 180]
k = int(input('k ni kiriting: '))
new = []
for i in numbers:
    if i > k:
        new.append(i)
a = max(new)
print(f"{new}\n k sonidan katta bolgan oxirgi son: {a}\n k sonidan katta bolgan oxirgi sonning indeksi: {new.index(a)}")
'''


'''
#series 17
numbers = [14, 27, 42, 53, 68, 79, 82, 95]
b = int(input('b ni kiriting: '))
for i in range(len(numbers)):
    numbers.insert(i*2, b)
print(numbers)
'''
'''
#series 18
numbers = [14, 27, 42, 42, 53, 68, 79, 79, 82, 95, 95]
new = []
for i in numbers:
    if numbers.count(i) != 2:
        new.append(i)
print('har xil qiymatli sonlar:', new)
'''
'''
#series 4
numbers = [17, 8, 13, 23, 11, 5]
n = int(input('n ni kiriting: '))
k = []
y = []
for i in numbers:
    i += n
    y.append(i)
print("n natural sonining n ta haqiqiy sonlar bilan yig'indisi:", y)
for j in numbers:
    j *= n
    k.append(j)
print("n natural sonining n ta haqiqiy sonlar bilan ko'paytmasi:", k)
'''
'''
#series 10
numbers = [-17, -8, -13, -23, -11, -5]
for i in range(len(numbers)):
    if numbers[i] > 0:
        print(True)
else:
    print(False)
'''
'''
#series 11
numbers = [17, 8, 13, 23, 11, 5]
k = int(input('k ni kiriting: '))
for i in numbers:
    if i < k:
        print(True)


else:
        print(False)
'''
'''
#string 42
words = "QATTIQ KATAK LOLA SHAHAR ALLA"
s = words.split()
n = 0
new = []
for i in s:
    if i[0] == i[-1]:
        n += 1
print("bir xil harf bilan boshlanuvchi va tugovchi so'zlar soni: ", n, "ta")
'''    
'''   
#string 43
words = "RUCHKA GUL KOMPYUTER OLMA"
#d = words.replace(" ", '')
print(words.find('A'))
'''
'''
#string 46
words = "ruchka gul daraxt olma uzunlik"
s = words.split()
d = max((s), key=len)
print(f"eng uzun so'z: {d}\n uning uzunligi:{len(d)}")
'''
'''
#string 47
words = "ruchka gul daraxt olma uzunlik"
d = words.replace(" ", ".")
print(d)
'''   
'''
#string 57
words = '  ruchka   gul  daraxt   olma    uzunlik'
d = (words.split())
s = " ".join(d)
print(s)
'''



'''
#homework 1
l = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
s = []
for i in l:
    if type(i) == int or type(i) == float:
        s.append(i)
print('listdagi eng katta son bu:', max(s))
'''

'''
#homework 2
list =  [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
s +=1
d = max(set(list), key = list.count, s)
print('listda eng kop takrorlangan son:', d)
print(s)
'''

password = input('parolni kiriting: ')
#s = 0
#d = 0
#m = 0
for i in password:
    if i.isdigit():
        print(password.replace(i, 'o')) 





hdunileulcbipusnc
        
        #s += 1
    #elif i.isalpha() and i.isupper():
       # d += 1
    #else:
        #i.isalpha() and i.islower()
        #m += 1
#print('raqamlar soni:', s, 'ta;', 'katta harflar soni:', d, 'ta;', 'kichik harflar soni:', m, 'ta')










































































