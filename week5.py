# Task 1

def encrypt_by_add_mod(msg,key):
    ouptut = ''
    for i in msg:
        ouptut += chr((ord(i)+key)%256)
    return ouptut

# Task 2

def encrypt_xor_with_changing_key_by_prev_cipher(string,key,operation):
    output = ""
    if operation == "encrypt":
        for i in string :
            output += chr((ord(i) ^ key))
            key = ord(i) ^ key

    else:
        for i in string:
            output += chr(ord(i) ^ key)
            key = ord(i)

    return output


# Task 3

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(message, key_list,operation):
    chunks =[]
    for i in range(len(key_list)):
        chunks.append(message[i::len(key_list)])
    
    encryption = []
    for i in range(len(key_list)):
        encryption.append(encrypt_xor_with_changing_key_by_prev_cipher(chunks[i],key_list[i],operation))
    
    output =''
    for i in range(len(message)):
        x = i % len(key_list)
        y = i // len(key_list)
        output += encryption[x][y]
    return output


