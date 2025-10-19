import re

def check_password_strength(password):
    # Criteria definitions
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Evaluate overall strength
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score == 5:
        return "✅ Strong Password"
    elif 3 <= score < 5:
        return "🟡 Medium Strength Password"
    else:
        return "🔴 Weak Password"

# Main program
password = input("Enter your password to check strength: ")
print(check_password_strength(password))
