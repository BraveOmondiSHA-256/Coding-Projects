
#prev_sum = 0

#for sum_100 in range(1,101):
  #prev_sum = prev_sum + sum_100
#print(prev_sum)

for one_hunna in range(1, 101):
   if one_hunna % 3 == 0 and one_hunna % 5 == 0:
      print("FizzBuzz")
   elif one_hunna % 5 == 0:
      print("Buzz")
   elif one_hunna % 3 == 0:
         print("Fizz")
   else:
      print(one_hunna)

