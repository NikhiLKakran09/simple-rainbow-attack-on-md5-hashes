
import os 
import json
import hashlib  # Import the hashlib library for hash functions.

def open_passwd_file_as_list(filepath):
    if os.path.isfile(filepath):
        words = None
        with open(filepath, "r") as fp:
            data = fp.read()
            words = data.split('\n')
        print("Opened password list successfully")
        return words
    print("Error while openning passwords list file")
    return None

def open_text_to_dict(filepath):
    if os.path.isfile(filepath):
        data = None
        with open(filepath, "r") as fp:
            data = json.load(fp)
        return data
    print("Error while openning rainbow table file")
    return None

def write_dict_to_txt(filepath,data_dict):
    if os.path.isfile(filepath):
        try:
            with open(filepath, "w") as fp:
                data = json.dump(data_dict,fp)
        except Exception as e:
            print("Error while writing hashes and passwords to rainbow table file")
                   
def update_rainbow_table(passwdfilepath):
    passwords = open_passwd_file_as_list(passwdfilepath)
    data_dict = open_text_to_dict('./hash_dictionary.txt')
    for password in passwords:
        # Encode the current word to bytes using UTF-8 and calculate its MD5 hash.
        enc_password = password.encode("UTF-8")
        #print("Calculating hash. Please wait...") # Displays a loading message for the user.
        enc_hash = hashlib.md5(enc_password.strip()).hexdigest()
        if enc_hash not in data_dict.keys():
            data_dict[enc_hash]=password
    write_dict_to_txt('./hash_dictionary.txt',data_dict)
    print("Hashes added successfully")
 
if __name__ == '__main__':
    update_rainbow_table('./passwords.txt')
    












# Note: Take care Error Handling

# Functions :
    # main loop
        # password_file()
        # safely open password file as list
        # safely open rainbow-table.txt file as list
        # save_hash()
    # save_hash
        # calculate md5 hash of a password
        # save md5 hash-password in rainbow-table.txt file as key-value
    # password_file()
        # take input of file path
        # validate path belongs to a file
    
    
