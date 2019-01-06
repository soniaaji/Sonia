X = "semi long string with competely random casing"
result_string = ""
for C in X:
    if(index%2 == 0):
        result_string += C.lower()
    else:
        result_string += C.upper()
    index+=1
print(result_string)
