# 1. Variables
name = "Alex"
age = 22
print(f"Name: {name}, Age: {age}")

# 2. Lists
tools = ["Python", "GitHub", "Notion"]
print("My tools:", tools)

# 3. Loops
print("Iterating through the list:")
for tool in tools:
    print("- Using:", tool)

# 4. Functions
def welcome_message(user_name):
    return f"Hello {user_name}, welcome to Python!"

print(welcome_message(name))
