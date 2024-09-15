Project _1
In this assignment, you will develop a basic calculator program using Python. This project
will reinforce fundamental programming concepts including functions, user input,
conditional statements, and error handling. The application will run in the terminal and
should not use any external libraries or frameworks.


TASKS:
1. Function Definitions: Implement functions for the following operations: addition,
subtraction, multiplication, division, and modulus. Each function should take two
arguments, perform the corresponding operation, and return the result.
2. Implement User Input Handling: Prompt the user to select an operation( e.g. 1
for Add, 2 for Subtract, 3 for Multiply, 4 for Divide and 5 for Modulus) and input two
numbers. Convert these inputs into appropriate data types for calculations.
3. Conditional Logic: Use ‘if’, ‘elif’, and ‘else’ statements to determine which
arithmetic operation to perform based on user selection.
4. Output Formatting: Display the results in a clear and readable format. Examples:
Addition: 5 + 6 = 11
Division: 5 / 2 = 2.50
5. Error Handling: Include checks to handle division by zero and other potential
errors. Provide informative error messages to guide the user.


SAMPLE INPUT OUTPUT:
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
Enter choice (1/2/3/4/5): 1
Enter first number: 5
Enter second number: 8
5.0 + 8.0 = 13.0
------------------------------------------------------------------
#Project 2: Number Guessing Game


OVERVIEW
In this assignment, you will create a CLI-based Number Guessing Game using Python. The
objective of this project is to design an interactive game where the computer selects a
random number between 1 and 100, and the user attempts to guess it. Your program will
need to generate a random number, handle user input, and provide feedback based on the
user's guesses.


TASKS
1. Random Number Generation: Begin by generating a random number within the
range of 1 to 100. This number will serve as the target that the user needs to guess.
The random number should be kept secret from the user until they correctly guess it.
2. Implement User Input Handling: Prompt the user to input their guess and ensure
the input is converted to an integer to compare it with the randomly generated
number. Handle any potential input errors.
3. Loops: Utilize a loop to continuously prompt the user for their guess until they
correctly identify the number. This loop should repeat until the user's guess matches
the randomly selected number, allowing them to keep guessing as many times as
needed.
4. Conditional Logic: After each guess, provide feedback to the user on whether their
guess is too high, too low, or correct. Use conditional logic to compare the user's
guess with the random number and determine which of the three possible outcomes
applies. This feedback should guide the user towards the correct answer.
5. Ending the Game: Once the user successfully guesses the number, conclude the
game by printing a congratulatory message. Additionally, inform the user of the
number of attempts it took them to guess the number correctly. This helps in
providing a sense of achievement and closure to the game.


SAMPLE INPUT OUTPUT:
Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.


Enter your guess: 50
Too low!


Enter your guess: 75
Too high!


Enter your guess: 62
Too low!


Enter your guess: 68
Congratulations! You've guessed the number in 4 attempts.


NOTE:
1. Ensure the program can handle invalid inputs, such as non-numeric values, gracefully.
2. Implement meaningful error messages for invalid operations, such as division by zero.