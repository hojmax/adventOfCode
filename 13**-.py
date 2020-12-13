import time
startTime = time.time()

def inv(a, m) : 
      
    m0 = m 
    x0 = 0
    x1 = 1
  
    if (m == 1) : 
        return 0
  
    # Apply extended Euclid Algorithm 
    while (a > 1) : 
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process  
        # same as euclid's algo 
        m = a % m 
        a = t 
  
        t = x0 
  
        x0 = x1 - q * x0 
  
        x1 = t 
      
    # Make x1 positive 
    if (x1 < 0) : 
        x1 = x1 + m0 
  
    return x1 
  
# k is size of num[] and rem[].  
# Returns the smallest 
# number x such that: 
# x % num[0] = rem[0], 
# x % num[1] = rem[1], 
# .................. 
# x % num[k-2] = rem[k-1] 
# Assumption: Numbers in num[]  
# are pairwise coprime 
# (gcd for every pair is 1) 
def findMinX(num, rem, k) : 
      
    # Compute product of all numbers 
    prod = 1
    for i in range(0, k) : 
        prod = prod * num[i] 
  
    # Initialize result 
    result = 0
  
    # Apply above formula 
    for i in range(0,k): 
        pp = prod // num[i] 
        result = result + rem[i] * inv(pp, num[i]) * pp 
      
      
    return result % prod 
  
# Alt det ovenstående er stjålet fra nettet, det sidste her har jeg selv lavet for at få dag 13's input på den rigtige form
# Var et svært problem når man ikke kendte teorien, men reddit fortalte mig at der skulle søges på
# "Chinese Remainder Theorem"
# Det hjalp lidt
num = []
rem = []
combined = [[23, 0], [41, 13], [37, 17], [421, 23], [17, 40], [19, 42], [29, 52], [487, 54], [13, 67]]
for e in combined:
    num.append(e[0])
    rem.append((e[0]-e[1]%e[0]) % e[0])
k = len(num)
print( "x is " , findMinX(num, rem, k))

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
