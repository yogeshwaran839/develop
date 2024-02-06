def caesar_cipher (text, shift):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base=ord('A')
            
            else:
                base=ord('a')
            encrypted_char=chr((ord(char)-base+shift)%26+base)
            result += encrypted_char
        else:
            result+=char
    return result

choice=input("Do you want to encrypt or decrypt (e/d)?").lower()
text=input("Enter the text:")
shift=int(input("Enter the shift value:"))

if choice =='e':
    encrypted_text=caesar_cipher (text, shift)
    print("Encrypted text:", encrypted_text)
elif choice =='d':
    decrypted_text=caesar_cipher (text,-shift)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid INPUT")
