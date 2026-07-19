def select_number():

    usrinput = input("Digite o número:")

    if not usrinput.isdigit():
        raise TypeError("Incorret option format")
    
    return int(usrinput)

