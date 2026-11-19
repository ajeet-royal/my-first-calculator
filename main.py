# ye mera pehla calculator hai aur mai ise aur bhi improve karunga and mai isme aur 
# bhi features add karunga jaise ki scientific calculator, graph platter,aur bhi bahut kuchh
while True :
    try :
        first_number = float(input("Enter your first number : "))
        second_number = float(input("Enter your second number : "))
    except ValueError:
        print("🤣🤣🤣🤣 ISKO ITNA BHI NHI PATA KI CALCULATOR KA USE NUMBERS KE LIYE HOTA HAI , 😡😡😡😡 SIRF NUMBER LIKHO SAMJHE") 
    else :
        operators = input(" Enter your operators like = (+, - , / , * , %)")
        if operators == "+":
            print(first_number + second_number)
        elif operators == "-":
            print(first_number - second_number)
        elif operators == "*":
            print(first_number * second_number)
        elif operators == "/":
            print(first_number / second_number)
        elif operators == "%":
            print(first_number % second_number)
        else :
            print("characters are not defined.") 



























