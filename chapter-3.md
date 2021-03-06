# Chapter 3: Elliptic Curvers over Finite Fields

## Scalar Multiplication for Elliptic Curves

One property of scalar multiplication is that it's really hard to predict without calculating.

Each point is labeled by how many times we've added the point. You can see that this is a complete scattershot. This is because point addition is nonlinear and not easy to calculate. Performing scalar multiplication is straightforward, but doing the opposite, point division, is not.

This is called the discrete log problem and is the basis of elliptic curve cryptography.

Another property of scalar multiplication is that at a certain multiple, we get to the point at infinity (remember, the point at infinity is the additive identity or 0). If we imagine a point G and scalar-multiply until we get the point at infinity, we end up with a set.

It turns out that this set is called a group, and because n is finite, we have a finite group (or more specifically, a finite cyclic group). Groups are interesting mathematically because they behave well with respect to addition.

When we combine the fact that scalar multiplication is easy to do in one direction but hard in the other and the mathematical properties of a group, we have exactly what we need for elliptic curve cryptography.

### Mathematical Groups

The preceding math (finite fields, elliptic curves, combining the two) was really to bring us to this point. What we actually want to generate for the purposes of public key cryptography are finite cyclic groups, and it turns out that if we take a generator point from an elliptic curve over a finite field, we can generate a finite cyclic group.

Unlike fields, groups have only a single operation. In our case, point addition is the operation. Groups also have a few other properties, like closure, invertibility, commutativity, and associativity. Lastly, we need the identity.

### Exercise 5

Order is 7

## Defining the Curve for Bitcoin

While we've been using relatively small primes for the sake of examples, we are not restricted to such small numbers. Small primes mean that we can use a compiler to search through the entire group. If the group has a size of 301, the computer can easily do 301 computations to reverse scalar multiplication or break discrete log.

An elliptic curve for public key cryptography is defined with the following parameters:

- We specify the a and b of the curve 
- We specify the prime of the finite field, `p`
- We specify the x and y coordinates of the generator point G
- We specify the order of the group generated by G, n

There are a few thing to notice about this curve. First, the equation is relatively simple. Many curves have a and b values that are much bigger.

Second, p is extremely close to 2**256. This means that most numbers under 2^256 are in the prime field, and thus any point on the curve has x and y coordinates that are expressible in 256 bits each. n is also very close to 2^256. This means any scalar multiple can also be expressed in 256 bits.

Third, 2^256 is a huge number. Amazingly, any number below 2^256 can be stored in 32 bytes. This means that we can store the private key relatively easy.

## Public Key Cryptography

At last, we have the tools that we need to do public key cryptography operations. The key operation that we need is P = eG, which is an asymmetric equation. We can easily compute P when we know e and G, but we cannot easily compute e when we know P and G. This is the discrete log problem described earlier. 

Generally, we call e the private key and P the public key. Note that the private key is a single 256 bit number and the public key is a coordinate (x, y), where x and y are each 256 bit numbers.

## Inscribing the Target

The inscribing of the target depends on the signature algorithm, and in our case that algorithm is called the Elliptic Curve Digital Signature Algorithm, or ECDSA

The secret in our case is e satisfying the following:

eG = P

where P is the public key and e is the private key

The target that we're going to aim at is a random 256-bit number, k. 

kG = R

R is now the target that we're aiming for. In fact, we're only going to care about the x coordinate of R, which we'll call r. You may have guessed that r here stands for random.

We claim at this point that the following equation is equivalent to the discrete log problem:

uG + vP = kG

where k was chosen randomly, u,v != 0 can be chosen by the signer, and G and P are known. 

To wit, here are the steps:

1. We are given (r, s) as the signature, z as the hash of the thing being signed, and P as the public key (or public point) of the signer.
2. We calculate u = z/s, v =r/s
3. We calculate uG + vP = R
4. If R's coordinate equals r, the signature is valid.

Given that we know how verification should work, signing is straightforward. The only missing step is figuring out what k, and thus R = kG to use. We do this by choosing a random k.

The signing procedure is as follows:

1. We are given z and know e such that eG = P
2. Choose a random k
3. Calculate R = kG and r = coordinate of R
4. Calculate s = (z-re)/k
5. Signature is (r, s)

