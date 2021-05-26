#GPA2

def FindingPrimeNumbersFrom3toN(N):
    listofprimes = list()
    for i in range(3,num,2):
        flag = True
        for j in range(2,i):
            if i%j == 0:
                flag = False
                break
            if flag:
                listofprimes.append(i)
    return listofprimes


def PrintPrimeFactors(primes_list,number):
    IsPrimeFactorFound = False  #always use a question for booleans. Easy to understand
    for primenumber in primes_list:
        if num%primenumber == 0:
            IsPrimeFactorFound = True
            print(primenumber)
    if IsPrimeFactorFound == FALSE:
        print(num)
  
  

# equivalent to main function in c  
if __name__ == "__main__":

    num = int(input())
    primenumbers_list = FindingPrimeNumbersFrom3toN(num)
    PrintPrimeFactors(primenumbers_list,num)

 
