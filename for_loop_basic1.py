# # Basic - Print all integers from 0 to 150.
for i in range(150):
    print(i)

# # Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1000, 5):
    print(i)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".


def divisible_by():
    for i in range(1, 100):
        if i % 5 == 0:
            print("Coding")
        if i % 10 == 0:
            print("Coding Dojo")


divisible_by()

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
maximum = 500000
minimum = 0


def add_odd_integer():
    sum = 0
    for i in range(minimum, maximum):
        if i % 2 == 1:
            sum += i
    print('Final', sum)


add_odd_integer()

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.


def countdown_by_4():
    for i in range(2018, 0, -4):
        if i > 0:
            print(i)


countdown_by_4()

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and
# going through highNum, print only the integers that are a multiple of mult. For example,
# if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


def flexible_counter(lowNum, highNum, multiple):
    for i in range(lowNum, highNum):
        if i % multiple == 0:
            print(i)


flexible_counter(2, 10, 3)
