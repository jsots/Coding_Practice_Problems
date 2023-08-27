def check_valid_phone_number (number):
    if len(number) != 10 or number[0] == "0" or number[0] == "1":
        return False
    return True

def convert_phone_number (number):
    if check_valid_phone_number(number):
        phone_num = []
        i = 0
        while i < len(number):
            if i % 3 == 0 and i != 9 and i != 0:
                phone_num.append("-")
            phone_num.append(number[i])
            i += 1

        return "".join(phone_num)
    else:
        return "Not a valid US phone number"

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