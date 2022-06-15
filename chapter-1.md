# Chapter 1: Finite Fields

## Finite Field Definition

Mathematically, a finite field is defined as a finite set of numbers and two operations + and * that satisfy the following:

1. If a and b are in the set, a+b and a*b are in the set. We call this property closed.
2. 0 exists and has the property a+0=a. We call this the additive identity.
3. 1 exists and has the property a*1=a. We call this the multiplicative identity.
4. If a is in the set, -a is in the set, which is defined as the value that makes a+(-a)=0. This is what we call the additive inverse.
5. If a is in the set and is not 0, a^(-1) is in the set, which is defined as the value that makes a*a^(-1)=1. This is what we call the multiplicative inverse.

We have a set of numbers that's finite. Because the set is finite, we can designate a number `p`, which is how big the set it. This is what we call the order of the set. 

## Definining Finite Sets

If the order (or size) of the set is p, we can call the elements of the set, 0, 1, 2,..., p-1. These numbers are what we call the elements of the set.

**Exercise 1**

Write the corresponding method `__ne__`, which checks if two `FieldElement` objects are not equal to each other.

```python
def __ne__(self, other):
    equal = self.__eq__(other)
    return (not equal)
```

## Module Arithmetic

## Module Arithmetic in Python

## Finite Field Addition and Subtraction

**Exercise 2**

- `44 + 33` -> 20
- `9 - 29` -> 37
- `17+42+49` -> 51
- `52-30-38` -> 41

**Exercise 5**

All the same resulting sets

Why Fields are Prime

The answer to Exercise 5 is why fields have to have a prime power number of elements. No matter what k you choose, as long as it's greater than 0, multiplying the entire set by k will results in the same set as you started with.

Intuitively, the fact that we have a prime order results in every element of a finite field equivalent. If the order of the set was a composite number, multiplying the set by one of the divisors would result in a smaller set. 

Why don't we force the exponent to be a FieldElement object? It turns out that the exponent doesn't have to be a member of the finite field for the math to work. In fact, if it were, the exponents wouldn't display the intuitive behavior we expect, like being able to add the exponents when we multiple with the same base.

## Finite Field Division

