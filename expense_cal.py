try:
    balance = float(input("How much do you have? "))
except ValueError:
    print("invalid value")

done = "YES"
done_right = ""
i = 0
total = 0

print("\n")

while not(done_right == done) :
    try:
        expense = float(input("Today's expenses: "))
    except ValueError:
        print("invalid value")
    i += 1

    for full_expense in range(1):
        total = total + expense

    if i <= 9:
        done_right = input("Done entering?\n>>>ENTER \'YES\' or \'NO\': ")
        print("\n")


if balance >= expense:
    result = balance - total
    print("_____________________________________________")
    print("Your today's last balance is " + str(result))
    print("_____________________________________________")
else:
    print("_____________________________________________")
    print("You've exceeded your money balance!")
    print("_____________________________________________")

