#GPA2
num = int(input())
prime = [2]

#finding the prime numbers from 3 to given input and appending it in prime list
for i in range(3,num,2):
  flag = True
  for j in range(2,i):
    if i%j == 0:
      flag = False
      break
  if flag:
    prime.append(i)

#checking the primes are divisible by given input
flag = False
for i in prime:
  if num%i == 0:
    flag = True
    print(i)

#If no prime factors are there, the given input is getting printed
if not flag:
  print(num)
