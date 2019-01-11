def char_frequency(str):
    dict = {}
    for N in str:
        keys = dict.keys()
        if N in keys:
            dict[N] += 1
        else:
            dict[N] = 1
    return dict
print(char_frequency("Google.com"))
