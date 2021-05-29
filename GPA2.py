def GeneratePrimesFrom3toN(N):    
    primes =list()
    
    for i in range(3,N,2):
        Is_i_aPrme = True      
        for j in range(2,i):
            if i%j == 0:
                Is_i_aPrme = False
                break
        if Is_i_aPrme == True:
            primes.append(i)
    return primes

def PrintPrimeFactors(primes_list,number):
    IsPrimeFactorFound = False
    for primenumber in primes_list:
        if number%primenumber == 0:
            IsPrimeFactorFound = True
            print(primenumber)
    if IsPrimeFactorFound == False:
        print(number)

# equivalent to main function in c  
if __name__ == "__main__":
    num = int(input())
    PrimesFrom3ToN = GeneratePrimesFrom3toN(num)
    PrintPrimeFactors(PrimesFrom3ToN,num)
