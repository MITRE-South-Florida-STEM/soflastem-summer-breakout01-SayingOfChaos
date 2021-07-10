# 1.
# Use the below two variables to create the string: "umbrella ella ella"
# Replace the ellipsis with your code.
once = "umbr"
repeat = "ella"

rihanna_says = once + repeat + ((" " + repeat) * 2)
print(rihanna_says)

# Hint: Use both the addition and multiplication signs to make your code concise

# 2.
# Find values for x such that each print statement is reached.

x = 0 #x = 0, 1, 6, -6
y = 5
if -1 < x / y < 1:
  if not x:
    print("Found me! x is ", x)
  else:
    print("Found me two! x is ", x)
elif x > 2:
  if x >= 3 and x - y <= 2:
    print("Found me three! x is", x)
else:
  if x % y > 1:
    print("Found me four! x is", x)

# 3.
# Complete the code in the for loop

my_variable = 0
for i in range(1, 10):
  # TODO add i to my_variable
  my_variable += i

  # TODO check if my_variable is even
  if my_variable % 2 == 0:
    # TODO square my_variable
    my_variable *= my_variable
  else:
    # TODO divide my_variable by 10
    my_variable /= 10

  # TODO check if my_variable is greater than 100
  if my_variable > 100:
    break

print(my_variable)
