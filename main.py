'''
Basic question and answer thing that you can run on the terminal.

relatively easy to change the questions and answer
Just write the questions in the questions dictionary by following basic dicitionary methods
Then in the answers dictionary, just write the answers.

Some say this looks tedious and less efficient than something like Anki or Quizlet, but its not too bad if you can type fast. Can be used by non-coders just by changing like this example

questions = {
    0: "Who is the dumbest person in the world",
    1:"Who is the smartest person in the world"
    }
    

answers = {
    "Who is the dumbest person in the world": "me",
    "Who is the smartest person in the world": "not me"
    }
Just change the question next to the number and colon, and copy paste it in the answer then write colon then answer.

Of course no non-coder is going to know a single thing about dictionaries, and advanced programmers be like bro we know this better than you, but yeah.....

'''

import random


numbq = list(range(2))
y = len(numbq)
points = 0

questions = {
    0: "What is the closest planet to the sun",
    1:"What is the only known planet to harbor life"
    }
    

answers = {
    "What is the closest planet to the sun": "Mercury",
    "What is the only known planet to harbor life": "Earth"
    }
qnumb = random.choice(numbq)
'''
First choose the question number that relates to the question
search that question in the answers bank
write your answer
if answer match = True

'''
x = len(numbq)
while x > 0:
    chosen = random.choice(numbq)
    numbq.remove(chosen)
    question = questions[chosen]
    answer = answers[question]
    print(question)
    my = input("Enter your Answer: ")
    if my == answer:
        print("True")
        points+=1
    else:
        print("False")
    x-=1
percentage = ((points/y)*100)
print(percentage)
if percentage >= 60:
    print("You passed")
else:
    print("You failed")
