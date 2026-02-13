#!/usr/bin/env python3
def add_one(n):
    return n + 1

x = 5
print("Before:", x)

add_one(x)

print("After:", x)

# ทำเผื่อไว้คับ
x = add_one(x) # กรณีที่อยากให้ค่า x เปลี่ยน
print("Extra case:", x)