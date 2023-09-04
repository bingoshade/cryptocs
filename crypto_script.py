from cryptography.fernet import Fernet
import os

# Function to generate or load an encryption key
def get_or_generate_key(key_filename):
    if os.path.exists(key_filename):
        with open(key_filename, 'rb') as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(key_filename, 'wb') as key_file:
            key_file.write(key)
    return key

# Function to encrypt data using a provided key
def encrypt_data(data, key):
    f = Fernet(key)
    token = f.encrypt(data)
    return token

# Function to decrypt data using a provided key
def decrypt_data(token, key):
    f = Fernet(key)
    data = f.decrypt(token)
    return data

if __name__ == '__main__':
    key_filename = 'encryption_key.key'
    in_path = 'the_path_of_your_file_that_contain_data'
    out_path = 'file_which_you_will_save_the_encrypted_data'
    dec_in_path = 'the_path_of_your_file_that_contain_encrypted_data'
    dec_out_path = 'file_which_you_will_save_the_decrypted_data'

    # Get or generate the encryption key
    key = get_or_generate_key(key_filename)

    # Encryption
    with open(in_path, 'rb') as infile:
        data = infile.read()
        encrypted_data = encrypt_data(data, key)

    with open(out_path, 'wb') as outputfile:
        outputfile.write(encrypted_data)
    print(f'The file {in_path} has been encrypted successfully and copied to {out_path}')

    # Decryption
    with open(dec_in_path, 'rb') as dec_infile:
        dec_data = dec_infile.read()
        decrypted_data = decrypt_data(dec_data, key)

    with open(dec_out_path, 'wb') as dec_outfile:
        dec_outfile.write(decrypted_data)
    print(f'The file {dec_out_path} has been decrypted and saved to {dec_in_path}')





  


