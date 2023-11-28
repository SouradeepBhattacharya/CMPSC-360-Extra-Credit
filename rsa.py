# -----------------------------------------------------------------------
# FA 23 CMPSC 360 Extra Credit Assignment
# RSA Implementation
# 
# Name: Souradeep Bhattacharya
# ID: skb6381@psu.edu
# 
# 
# You cannot use any external/built-in libraries to help compute gcd
# or modular inverse. You cannot use RSA, cryptography, or similar libs
# for this assignment.
# 
# -----------------------------------------------------------------------

from typing import Tuple

# Type defs
Key = Tuple[int, int]



def isprime(p: int) -> bool:
    '''
    Description: Checks if the input is a valid prime number
    Args: p (input integer)
    Returns: Bool
    '''
    y = (p)**(1/2)
    if p == 1:
        return False
    elif y == int(y):
        for i in range(2,int(y)+1):
            if p % i == 0:
                return False
        else:
            return True
    elif y != int(y):
        for j in range(2,int(y)+1):
            if p % j == 0:
                return False
        else:
            return True


def generate_keypair(p: int, q: int) -> Tuple[Key, Key]:
    '''
    Description: Generates the public and private key pair
    if p and q are distinct primes. Otherwise, raise a value error
    
    Args: p, q (input integers)

    Returns: Keypair in the form of (Pub Key, Private Key)
    PubKey = (n,e) and Private Key = (n,d)
    '''
    #When p and q are coprimes
    if gcd(p,q) == 1:
        n = p*q
        k = (p-1)*(q-1)
        e = generate_public_exponent(k)
        d = modular_inverse(e,k)
        public_key = tuple([n,e]) #Tuple[n,e]
        private_key = tuple([n,d]) #Tuple[n,d]

    else:
        return f"ERROR! {p} and {q} are not co-primes"

    return tuple([public_key, private_key])


def generate_public_exponent(k: int) -> int:
    '''
    Description: Helper function that generates the SMALLEST
    public exponent for a given k value.

    Args: k (integer)

    Returns: e (public exponent)
    '''
    #gcd(e,k) = 1
    potential = {}
    for e in range(2,k):
        potential[e] = gcd(e,k)

    gcd_1 = [i for i in potential if potential[i] == 1]

    gcd_1.sort()
    return gcd_1[0]


def gcd(x: int, y: int) -> int:
    '''
    Description: Helper function to compute gcd of two integers
    Args: x and y 
    Returns: gcd(x,y)

    NOTE: You CANNOT use math.gcd or any other function. You need to
    implement the algorithm yourself.
    '''
    factors_x = primefactorization([],x)
    factors_y = primefactorization([],y)
    
    counts_x = {factor: factors_x.count(factor) for factor in factors_x}
    counts_y = {factor: factors_y.count(factor) for factor in factors_y}

    #common factors:
    gcd_factors = []
    for factor in list(set(factors_x)&set(factors_y)):
        min_count = min(counts_x[factor], counts_y[factor])
        gcd_factors.extend([factor] * min_count)

    #gcd:
    value = 1
    for n in gcd_factors:
        value = value*n

    return value

#helper function for the gcd function
def primefactorization(l:list, x: int) -> list:
    
    if isprime(x):
        a = [i for i in l]
        a.append(x)
        x = x//x
    else:
        a = [i for i in l]
        for i in range(2,x):
            while x%i != 0:
                i+=1
            if x%i == 0:
                x = x//i
                a.append(i)
                break

    while x != 1:
        return primefactorization(a,x)
    if x == 1:
        pass
    return a    


def modular_inverse(a: int, n: int) -> int:
    '''
    Description: Helper function to compute the modular inverse
    of a with respect to n
    Args: a (integer), n (modulus)
    Returns: a^(-1)modn

    Examples:
    modular_inverse(3,10) = 7
    modular_inverse(2,5) = 3

    NOTE: You CANNOT use the pow function (or any other function) 
    for computing modular inverse. Implement the algorithm yourself.

    '''
    if a >= n:
        return f"{a} is greater than {n}. Not Possible!"
    
    if gcd(a,n) != 1:
        return f"Error! For the modular inverse, the gcd({a},{n}) has to be 1. \nBut, gcd({a},{n}) = {gcd(a,n)} "

    #When everything is right
    inverses = []
    for i in range(n):
        p = a*i
        r = p%n
        if r == 1:
            inverses.append(i)

    for j in inverses:
        if len(inverses) > 1:
            inverses.sort()
            return inverses[0]

        else:
            return j


def mod_exp(base: int, exp: int, mod: int) -> int:
    '''
    Description: Helper function for modular exponentiation
    Args: base (integer), exp (exponent), mod (modulus)
    Return: v (result of mod exponentiation)
    '''
    #Fermat's Little Theorem 
    if exp > mod and isprime(mod) and gcd(base,mod) == 1:
        return fermats_little_theorem(base,exp,mod)
    
    #If exp is less than mod
    # -- Binary Expansion of Exponent helps
    else:    
        exp_split = binary_factor(exp)
        mod_split = []
        for i in exp_split:
            mod_split.append((base**i)%mod)

        modulo = 1
        for j in mod_split:
            modulo *= j

        result = modulo%mod
        return result

#Helper functions for the mod_exp function
def binary_factor(a: int) -> list:
    input_value = [a]
    remainder = []
    r = a%2
    q = a//2
    remainder.append(r)
    while q != 0:
        r = q%2
        q = q//2
        remainder.append(r)
    if q == 0:
        remainder
    
    dictionary = {}
    for j in range(len(remainder)):
        dictionary[j] = remainder[j]

    values_list = []
    for keys, values in dictionary.items():
        values_list.append(values*(2**keys))
    
    return values_list

#Helper functions for the mod_exp function
def fermats_little_theorem(base:int, exp:int, mod:int):
    p = mod-1
    factorize = []
    r = exp%p
    q = exp//p
    factorize.append(q)
    factorize.append(r)
    
    result = ((base**r))%mod
    
    return result



def rsa_encrypt(m: int, pub_key: Key) -> int:
    '''
    Description: Encrypts the message with the given public
    key using the RSA algorithm.

    Args: m (positive integer input)

    Returns: c (encrypted cipher)
    NOTE: You CANNOT use the pow function (or any similar function)
    here.
    '''
    n = pub_key[0]
    e = pub_key[1]

    if m < n:
        c = mod_exp(m,e,n)
        return c

    elif m>= n:
        return f"Your input {m} cannot be greater than the modulus {n}"

    

def rsa_decrypt(c: int, priv_key: Key) -> int:
    '''
    Description: Decrypts the ciphertext using the private key
    according to RSA algorithm

    Args: c (encrypted cipher)

    Returns: m (decrypted message, an integer)
    NOTE: You CANNOT use the pow function (or any similar function)
    here.
    '''
    n = priv_key[0]
    d = priv_key[1]

    if c < n:
        m = mod_exp(c,d,n)
        return m
    
    elif c>= n:
        return f"Your input {c} cannot be greater than the modulus {n}"



if __name__ == '__main__':
    a = generate_keypair(3,11)
    pub_key = a[0]
    b = rsa_encrypt(42,pub_key)
    print("The encrypted message is: ",b)

    priv_key = a[1]
    c = rsa_decrypt(b,priv_key)
    print("The decrypted message is: ",c)