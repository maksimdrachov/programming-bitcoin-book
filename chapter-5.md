# Chapter 5: Transactions

## Transaction Components

At a high level, a transaction really only has four components. They are:

1. Version
2. Inputs
3. Outputs
4. Locktime

The version indicates what additional features the transaction uses, inputs define what bitcoins are being spent, outputs define where the bitcoins are going, and locktime defines when this transaction starts being valid. 

The ScriptPubKey, like the ScriptSig, has to do with Bitcoin's smart contract language, Script. Think of the ScriptPubKey as the locked box that can only be opened by the holder of the key. It's like a one-way safe that can receive deposits from anyone, but can only be opened by the owner of the safe. 

## Locktime

Locktime is a way to time-delay a transaction. A transaction with a locktime of 600 000 cannot go into the blockchain until block 600 001. 

Note that locktime is ignored if the sequence numbers for every input are ffffffff.

The uses before BIP0065 were limited. BIP0065 introduced OP_CHECKLOCKTIMEVERIFY, which makes locktime more useful by making an output unspendable until a certain locktime.

