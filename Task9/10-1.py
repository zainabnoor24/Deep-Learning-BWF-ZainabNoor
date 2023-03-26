filename = 'learning_python.txt'

print("Entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\nLooping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\nStoring lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())