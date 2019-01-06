def roman_to_int(self, S):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(S)):
            if i > 0 and rom_val[S[i]] > rom_val[S[i - 1]]:
                int_val += rom_val[S[i]] - 2 * rom_val[S[i - 1]]
            else:
                int_val += rom_val[S[i]]
        return int_val
print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))
