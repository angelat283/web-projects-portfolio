# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python lab1/test_lab1.py
#
# Author: Angel Suleiman
# Student Number: 152961231ß

def wins_rock_scissors_paper(player, opponent):
    # normalize case
    player = player.lower()
    opponent = opponent.lower()

    if player == opponent:
        return False

    if (player == "rock" and opponent == "scissors") or \
       (player == "scissors" and opponent == "paper") or \
       (player == "paper" and opponent == "rock"):
        return True

    return False


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def sum_to_goal(numbers, goal):
    seen = set()
    for num in numbers:
        diff = goal - num
        if diff in seen:
            return num * diff
        seen.add(num)
    return 0


class UpCounter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step

    def count(self):
        return self.value

    def update(self):
        self.value += self.step


class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step
