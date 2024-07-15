import numpy as np

def hill_cipher_encrypt(message, key):
    # Convert message to uppercase
    message = message.upper()
    
    # Ensure key is a square matrix
    n = int(np.sqrt(len(key)))
    key_matrix = np.array(key).reshape(n, n)
    
    # Convert message to numerical form
    message_vector = [ord(char) - ord('A') for char in message]
    
    # If the message length is not a multiple of n, pad it with 'X' (or any other character)
    while len(message_vector) % n != 0:
        message_vector.append(ord('X') - ord('A'))
    
    message_matrix = np.array(message_vector).reshape(-1, n).T
    
    # Encrypt the message
    encrypted_matrix = np.dot(key_matrix, message_matrix) % 26
    
    # Convert back to letters
    encrypted_message = ''.join([chr(num + ord('A')) for num in encrypted_matrix.T.flatten()])
    return encrypted_message

def hill_cipher_decrypt(encrypted_message, key):
    # Convert encrypted message to uppercase
    encrypted_message = encrypted_message.upper()
    
    # Ensure key is a square matrix
    n = int(np.sqrt(len(key)))
    key_matrix = np.array(key).reshape(n, n)
    
    # Calculate the inverse of the key matrix modulo 26
    key_inverse = np.linalg.inv(key_matrix)
    key_inverse = np.round(key_inverse).astype(int) % 26
    
    # Convert encrypted message to numerical form
    encrypted_vector = [ord(char) - ord('A') for char in encrypted_message]
    encrypted_matrix = np.array(encrypted_vector).reshape(-1, n).T
    
    # Decrypt the message
    decrypted_matrix = np.dot(key_inverse, encrypted_matrix) % 26
    
    # Convert back to letters
    decrypted_message = ''.join([chr(int(num) + ord('A')) for num in decrypted_matrix.T.flatten()])
    return decrypted_message

# Example usage:
key = [6, 24, 1, 13, 16, 10, 20, 17, 15]  # 3x3 key matrix
message = "ACT"

encrypted_message = hill_cipher_encrypt(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = hill_cipher_decrypt(encrypted_message, key)
print("Decrypted Message:", decrypted_message)
import numpy as np

def hill_cipher_encrypt(message, key):
    # Convert message to uppercase
    message = message.upper()
    
    # Ensure key is a square matrix
    n = int(np.sqrt(len(key)))
    key_matrix = np.array(key).reshape(n, n)
    
    # Convert message to numerical form
    message_vector = [ord(char) - ord('A') for char in message]
    
    # If the message length is not a multiple of n, pad it with 'X' (or any other character)
    while len(message_vector) % n != 0:
        message_vector.append(ord('X') - ord('A'))
    
    message_matrix = np.array(message_vector).reshape(-1, n).T
    
    # Encrypt the message
    encrypted_matrix = np.dot(key_matrix, message_matrix) % 26
    
    # Convert back to letters
    encrypted_message = ''.join([chr(num + ord('A')) for num in encrypted_matrix.T.flatten()])
    return encrypted_message

def hill_cipher_decrypt(encrypted_message, key):
    # Convert encrypted message to uppercase
    encrypted_message = encrypted_message.upper()
    
    # Ensure key is a square matrix
    n = int(np.sqrt(len(key)))
    key_matrix = np.array(key).reshape(n, n)
    
    # Calculate the inverse of the key matrix modulo 26
    key_inverse = np.linalg.inv(key_matrix)
    key_inverse = np.round(key_inverse).astype(int) % 26
    
    # Convert encrypted message to numerical form
    encrypted_vector = [ord(char) - ord('A') for char in encrypted_message]
    encrypted_matrix = np.array(encrypted_vector).reshape(-1, n).T
    
    # Decrypt the message
    decrypted_matrix = np.dot(key_inverse, encrypted_matrix) % 26
    
    # Convert back to letters
    decrypted_message = ''.join([chr(int(num) + ord('A')) for num in decrypted_matrix.T.flatten()])
    return decrypted_message

# Example usage:
key = [6, 24, 1, 13, 16, 10, 20, 17, 15]  # 3x3 key matrix
message = "ACT"

encrypted_message = hill_cipher_encrypt(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = hill_cipher_decrypt(encrypted_message, key)
print("Decrypted Message:", decrypted_message)