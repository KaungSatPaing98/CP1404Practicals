import random
quick_picks = int(input("How many quick picks? "))
for random_number in range(quick_picks):
    numbers = sorted(random.sample(range(1, 46), 6))
    print("{:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(*numbers))
