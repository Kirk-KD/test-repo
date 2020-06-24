# Homework
# 1.
with open("D:\\Coding Projects\\Python Scripts\\Python Class\\L3C2\\file2.txt", "r") as f1:
    line = f1.readlines()
    for l in line:
        print(len(l))
f1.close()

# 2.
with open("D:\\Coding Projects\\Python Scripts\\Python Class\\L3C2\\program2.txt", "w") as f2:
    for i in range(1, 11):
        f2.write(f"{i}\n")
f2.close()
