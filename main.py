from scrambler import encrypt
from descrambler import decrypt

print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose: ")

if choice == "1":
    encrypt()

elif choice == "2":
    decrypt()

else:
    print("Invalid choice")
