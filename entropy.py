import math


def get_character_pool_size(password: str) -> int:
    """Determine the size of the character pool used in the password."""
    pool=0
    if any(c.islower() for c in password):
        pool += 26  # Lowercase letters
    if any(c.isupper() for c in password):
        pool += 26  # Uppercase letters
    if any(c.isdigit() for c in password):
        pool += 10  # Digits
    if any(not c.isalnum() for c in password):
        pool += 32  # Symbols

    return pool
def calculate_entropy(password: str) -> float:
    """Calculate the entropy of a password."""
    if not password:
        return 0.0
    pool_size = get_character_pool_size(password)
    if pool_size == 0:
        return 0.0  # Avoid log(0) error

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)
def get_entropy_rating(entropy: float) -> str:
    """Get the strength rating based on the entropy value."""
    if entropy < 28:
        return "Very Weak"
    elif 28 <= entropy < 35:
        return "Weak"
    elif 35 <= entropy < 59:
        return "Reasonable"
    elif 59 <= entropy < 128:
        return "Strong"
    else:
        return "Very Strong"
def analyse_entropy(password: str) -> dict:
    """Analyse the password and return its entropy and strength rating."""
    pool_size = get_character_pool_size(password)
    entropy = calculate_entropy(password)
    rating = get_entropy_rating(entropy)

    return {
        "entropy_bits" : entropy,
        "pool_size" : pool_size,
        "length" : len(password),
        "rating" : rating,
    }

if __name__ == "__main__":
    test_passwords = [
        "abc",
        "password",
        "password1",
        "P@ssw0rd!",
        "x7#mk2$ql9!vR4",
    ]
    print(f"{'Password':<20} {'Length': >6} {'Pool': >5}{'Entropy (bits)': >15}  {'Rating' : >12}")
    for pwd in test_passwords:
        result = analyse_entropy(pwd)
        print(f"{pwd:<20} {result['length']: >6} {result['pool_size']: >5} {result['entropy_bits']: >15}  {result['rating'] : >12}")

        print("\n)" + "="*65)
        print("Password entropy checker")
        print("="*65)
        while True:
            user_pwd = input("Enter a password to check (or 'exit' to quit): ")
            if user_pwd.lower() == 'exit':
                print("Exiting the password entropy checker. Stay safe!")
                break
            result = analyse_entropy(user_pwd)
            print(f"Password: {user_pwd}")
            print(f"Length: {result['length']} characters")
            print(f"Character Pool Size: {result['pool_size']}")
            print(f"Entropy: {result['entropy_bits']} bits")
            print(f"Strength Rating: {result['rating']}")
            print("-" * 65)
            