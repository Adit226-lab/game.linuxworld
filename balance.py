balance = 5000
pin = 1234
attempts = 0  

while attempts < 3:   
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("PIN Verified Successfully!")
        print("Your balance is:", balance)
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful! New balance is:", balance)
        else:
            print("Insufficient Balance!")
        break   

    else:
        attempts += 1
        print("Incorrect PIN!")

        if attempts < 3:
            print(f"Attempts left: {3 - attempts}")


if attempts == 3:
    print("3 Wrong Attempts! Access Blocked.")

 