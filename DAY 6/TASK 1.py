import re

emp_id = "EMP123"
m = re.match(r"(EMP)(\d{3})", emp_id)

if m:
    print("Valid Employee ID:", m.group())
    print("Prefix:", m.group(1), "Digits:", m.group(2))

text = "Mail us at test123@gmail.com"
e = re.search(r"([\w.+-]+)@([\w-]+\.\w+)", text)

if e:
    print("Email:", e.group())
    print("User:", e.group(1), "Domain:", e.group(2))

s = "ID 45 Price 900"
r = re.search(r"(\d+)\s+\w+\s+(\d+)", s)

if r:
    print("Numbers:", r.group(1), r.group(2))
