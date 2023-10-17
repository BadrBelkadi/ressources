def hex2string(normal_string):
    try:
        x=bytearray.fromhex(normal_string).decode()
        return x
    except:
        return "-1"
    


def string2hex(normal_string):

    x = normal_string.encode("utf-8").hex()
    return x


def hex_xor(a, b):

    z = (hex(int(a, 16) ^ int(b, 16)))[2:]
    if z == "0":
        return (z.rjust(4, '0'))
    else:
        return (z)
    

def encrypt_single_byte_xor(a, b):
    z = a
    zz = len(z)
    b = b.rjust(zz, b[1])
    result = hex_xor(z, b)
    return result

def decrypt_by_xor(a, b):
    z = a
    zz = len(str(z))
    zzz = int(zz/2)
    b = b*zzz
    result = hex_xor(z, b)
    return result


def lower_letters_count_func(x):
    lower_letters_count = 0
    for letter in x:
        if letter.islower():
            lower_letters_count = lower_letters_count + 1
    return lower_letters_count


def valid_letters_count(string):
    count = 0
    valid_characters =  "abcdefghijklmnopqrstuvxyz ABCDEFGHIJKLMNOPQRSTUVXYZ"
    for char in string:
        if char in valid_characters:
            count +=1

    return count


def decrypt_single_byte_xor(x):
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    all_keys = []
    possible_solutions = []
    for i in range(16):
        for j in range(16):
            all_keys.append(a[i]+a[j])
    h = 0
    
    
    possible_strings = []
    for k in all_keys:
        possible_solutions.append(decrypt_by_xor(x, k))
        possible_strings.append(hex2string(possible_solutions[h]))
        h = h + 1
    letters_count = []
    for string in possible_strings:
        letters_count.append(valid_letters_count(string))
    index_of_max_value = letters_count.index(max(letters_count))
    return possible_strings[index_of_max_value]


print(decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480'))

