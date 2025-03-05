import hashlib
import requests

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1
    if any(char in '!@#$%^&*()-+=' for char in password):
        strength += 1

    return min(strength, 3)  # Ensure the strength value stays within range

def check_data_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    
    if suffix in response.text:
        return True
    return False

def main():
    password = input("Enter a password to check: ")
    strength = check_password_strength(password)
    breached = check_data_breach(password)
    
    print("\nPassword Strength:", ["Weak", "Moderate", "Strong", "Very Strong"][strength])
    if breached:
        print("⚠️ Warning: This password has been found in a data breach!")
    else:
        print("✅ Good news! This password has not been found in breaches.")

if __name__ == "__main__":
    main()
