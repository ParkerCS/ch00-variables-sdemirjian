#continue, break, and else
#break ends the loop
for i in range(100):
    if i == 50:
        break
    print(i)

#continue skips the rest of the loop code and starts the next iteration
for i in range(10):
    if i == 5:
        continue
    print(i)

#pass is just a place holder. It does nothing but fill the loop so the code doesn't give an error. An alternative to commenting out the loop
for i in range(1000):
    pass

for i in range(10):
    user_input = int(input("Gimme a number in between 0 and 100: "))
    if user_input < 0 or user_input > 100:
        break
else:
    print("Thank you for entering your numbers")