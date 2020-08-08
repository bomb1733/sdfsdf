"""
for i in range(11):
    print("*"*i)
"""

"""
for a in range(10):
    print("*"*a)
for b in range(10):
    print("*"*(10-b))
"""
"""
for i in range(100):
    a = i  % 10
    if a%3 == 0:
        print("*")
    else:
        print(i)
"""
"""
for i in range(100):
    a = i  % 10
    if i%10 == 0:
        print(i)
    elif a%3 == 0:
        print("*")
    else:
        print(i)
"""
"""
33, 36, 39
63, 66, 69
93, 96, 99 일 경우에는 별 두개
"""

for i in range(100):
    a = i  % 10
    b = i // 10
    if i%10 == 0 and i%10 != 0:
        print(i)
    elif i == 33 or i == 36 or i == 39 or i == 63 or i == 66 or i == 69 or i == 93 or i == 96 or i == 99:
        print("**")
    elif a%3 == 0:
        print("*")
    elif b == 3 or b == 6 or b == 9:
        print("*")
    else:
        print(i)
"""
선생님답
"""

"""
for i in range(100):
    one = i % 10
    ten = i // 10

    ten_condition = ten % 3 == 0 and ten !=0
    one_condition = one % 3 == 0 and one !=0

    if one_condition and ten_condition:
        print("**")
    elif one_condition:
        print("*")
    elif ten_condition:
        print("*")
    else:
        print(i)

"""
"""
for i in range(10):
    if i == 5:
        continue
    print(i)
"""
