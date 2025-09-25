

prompt = "Enter ticket that youy want to print : "


num_ticket = input(prompt)


try:
    num_ticket = int(num_ticket)
    if num_ticket <= 0:
        raise ValueError("The number must be positive.")
except ValueError:
    print("Please try again")
else:
    print(f"Your ticket number is {num_ticket}")