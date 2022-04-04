# 1. TASK: print "Hello World"
print("Hello world")
# # 2. print "Hello Noelle!" with the name in a variable
name = "Julie"
print(f"Hello {name}")
print("Hello", name)  # with a comma
# print( your code here )	# with a +
print("Hello" + " " + name)
# # 3. print "Hello 42!" with the number in a variable
num = 20
print("Hello", num)  # with a comma
# print( your code here )	# with a +	-- this one should give us an error!
print("Hello" + " " + str(num))
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "chinese"
fave_food2 = "mexican"
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string
print("I love to eat {} and {}.".format(fave_food1, fave_food2))  # with .format()

