-+-+-+-+-+-+-+-+-+-+

Game Assignment

The game is based on a guessing game of dices. It's created so that the user can enter a number between 1-6 to try and guess the value of two seperate dices.
The program is specifically designed to accept only values from 1-6 or else the program breaks. If the user answers the value of each dice correctly, the player will get a winning message and if not, the player recieves a losing message. The algorithm behind it is as follows. 

~ First we summon the graphics.py library, which is used to do shapes, fill in shapes, and shapes with colors. Then, we add the random library so that the computer can generate a random number or numbers. 

~ We assign the rectangle (dice), its size, and its color and let the computer draw the dice.
~ We do the same with the dots insie each dice, depending on the user's input (1-6) on the first dice. If the user's first input is 4, it will draw four dots, if it's 6 it will draw 6 dots and so on. Next step is repeating the same process but with the input of the second dice. 

~ There's a line of code that is placed that the user licks on the dice to make them roll and see if they answered correctly. 
~ We add an exception on the code which prohibids the user from entering a number thats is NOT between 1-6. If so, the program breaks. 

Also, in addition, there's a different message for each result of the game as mentioned above. Winner message if guessed correctly and losing message if not answered correctly. After that, the code ends and the game will now close.

-+-+-+-+-+-+-+-+-+-+
