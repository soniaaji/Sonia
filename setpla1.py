def reverse(str):
    S = ""
    for ch in str:
        S = ch + S
    return S
mystr = "BeginnersBook"
print("Given String: ", mystr)
print("Reversed String: ", reverse(mystr))
