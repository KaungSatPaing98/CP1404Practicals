for i in range(1, 21, 2):
    print(i, end=' ')
print()

for a in range(0, 101, 10):
    print(a, end=' ')
print()

for b in range(20, 0, -1):
    print(b, end=' ')
print()

# C
star = int(input("Number of stars: "))
while star <= 0:
    print("incorrect")
    star = int(input("Number of stars: "))
for i in range(star):
    print("*", end="")
print()
# D
star = int(input("Number of stars: "))
for i in range(1, star+1):
    print("*" * i)
