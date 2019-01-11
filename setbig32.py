name = input("Enter name: ") 
num_words = 0
with open(name, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
