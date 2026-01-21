import re

print("----- STRONG PASSWORD VALIDATION -----")

password = "Abhay@123"

password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.match(password_pattern, password):
    print("Password:", password, "-> Strong Password")
else:
    print("Password:", password, "-> Weak Password")


print("\n----- REGEX MODIFIERS DEMONSTRATION -----")

# re.IGNORECASE example
text1 = "Python is Powerful"
pattern1 = "python"
match1 = re.search(pattern1, text1, re.IGNORECASE)

print("IGNORECASE Match:", match1.group() if match1 else "No match")


# re.MULTILINE example
text2 = """Python is easy
Java is powerful
Python is popular"""

pattern2 = r"^Python"
matches2 = re.findall(pattern2, text2, re.MULTILINE)

print("MULTILINE Matches:", matches2)


# re.DOTALL example
text3 = "Hello\nWorld"
pattern3 = "Hello.*World"

match3 = re.search(pattern3, text3, re.DOTALL)
print("DOTALL Match:", "Matched" if match3 else "No match")


print("\n----- COMBINED MODIFIERS -----")

text4 = """hello World
HELLO Python"""

pattern4 = r"^hello"
matches4 = re.findall(pattern4, text4, re.IGNORECASE | re.MULTILINE)

print("IGNORECASE + MULTILINE Matches:", matches4)
