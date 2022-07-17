import random

x = int(random.randint(-100,100))
y = int(random.randint(-100,100))


def reshenie():
    print(x," * ",y ,"=")
    ans = int(input('Введите ответ:'))

    primer = x * y

    if ans == primer:        
        print('красава')

    else:
        print(primer)
 
pos1 = input("1 - получить пример, 0 - выйти:")

while pos1 == "1":
    reshenie()
    pos1 = input("1 - получить пример, 0 - выйти:")
    x = int(random.randint(1,100))
    y = int(random.randint(1,100))



