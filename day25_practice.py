# Day 25 - break & continue

# 1. break example
for i in range(1,6):
    if i == 3:
        break
    print(i)

# 2. continue example
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# 3. skip even numbers
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

# 4. stop at first even number
for i in range(1,11):
    if i % 2 == 0:
        break
    print(i)

# 5. important logic ( order matters)
for i in range(1,6):
    print(i)
    if i == 3:
        continue
    print("hello")

# 6. password checker
correct_password = "python123"
for i in range(5):
    p = input("enter password: ")
    if p == correct_password:
        print("access granted")
        break
    else:
        print("wrong password")
else:
    print("blocked")


# 7. skip banned items
items = [ "apple", "chips","cola","banana","chocolate"]
for i in items:
    if i == "chips" or i == "cola":
        continue
    print("allowed:" , i)


