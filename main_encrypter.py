start = input("Enter your message: ")
cipher = ""

for ch in start:
    if not ch.isalpha():
        continue
    else:
        char = ch.upper()
        code = ord(char) + 1
        if code > ord("Z"):
            code = ord("A")
        cipher += chr(code)

print(f"\nEncrypted message is {cipher}")