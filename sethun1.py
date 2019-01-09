num = int(input("How many nos:"))
total_sum = 0
for N in range(num):
    numbers = float(input("Enter no : "))
    total_sum += numbers
avg = total_sum/num
print("Average of ", num, " nos is :", avg)
