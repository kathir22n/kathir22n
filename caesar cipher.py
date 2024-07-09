def encryption(text,key):
    e=''
    for c in text:
        if c.islower():
            e=e+chr((ord(c)+k-97)%26+97)
        elif c.isupper():
            e=e+chr((ord(c)+k-65)%26+65)
        else:
            e=e+c
    return e
def decryption(text,key):
    d=''
    for c in text:
        if c.islower():
            d=d+chr((ord(c)-k-97)%26+97)
        elif c.isupper():
            d=d+chr((ord(c)-k-65)%26+65)
        else:
            d=d+c
    return d

plaintext=input('enter a plaintext: ')
k=int(input('enter the key value: '))
plaintext=encryption(plaintext,k)
print("encrypted text:",plaintext)
etext=input('enter a encrypted text: ')
k=int(input('enter the key value: '))
etext=decryption(etext,k)
print("decrypted text:",etext)
