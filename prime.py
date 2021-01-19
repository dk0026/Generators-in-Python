def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def primeGenerator(n):
    num=2
    while n:
        if isPrime(num):
            yield num
            n-=1
        num+=1
    return

it = primeGenerator(20)
for e in it:
    print(e,end=' ')

#file handeling
def fileHandle():
    file = open("sample.txt","r")
    content = file.readlines()
    for line in content:
        print(line)
fileHandle()