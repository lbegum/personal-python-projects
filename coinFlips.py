import random

print('I will flip a coin 1000 times. \
Guess how many times it will come up heads. \
(Guess to begin)')
guess = input("Choose a number between 0 and 1000: ")
guess_list = list(map(str, range(0, 1001)))
while guess not in guess_list:
    guess = input("Choose a number between 0 and 1000: ")
int_g = int(guess)

flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 flips and there have been ' + \
            str(heads) + ' heads.')
    if flips == 100:
        print('At 100 tosses, heads has come up ' + \
            str(heads) + ' times so far.')
    if flips == 500:
        print('Halfway done, and heads has come up ' + \
            str(heads) + ' times.')

print()
print(f'Out of 1000 coin tosses, heads came up {heads} times!')
print(f"Your guess of {guess} was off by {abs(int_g - heads)}!")
if abs(int_g - heads) < 10:
    print("Wow! That was close!")
else:
    print("Better luck next time!")

