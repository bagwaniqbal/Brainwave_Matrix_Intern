import re
from math import log2

# Load a dictionary of common passwords dynamically 
def load_common_passwords():
    return {"123456", "password", "qwerty", "abc123", "letmein", "monkey", "123456789", "iloveyou"}

COMMON_PASSWORDS = load_common_passwords()

def calculate_entropy(password):
    """Calculate entropy of a password based on its character set."""
    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        charset_size += 32

    return len(password) * log2(charset_size) if charset_size else 0

def assess_password_strength(password):
    score = 0
    feedback = []
    entropy = calculate_entropy(password)

    # 1. Length Check
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif 8 <= length <= 12:
        score += 1
        feedback.append("Good length, but longer passwords are more secure.")
    else:
        score += 2
        feedback.append("Great! Your password is long enough.")

    # 2. Complexity Check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        score += 1
    else:
        feedback.append("Include special characters (e.g., !, @, #).")

    # 3. Uniqueness Check
    if password in COMMON_PASSWORDS:
        feedback.append("Avoid using common passwords.")
        score -= 2

    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid using repetitive characters.")
        score -= 1

    if re.search(r'(?:012|123|234|345|456|567|678|789)', password):
        feedback.append("Avoid sequential numbers.")
        score -= 1

    # Add entropy-based feedback
    if entropy < 28:
        feedback.append("Entropy is low; your password is too predictable.")
    elif entropy < 50:
        feedback.append("Entropy is moderate. Consider making it more complex.")
    else:
        feedback.append("Great! Your password has high entropy.")

    # Scoring
    if score >= 5 and entropy > 50:
        strength = "Strong"
    elif 3 <= score < 5 or 28 <= entropy <= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "entropy": entropy,
        "feedback": feedback
    }

# Real-time Feedback Example
def real_time_feedback():
    print("Enter a password to check its strength (type 'exit' to quit):")
    while True:
        password = input("\nPassword: ")
        if password.lower() == 'exit':
            print("Goodbye!")
            break

        result = assess_password_strength(password)
        print(f"\nStrength: {result['strength']}")
        print(f"Entropy: {result['entropy']:.2f} bits")
        print("Feedback:")
        for note in result["feedback"]:
            print(f"- {note}")

# Run Real-Time Feedback
if __name__ == "__main__":
    real_time_feedback()
