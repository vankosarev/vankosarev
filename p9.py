import array,random
pribil = []

mesiki = ["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
    
def genPribil(index):
    while index > 0:
            pribil.insert(index,random.randint(10000,20000))
            index = index - 1
    print("прибыль за какждый месяц", pribil)        
    

def maxPribil():
    print("максимальная приыль за год:", max(pribil))

def sumPribil():
    print('сумма за год:',sum(pribil))

def maxPribilIndex(a,b):
    for i in pribil:
        while b < 12:
            if pribil[a] > pribil[b]:
                b = b + 1
            elif pribil[a] < pribil[b]:
                a = b
                b = b + 1
    print("большая прибыль в ",mesiki[a+1])
  
def sumPeriod(m1,m2):
    r = m2 - m1
    s = pribil[m1]
    for summa in range(0,r):
        l = m1 + 1
        s = s + pribil[l]
    print("сумма за период с ",mesiki[m1-1]," по ",mesiki[m2-1],': ',s)
   
genPribil(12)
maxPribil()
sumPribil()
maxPribilIndex(1,2)
  
vibor = input("1 - получить прибыль за период, 0 - закрыть.")

if vibor == "1":
    m1 = int(input("перый месяц"))
    m2 = int(input("последний месяц"))
    sumPeriod(m1,m2)
