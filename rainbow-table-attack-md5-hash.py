
from rainbow_table_create_md5_hash import *


if __name__ == '__main__':
    # enter_passwd = input("Enter Your password : ")
    # Encode the current word to bytes using UTF-8 and calculate its MD5 hash.
    # enc_password = enter_passwd.encode("UTF-8")
    # print("Calculating hash. Please wait...") # Displays a loading message for the user.
    # enc_hash = hashlib.md5(enc_password.strip()).hexdigest()
    enc_hash = input("Enter value of md5 hash : ")
    password_hashes = open_text_to_dict('./hash_dictionary.txt')
    print(enc_hash)
    if enc_hash in password_hashes.keys():
        print("for md5 has supplied by you we found password : ",password_hashes[enc_hash]," in our rainbow table")