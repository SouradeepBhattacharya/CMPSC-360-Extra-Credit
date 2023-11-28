# CMPSC-360-Extra-Credit
## 1 Base Conversion
In the first part of the assignment, you will implement the base conversion(number, base)
function which takes two inputs: an integer number and a base (ranging from 2 to 9), and returns the
conversion of the input number from the input base to base 10. Your function should be capable of
checking whether the inputs are reasonable. If the digits of the input number are greater than or equal
to the base, it should return an error message: ’The input is wrong. Digits should
be less than the base.’
You are not permitted to use built-in functions for base conversion.
Here are some examples of input and output for the function:

_BaseConversion(345, 7)_
_Output: 180_

_BaseConversion(239, 9)_
_Output: ’The input is wrong. Digits should be less than the base.’_

## 2 RSA Implementation
In this part of the assignment, you will implement the RSA algorithm in Python. You will learn how
modular arithmetic can be leveraged to enforce security in a PKI system. Unlike the shift cipher
you’ve encountered in class, RSA employs an asymmetric key encryption technique. This means
that the encryption key used to secure a message is different from the decryption key, which is kept
confidential and known only to the intended recipient. The computational hardness of this algorithm
is prime factorization. To decrypt the messages, an adversary needs to recover the prime numbers
p and q from the common modulus n = p ∗ q. While this is far more secure than a symmetric key
encryption technique like the shift cipher, there are many known vulnerabilities in RSA.
