# Chapter 2: Elliptic Curves

Elliptic curves are useful because of something called point addition. Point addition is where we can do an operation on two of the points on the curve and get a third point also on the curve. This is called addition because the operation has a lot of the intuitions we associate with the mathematical operation of addition. 

One of the properties that we are going to use is that point addittion is not easily predictable. We can calculate point addition easily enough with a formule, but intuitively, the result of point addition can be almost anywhere given two points on the curve. In mathematics parlance, point addition is nonlinear.

### Math of Point Addition

Point addition satisfies certain properties that we associate with addition, such as:

- Identity
- Commutativity
- Associativity
- Invertibility

To code point addition, we're going to split it up into three steps:

1. Where the points are in a veritcal line or using the identity point
2. Where the points are not in a vertical line, but are different
3. Where the two points are the same

Coding Point Addition

