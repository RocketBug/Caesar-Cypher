# Caesar cipher
# A - Z 65-90
# a - z 97-122

message = input("Enter the message: ")
key = int(input("Enter the key between 1-26 : "))
secretMessage = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26

            if char_code < ord('A'):
                char_code += 26

        else:
            if char_code > ord('z'):
                char_code -= 26

            if char_code < ord('a'):
                char_code += 26

        secretMessage += chr(char_code)
    else:
        secretMessage += char


print("Encrypted message: ", secretMessage)
origMessage = ""
key = -key
for char in secretMessage:

    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26

            if char_code < ord('A'):
                char_code += 26

        else:
            if char_code > ord('z'):
                char_code -= 26

            if char_code < ord('a'):
                char_code += 26

        origMessage += chr(char_code)

    else:
        origMessage += char

print("Decrypted message: ", origMessage)
