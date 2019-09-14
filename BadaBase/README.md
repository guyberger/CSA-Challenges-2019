# BadaBase

Looking at the end of the cyphertext we have '=='.
Base64 padding is '=' and after examining the text we can see that all the characters indeed fit to the base64 char set.

The description of the challenge says 
> "The king of Sheshach shall drink after them"

A quick [Wikipedia](https://en.wikipedia.org/wiki/Sheshach) search will show you that the phrase is connected to the Atbash cypher.

Following these pieces of information we can get the original text by using Atbash decryption where the alphabet is base64 encoding alphabet.

### Flag:
> C.S.A. (2019)-Rulz-{<@!*~*!@>} A.S.C.
