"""
This program uses the Fernet symmetric encryption algorithm from the cryptography library to encrypt and decrypt files.
The following was coded folliwng the tutorial at https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

This is used to test the AES256 encryption and decryption functions. Next steps will be to make it more user-friendly and add more features.
Such as receiving the password from the user and letting the user choose and select the file to encrypt or decrypt.

Name: Andrea Marcelli
Course: CPSC 49200 003, Fall 2024
Capstone Project
"""

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import secrets
import base64
import getpass

# The `generate_salt` function generates a random salt of a specified size.
def generate_salt(size=16):
    """Generate the salt used for key derivation, 
    `size` is the length of the salt to generate and is returned as bytes."""
    return secrets.token_bytes(size)

# The `derive_key` function generates a key from a password and a salt using the Scrypt key derivation function.
def derive_key(salt, password):
    """Derive the key from the `password` using the passed `salt`
        Salt is 16 bytes long, key length is 32 bytes (or 256 bits)
        n stands for the number of iterations
        r is the block size
        p is the parallelization factor.
    """
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

# The `load_salt` function reads the salt from a file called `salt.salt`.
def load_salt():
    # load salt from salt.salt file
    return open("salt.salt", "rb").read()

# This function generates a key from a password and a salt by using the `derive_key` function.
# The key is necessary for encryption and decryption. Specifically, it uses the Fernet symmetric encryption algorithm.
def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """
    Generates a key from a `password` and the salt.
    If `load_existing_salt` is True, it'll load the salt from a file
    in the current directory called "salt.salt".
    If `save_salt` is True, then it will generate a new salt
    and save it to "salt.salt"
    """
    if load_existing_salt:
        # load existing salt
        salt = load_salt()
    elif save_salt:
        # generate new salt and save it
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    # generate the key from the salt and the password
    derived_key = derive_key(salt, password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)

# Encrypt and decrypt functions

# The encrypt function does the following:
# 1. Read the file data
# 2. Encrypt the data
# 3. Write the encrypted data back to the file
def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# The decrypt function does the following:
# 1. Read the encrypted data
# 2. Decrypt the data
# 3. Write the decrypted data back to the file
def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data by using the key given by the user and write it back to the file

    """
    VERY IMPORTANT: Note that if you generate another salt (by passing -s or --salt-size) while decrypting, 
    even if it's the correct password, you won't be able to recover the file as a new salt will be generated 
    that overrides the previous one, so make sure not to pass -s or --salt-size when decrypting.
    """
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully")

# Main function to run the script from the command line
"""
This script can be used to encrypt and decrypt files using AES256 encryption.
It works by generating a key from a password and a salt, then using that key to encrypt or decrypt the file.
"""
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="File Encryptor Script with a Password")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",
                        type=int)
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ")
    elif args.decrypt:
        password = getpass.getpass("Enter the password you used for encryption: ")

    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        encrypt(file, key)
    elif decrypt_:
        decrypt(file, key)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    
# Use the following command to encrypt --> python aes256-test1.py filename.format --encrypt --salt-size 16
# Use the following command to decrypt --> python aes256-test1.py filename.format --decrypt

# The first example will encrypt our file inside the folder, called 'Code_v2.pdf' with a salt size of 16 bytes.