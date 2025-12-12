### **Purpose of each file:**

\- game.py: runs the game  
\- cards.py: creates card object and a deck of random cards  
\- players.py: creates player object  
\- initial\_guess\_phase.py: deals the cards to each player and has them guess for each card  
\- pyramid\_matching.py: constructs 5 row pyramid and has player match cards they have on hand in each row  
\- riding\_the\_bus.py: player with the lowest points is decided and has chances to gain points depending on card flipped

### **How to run program:**

To run the program, run the command *python game.py* followed by at least two name arguments.

Required Arguments:  
Player1 (str) \- name of first player   
Player2 (str) \- name of second player

Optional Arguments:  
	Player3 (str) \- name of additional players

Example Command:  
	*python game.py Elena Jane*

### **How to use program:**

Throughout each phase of the game, the program will prompt the user with different questions. This section explains what questions the player will be asked and what answers are expected.

**Phase 1: Initial Guessing Phase**   
For the first phase, a series of questions will be asked about the characteristics of the drawn cards. Here are the questions in the order that they appear.

Question 1: Is the card red or black?   
The player can respond with “r” for red or “b” for black.

Question 2: Is the new card higher or lower than the previous card?  
The player can respond with “h” for higher and “l” for lower.

Question 3: Is the new card drawn inside or outside the two cards?  
The player can respond with “i” for inside and “o” for outside.

Question 4: What suite is the new card?   
The player can respond with “Hearts”, “Diamonds”, “Clubs”, or “Spades”. The answer choices for this are not case sensitive.

**Phase 2: Pyramid Round**  
The second phase consists of players matching their hand of cards with cards in each row of a card pyramid. The player will be asked multiple questions consisting of the following:

Question 1: Do you want to match a card in this row?   
The player can respond with “y” for yes and “n” for no. If no input is entered and the player presses “Enter”, the program will automatically use the default value, no.

Question 2: Which card do you want to match?   
The user can respond by entering the number that corresponds to the card the player wants to use. 

Question 3: Do you want to match another card in this row?   
The user can respond with “y” for yes and “n” for no.

**Phase 3: Ride the Bus**  
In the last round the player will ask the player to choose 3 cards numbered between 1-10 with a chance of gaining more points. 

Question: Pick a card (1-10).   
The player will respond with a number between 1 and 10.Points will be awarded if face cards are selected. 

### **Attributes Table:**

| Method/Function | Primary Author | Techniques |
| :---- | :---- | :---- |
| Choice function | Adela Wallis | Optional parameters |
| Pyramid\_round function | Adela Wallis | Sequence unpacking |
| bus\_player function | Carlos Miranda | List comprehension |
| ride\_the\_bus function | Carlos Miranda | Iteration |
| \_\_init\_\_  (Card class) | Ayah Hamouda | Attributes |
| add\_score | Ayah Hamouda | Compound assignment operator |
| str, repr | Ranjith Mahendran | Magic methods  |
| guesses  | Ranjith Mahendran | Conditional expressions  |
| parse\_args | Ranjith Mahendran | ArgumentParser class |

### **Annotated Bibliography:**

Kobler, F. (2025, November 24). *How to play ride the bus: Official Drinking Game Rules*. wikiHow. https://www.wikihow.com/Play-Ride-the-Bus. This is the wiki page for the drinking game “Ride the Bus”. This site provided in-depth, step by step instructions on how to play the game. It also provided an alternative option for the last round, which gave us inspiration for our version of the last phase of the game. 
