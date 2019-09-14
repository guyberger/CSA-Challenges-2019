# Prince of Persia
## Introduction
The challenge uses a modified version of the original SDL-PoP game found [here](https://github.com/NagyD/SDLPoP).
## Getting started
The first thing we notice if we try to play the game is that it's upside down.
This already indicates that we should expect modifications in the game to make it either harder to win or simply because why not?
To change some basic settings we should follow the instructions provided in the doc/readme file.
(For example changing upside-down settings in SDL-POP.ini).

Since we are told to reach the reach the end, the fastest way to do it is to run the game using cheats straight to the winning level (14):
```
./prince megahit 14
```
After finishing this level we get a messege that clearly is not part of the original game:
> Great: 'some random chars'

Well, we certainly found something, but what?
Note for later use: the box displaying the messege in the game has the string
> Press any key to continue

We will use it in the next part of the solution.

## Reversing
Firstly we want to find out what happens in the code when we reach the end and get the messege.
To do that we can use one of two ways:
1. Using gdb we can put breakpoints and move ourselves in the code until we reach the messge at the end of level 14, to find out which function is called to print the messege.
2. Using IDA.

Explaining method 2:
I opened 'prince' in IDA and I first tried to search for the string 'Great', no results. That hints that the string is probably encoded somehow in the code.
Next I searched for 'Press any key to continue" and found the exact location in the code of that string, yay!
The string is printed out inside a function called "check_the_end", so this is a good place to continue digging.

### check_the_end
Since we have the source files, we can run the command 
```
grep -rlw "./" -e "check_the_end"
```
to find the file containing the function, which we find is seg000.c.
Here we spot a couple of interesting things:
1. Some weird for loop used to modify 'str'.
2. RC method called to generate the ciphertext which is printed.
3. Some kind of array called "rooms".

After examining the for loop we can deduce that it basically doesn't modify 'str' at all. 
My first attempt was to try and print the plaintext ('str') instead of the ciphertext by changing the printf line to:
```
printf("%s\n", str);
```
but we get random chars again.

So remembering the hint we are provided
> "... Little does it know that he is already a prisoner in Jaffar's dungeons..."

I figured the flag probably is a combination of some information throughout the game.
The RC is a function that is implemented over 3 files (using submethods 'KSA', 'PRGA') and is an implementation of the RC4 encryption.
The RC4 encryption uses a key to generate the ciphertext and in our implementation the key provided is the array 'rooms', so naturally that's what we want to investigate next.

### rooms
Using the 'grep' command again we find the following code line in src/seg006.c:
```
rooms[current_level - 1] = curr_room;
```
Bingo! looks like we can have a try in filling the array.
This code line appears under a 'case' in the event of ending a level. 
It is safe to assume we would like to fill the array with room numbers of the rooms from which we finish a level.

To find the rooms quickly we can use the cheat commands
```
c: show numbers of current and adjacent rooms
Shift-C: show numbers of diagonally adjacent rooms
h: look at room to the left
j: look at room to the right
u: look at room above
n: look at room below
```
to navigate through rooms and see the room numbers, and the command
```
Shift-L
```
to go to the next level, and finish filling the array.

## Finishing up
Once we have filled the array we can finish level 14 again and see the correct flag which was egenerated using RC method with the right "rooms" array as key.

## Code
Note: I couldn't decide which room numbers are supposed to be taken in the 2 falling levels so I brute forced these two.
For the solution I created a copy of the RC method in python (without loss of functionality).

### Flag:
> CSA{<3_4nd_Th3y_L1VeD_HapPiLy_Ev3r_Af7eR_<3}








