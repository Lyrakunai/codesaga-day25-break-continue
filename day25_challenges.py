# ------------------
#  Mini Challenges
# ------------------

# Challenge 1 - bus system
for i in range(1,21):
    if i % 4 == 0:
        continue
    if i == 13:
        print("VIP arrived")
        continue
    if i == 17:
        print("bus full")
        break
    print("passenger", i ,"borded")

# Challenge 2 - battery system
for i in range(100,0,-10):
    if i == 50:
        print("half battery")
    if i == 20:
        continue
    if i == 10:
        print("critical ")
        break
    print("battery:", i,"%")

# Challenge 3 - exam system
for i in range(1,16):
    if i == 5 or i == 9:
        continue
    if i == 12:
        print("student",i ,":disqualified")
        break
    if i % 2 == 0:
        print("student",i,":pass")
    else:
        print("student",i, ":fail")

# Challenge 4 - youtube system
for i in range(1,11):  
    if i == 3:
        continue
    if i == 6:
        print("liked & shared")
        continue
    if i == 8:
        print("bored")
        break
    print("watching video",i)

# Challenge 5 - train system
for i in range(1,13):
    if i == 2 or i == 11:
        continue 
    if i == 7:
        print("suspicious")
    if i == 10:
        print("police called")
        break
    print("checked passenger",i)
