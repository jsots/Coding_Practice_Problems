def convert_phone_number (number):
    if len(number) != 10 or number[0] == "0" or number[0] == "1":
        return "Not a valid phone number."
    
    phone_num = []
    counter = 0
    for num in number:
        if counter == 3:
            counter = 0
            phone_num.append("-")
        else:
            counter += 1
            phone_num.append(num)

    return "".join(phone_num)

test_1 = "1234567890"
test_2 = "9876543210"
test_3 = "5551234567"
test_4 = "0123456789"
test_5 = "12345"

print(convert_phone_number(test_1))
print(convert_phone_number(test_2))
print(convert_phone_number(test_3))
print(convert_phone_number(test_4))
print(convert_phone_number(test_5))