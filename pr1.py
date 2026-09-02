## First mini project

import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
chars = "!@#$%^&*()_+"
all = lower + upper + number + chars

length = 12

password = "".join(random.sample(all, length))
print("Your password is: " + password)