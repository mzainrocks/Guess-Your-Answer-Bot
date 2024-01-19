import random
import string
import time

characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
target = input("Enter the answer you want me to guess: ")

guessedanswer = False
guessfirst = ''.join(random.choice(characters) for i in range(len(target)))
guessnext = ''
count = 0

while guessedanswer==False:
    print(guessfirst)
    guessnext= ''
    guessedanswer= True
    for i in range(len(target)):
        if guessfirst[i] !=target[i]:
            guessedanswer = False
            guessnext += random.choice(characters)
        else:
            guessnext += target[i]
    count += 1
    guessfirst = guessnext
    time.sleep(0.1)

print("Guessed your answer! That took " + str(count) + " tries ;)")
