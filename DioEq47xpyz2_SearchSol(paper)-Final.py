import math
def is_prime(num):
    if num==2 or num==3: return True
    if num%2==0 or num<2: return False
    r = int(num**0.5)
    for i in range(3,r+1,2):
        if num%i == 0: return False
    return True
def is_perfect_square(num):
    if num < 0:return False
    sq_root = math.isqrt(num)
    return sq_root**2 == num
def satisfy_main_theorem(p,x,y,z):
    solution = p,x,y,z
    if solution in [(2,0,2,0)]:
        return True #Solution satisfies Theorem (i)
    elif (x>=5 and x%2==1 and y%4==1 and (z%16 in [3,5,11,13]) or
        x>=5 and x%2==1 and y%4==3 and (z%16 in [1,7,9,15]) or
        solution in [(3,0,1,1),(3,1,1,5),(3,1,3,1),(3,2,3,13),(3,3,1,37)]):
        return True #Solution satisfies Theorem (ii)
    elif 5<=p<=17:
        return False #Solution does not satisfy Theorem (iii)
    elif (x%2==1 and y%2==1 and (z%24 in [3,9,15,21])):
        return True #Solution satisfies Theorem (iv)
    return False #Solution does not satisfy Theorem
def satisfy_corollary(p,x,y,z):
    if z%24 in [3,9,15,21]:
        if x%6==1:
            if y%6==3 and p%24==19:
                #Solution satisfies Corollary with p mod 24 = 19
                return True
            elif y%6==1 and p%72==19:
                #Solution satisfies Corollary with p mod 72 = 19
                return True
            elif y%6==5 and p%72==19:
                #Solution satisfies Corollary with p mod 72 = 19
                return True
        elif x%6==3:
            if y%6==5 and p%72==43:
                #Solution satisfies Corollary with p mod 72 = 43
                return True
            elif y%6==1 and p%72==67:
                #Solution satisfies Corollary with p mod 72 = 67
                return True
        elif x%6==5:
            if y%6==5 and p%72==67:
                #Solution satisfies Corollary with p mod 72 = 67
                return True
            elif y%6==1 and p%72==43:
                #Solution satisfies Corollary with p mod 72 = 43
                return True
    return False #Solution does not satisfy Corollary"
if __name__=='__main__':
    #### parameters ####
    prime_max = 100000
    x_max = 1000
    ####################
    primes = []
    for p in range(2,prime_max+1):
        if is_prime(p): primes.append(p)
    for p in primes:
        for x in range(1,x_max+1):
            y_max=math.floor(math.log(4*7**x,p))
            for y in range(1,y_max+1):
                z_squared  = 4*7**x-p**y
                if is_perfect_square(z_squared):
                    z = int(z_squared**0.5)
                    result_theorem = satisfy_main_theorem(p,x,y,z)
                    print(f"Solution {(p,x,y,z)} satisfies")
                    print(f"\tTheorem:{result_theorem}")
                    if p>=19:
                        result_corollary = satisfy_corollary(p,x,y,z)
                        print(f"\tCorollary:{result_corollary}")