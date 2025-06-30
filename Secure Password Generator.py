import secrets
import string

class PasswordGen:
    def __init__(self):
        
        self.clear_letters = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
        self.clear_numbers = "23456789"
        self.symbols = "!@#$%&*+-="
    
        self.prefixes = ["Fire", "Moon", "Star", "Blue", "Fast", "Wild", "Gold", "Cool"]
        self.suffixes = ["Cat", "Fox", "Wolf", "Bear", "Lion", "Bird", "Fish", "Hawk"]

    def random_password(self, length=12, use_symbols=True, clear_chars=True):
        """Generate a random password"""
        chars = ""
        
        if clear_chars:
            chars = self.clear_letters + self.clear_numbers
        else:
            chars = string.ascii_letters + string.digits
            
        if use_symbols:
            chars += self.symbols
            
        # Ensure we have at least one of each type
        password = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase), 
            secrets.choice(string.digits),
        ]
        
        if use_symbols:
            password.append(secrets.choice(self.symbols))
            
        # Fill the rest randomly
        while len(''.join(password)) < length:
            password.append(secrets.choice(chars))
            
        # Shuffle and return
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

    def memorable_password(self, add_numbers=True, add_symbols=True):
        """Generate a memorable password like 'FireCat42!' """
        password = secrets.choice(self.prefixes) + secrets.choice(self.suffixes)
        
        if add_numbers:
            password += str(secrets.randbelow(100))
            
        if add_symbols:
            password += secrets.choice(self.symbols)
            
        return password

    def passphrase(self, words=4):
        """Generate a passphrase like 'fire-moon-star-cool-23' """
        word_list = [w.lower() for w in self.prefixes + self.suffixes]
        selected = [secrets.choice(word_list) for _ in range(words)]
        selected.append(str(secrets.randbelow(100)))
        return '-'.join(selected)

    def check_strength(self, password):
        """Quick strength check"""
        score = 0
        checks = {
            "Length 8+": len(password) >= 8,
            "Length 12+": len(password) >= 12, 
            "Uppercase": any(c.isupper() for c in password),
            "Lowercase": any(c.islower() for c in password),
            "Numbers": any(c.isdigit() for c in password),
            "Symbols": any(c in self.symbols for c in password)
        }
        
        score = sum(checks.values())
        
        if score <= 2:
            strength = "😟 Weak"
        elif score <= 4:
            strength = "😐 Fair"  
        elif score <= 5:
            strength = "😊 Good"
        else:
            strength = "💪 Strong"
            
        return strength, checks

def main():
    gen = PasswordGen()
    
    print("🔐 Simple Password Generator")
    print("-" * 30)
    
    while True:
        print("\n1. Random password")
        print("2. Memorable password")
        print("3. Passphrase")
        print("4. Check password strength")
        print("5. Generate multiple")
        print("6. Quit")
        
        choice = input("\nPick (1-6): ").strip()
        
        if choice == "1":
            length = int(input("Length (default 12): ") or 12)
            use_symbols = input("Include symbols? (Y/n): ").lower() != 'n'
            
            pwd = gen.random_password(length, use_symbols)
            strength, _ = gen.check_strength(pwd)
            
            print(f"\n🔑 Password: {pwd}")
            print(f"💪 Strength: {strength}")
            
        elif choice == "2":
            pwd = gen.memorable_password()
            strength, _ = gen.check_strength(pwd)
            
            print(f"\n🔑 Password: {pwd}")
            print(f"💪 Strength: {strength}")
            print("💡 Easy to remember and type!")
            
        elif choice == "3":
            words = int(input("Number of words (default 4): ") or 4)
            pwd = gen.passphrase(words)
            strength, _ = gen.check_strength(pwd)
            
            print(f"\n🔑 Passphrase: {pwd}")
            print(f"💪 Strength: {strength}")
            print("💡 Super memorable!")
            
        elif choice == "4":
            pwd = input("Enter password to check: ")
            strength, checks = gen.check_strength(pwd)
            
            print(f"\n💪 Strength: {strength}")
            print("Details:")
            for check, passed in checks.items():
                print(f"  {'✅' if passed else '❌'} {check}")
                
        elif choice == "5":
            count = int(input("How many passwords? ") or 3)
            print(f"\n🔑 Generated {count} passwords:")
            
            for i in range(count):
                pwd = gen.random_password()
                strength, _ = gen.check_strength(pwd)
                print(f"{i+1}. {pwd} {strength}")
                
        elif choice == "6":
            print("👋 Bye!")
            break
            
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()