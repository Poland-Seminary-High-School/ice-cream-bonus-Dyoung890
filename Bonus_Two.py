#Ice cream order
print("Hello, welcome to the ULTIMATE SUNDAE PROGRAM")
Base = input("Please enter the flavor you want the ice cream to be (Vanilla, Chocolate, or Twist) ")
prompt = ("\nPlease enter a sauce you would like on the sundae: ")
prompt += ("\ntype 'quit' when you are finished ")
toppings = [""]
message = ""
while message != "quit":
    message = input(prompt)
    toppings.append(message)
    print(f"Topping {message} has been added")
    prompt = ("\nEnter another topping or type 'quit' to end the program ")
    if message == "quit":
        toppings.remove("quit")
        toppings.remove("")
        toppings_two = ", ".join(toppings)
        print(f"Your sundae is made of {Base} ice cream and has the toppings {toppings_two}, please pull up to the window for your total")