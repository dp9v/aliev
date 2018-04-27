def compare_string(str_1, str_2):
    symbols_count = {}
    if len(str_1) != len(str_2):
        return False
    for ch in str_1:
        if ch in symbols_count.keys():
            symbols_count[ch] += 1
        else:
            symbols_count[ch] = 1

    for ch in str_2:
        if ch in symbols_count.keys():
            symbols_count[ch] -=1
        else:
            return False
        if symbols_count[ch]<0:
            return False
    return True


print(compare_string("1234", "4321"))
print(compare_string("12324", "43321"))
print(compare_string("1234fs", "4f32s1"))
print(compare_string("12234fs", "4f3g2s1"))