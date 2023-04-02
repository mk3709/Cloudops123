from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Create a new Fernet object with the key
cipher_suite = Fernet(key)

# Encrypt data
plaintext = b"Secret data"
ciphertext = cipher_suite.encrypt(plaintext)

# Decrypt data
decrypted_plaintext = cipher_suite.decrypt(ciphertext)

print(decrypted_plaintext)
