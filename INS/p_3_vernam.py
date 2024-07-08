def vernam_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        encrypted_char = chr(((ord(char) - ord('A') + ord(key_char) - ord('A')) % 26) + ord('A'))
        ciphertext.append(encrypted_char)
    
    return ''.join(ciphertext)

def vernam_decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % len(key)]
        decrypted_char = chr(((ord(char) - ord('A') - (ord(key_char) - ord('A')) + 26) % 26) + ord('A'))
        plaintext.append(decrypted_char)
    
    return ''.join(plaintext)

def main():
    while True:
        print("Select an option:")
        print("1. Encrypt (Vernam cipher)")
        print("2. Decrypt (Vernam cipher)")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            plaintext = input("Enter plaintext (only uppercase letters): ")
            encryption_key = input("Enter encryption key (same length as plaintext): ").strip().upper()
            
            if len(plaintext) != len(encryption_key):
                print("Error: Key length must match plaintext length.")
                continue
            
            ciphertext = vernam_encrypt(plaintext, encryption_key)
            print(f"Encrypted: {ciphertext}")
        
        elif choice == '2':
            ciphertext = input("Enter ciphertext (only uppercase letters): ")
            decryption_key = input("Enter decryption key (same length as ciphertext): ").strip().upper()
            
            if len(ciphertext) != len(decryption_key):
                print("Error: Key length must match ciphertext length.")
                continue
            
            decrypted_text = vernam_decrypt(ciphertext, decryption_key)
            print(f"Decrypted: {decrypted_text}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()