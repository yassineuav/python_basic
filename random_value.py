import random
import string

letters_digits = string.ascii_letters + string.digits 


print(random.random())
print(random.randint(1, 100))


print(random.choice(range(1, 10)))
print(random.choices("abcdefghilmnkptsqwzxy", k=4))
print("".join(random.choices(string.printable, k=8)))
