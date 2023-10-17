
#task 1
print('## Task1 =')
def encrypt_with_power(m,k):
    res = ""
    p = 2
    for i in m:
        knn = (ord(i) ^ k)
        k = (k**2)%256
        res += chr(knn)

    return (res)


print(encrypt_with_power('Hello',250))
print(encrypt_with_power(encrypt_with_power('Hello',123),123))
print(encrypt_with_power(encrypt_with_power('Cryptography',10),10))


#task 2

print("== Task 2 ==========")

def encrypt_with_power2(m,k,mode):
    res = ""
    enc = ""
    if mode == 'encrypt':
        for i in range(0,len(m)):
            knn = (ord(m[i]) ^ k)
            if knn == 0 or knn == 1:
                k = ord(m[i-1:i])

            else:
                k = (k ** 2) % 256

            res += chr(knn)
            print(res)
            return res
    else :
        for i in range(0, len(m)):
            knn = (ord(m[i]) ^ k)
            if knn == 0 or knn == 1:
                k = ord(res[-1])
            else:
                k = (k ** 2) % 256

            enc += chr(knn)

            return enc


encrypt_with_power2('Hello',253,'encrypt')
encrypt_with_power2('Hello2',131,'encrypt')
encrypt_with_power2(encrypt_with_power2('Hello',123,'encrypt'),123,'decrypt')
encrypt_with_power2(encrypt_with_power2('Cryptography',10,'encrypt'),10,'decrypt')




#task 3
print('## Task3 =')
def swap_lower_and_upper_bits(c):
    bina = format(c,"b").rjust(8,"0")
    res =''
    co = 4
    for i in range(len(bina)):
        res += bina[co:co+4]
        co += 4
        co = co % len(bina)
        if len(res) == 8 :
            break
    return int(res,2)

print(bin(swap_lower_and_upper_bits(0b1111)))

#task 4







print('===================== Exam B =================')
# Exam B



#task 1
print('## Task1 =')

def encrypt_with_mul(m,k):
    smt =''
    for i in m:
        knn = ord(i) ^ k
        k = (k*2)%256
        smt += chr(knn)
    return smt


print(encrypt_with_mul('Hello',227))
print(encrypt_with_mul(encrypt_with_mul('Hello',123),123))
print(encrypt_with_mul(encrypt_with_mul('Cryptography',10),10))


#task 2


