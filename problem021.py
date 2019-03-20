def iternums(max):
    sum = 0
    for i in range(1,max+1):
        if check_amic(i):
            print(i)
            sum += i
    return sum

def check_amic(num):
    pair = sumfac(num)
    return num == sumfac(pair) and pair != num

def sumfac(num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum += i
    return sum

if __name__ == "__main__":
    print(iternums(9999))

