def check_string(input_string):
    symbols = set()
    for ch in input_string:
        if ch in symbols:
            return False
        else:
            symbols.add(ch)
    return True

print("1", check_string("123456"))
print("2", check_string("1234563"))
print("3", check_string("1223456"))