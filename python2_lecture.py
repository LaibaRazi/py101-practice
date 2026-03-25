# Think of Python like LEGO - small pieces (tokens) build big programs!

# 1. CHARACTER SET: Letters, numbers, symbols Python understands
# (Like alphabet + math symbols + punctuation)

# 2. TOKENS (code pieces):
# ------------------------
# KEYWORDS (Python's special words) - 'print', 'if', 'for' etc.
# IDENTIFIERS (names we create) - variables, functions etc.
# LITERALS (fixed values) - numbers, text
# OPERATORS (actions) - +, -, *, / 
# PUNCTUATORS (grammar) - (), :, "" etc.

# ===== LET'S CODE! =====
print("\n=== TOKEN ADVENTURE ===")

# IDENTIFIERS & LITERALS
hero = "SuperCoder"  # 'hero' is identifier, "SuperCoder" is string literal
power_level = 9001   # 'power_level' is identifier, 9001 is number literal
skills = ["Coding", "Math", "Debugging"]  # List literal

print("Meet our hero:", hero)
print("Power level:", power_level)
print("Special skills:", skills)

# TYPE FUNCTION - reveals what kind of data
print("\n=== DATA TYPE DETECTIVE ===")
print("hero is", type(hero))          # string
print("power_level is", type(power_level))  # integer
print("skills is", type(skills))      # list

# OPERATORS IN ACTION
print("\n=== MATH MAGIC ===")
a = 10
b = 3
print("a =", a, "| b =", b)

print("\nLet's do math!")
print("Add:", a, "+", b, "=", a + b)    # + operator
print("Subtract:", a, "-", b, "=", a - b)
print("Multiply:", a, "*", b, "=", a * b)
print("Divide:", a, "/", b, "=", a / b)
print("Power:", a, "** 2 =", a ** 2)    # exponent

# COMPARISON OPERATORS (True/False)
print("\n=== COMPARISON CHALLENGE ===")
print("Is power_level > 9000?", power_level > 9000)  # > operator
print("Is hero == 'SuperCoder'?", hero == "SuperCoder")  # == operator

# BONUS: INTERACTIVE VERSION
print("\n=== YOUR TURN! ===")
try:
    your_name = input("Enter your name: ")
    your_age = int(input("Enter your age: "))
    print(f"\nWelcome {your_name}! In 10 years you'll be {your_age + 10}!")
except:
    print("Oops! Please enter numbers for age!")

print("\nRemember: Code is built with these small tokens!")