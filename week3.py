def hex2bin(string):
    return bin(int(string,base=16))[2:]

def bin2hex(string):
    return hex(int(string,2))[2:]

def hex2base64(string):
    
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
    }

    binary_string = ''.join(hex_to_bin[char] for char in string.lower())

    padding = (6 - (len(string) % 6)) % 6

    binary_string += '0' * padding

    bin_to_base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    base64_string = ''


    for i in range(0, len(binary_string), 6):
        block = binary_string[i: i + 6]
        dec_value = int(block, 2)
        base64_string += bin_to_base64[dec_value]

    base64_string += '=' * (padding // 2)

    return base64_string




