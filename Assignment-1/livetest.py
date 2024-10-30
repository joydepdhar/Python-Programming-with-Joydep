def ticket_price(age ,showtime):
    ticket_price=0
    if age<0:
        return "Invalid age"
    elif showtime < 0 or showtime > 2359 or showtime % 100 >= 60:
        return "Invalid input. Please provide the showtime in the correct format."
    if age < 11:
        ticket_price = 300
    elif age < 26:
        ticket_price = 500
    elif age<60:
        ticket_price = 800
    elif age>60 and age<100:
        ticket_price = 400
    discount = 0
    if showtime < 1700:
        discount = ticket_price * 0.10 

    discountPrice=ticket_price-discount
    return [ticket_price,discount,discountPrice]

def main():
    print("**Welcome to Movie Theater**")
    try:
        age = int(input("Enter your age: "))
        showtime = int(input("Enter the showtime (HHMM): "))
        # print(ticket_price(age, showtime))
        result=ticket_price(age,showtime)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Ticket Price: {result[0]:.2f} BDT")
            print(f"Discount: {result[1]:.2f} BDT")
            print(f"Discounted Price: {result[2]:.2f} BDT")
    except ValueError:
        print("Invalid input. Age must be a positive integer.")
        
if __name__ == "__main__":
        main()