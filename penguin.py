#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

BLOCK_SIZE = AES.block_size


def ecb_penguin(key: bytes, img: bytes) -> bytes:
    """
        I start by setting up my AESCipher object, next I save the image header in my header variable
        to add back on later. After that, I calculate how many sets of 16 bytes there are in the data
        portion of the file (header is 54 bytes so I just slice img accordingly) and store that info in
        my length variable. Then I loop through and encrypt the image 16 bytes at a time with an offset of 54 
        bytes and append the encrypted data to my encrypted variable. Finally I can return the header + encrypted
        data + trailing bytes at the end.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    header = img[:54]
    length = len(img[54:]) // 16
    encrypted = b""
    for i in range(length):
        start = i * 16 + 54
        encrypted += cipher.encrypt(img[start:start+16])

    return header+encrypted+img[length*16:]

        
def cbc_penguin(key: bytes, iv: bytes, img: bytes) -> bytes:
    """
        I start by setting up my AESCipher object, next I save the image header in my header variable
        to add back on later. After that, I use cipher.encrypt and pass in the img data using the pad
        to ensure the correct size. Then I calculate how many sets of 16 bytes there are in the data
        portion of the file (header is 54 bytes so I jsut slice img accordingly) and store that info in
        my length variable. Finally I can return the header + encrypted data + trailing bytes at the end.
    """
    assert iv is not None

    cipher = AES.new(key, AES.MODE_CBC, iv)
    header = img[:54]
    encrypted = cipher.encrypt(pad(img[54:], AES.block_size))
    length = len(img[54:]) // 16
    return header+encrypted+img[length*16:]




if __name__ == "__main__":
    key = b"3109SaysAvoidECB"

    with open("tux.bmp", "rb") as f:
        img = f.read()

    with open("ecb_tux.bmp", "wb") as f:
        ciphertext = ecb_penguin(key, img)
        f.write(ciphertext)

    iv = get_random_bytes(AES.block_size)
    with open("cbc_tux.bmp", "wb") as f:
        ciphertext = cbc_penguin(key, iv, img)
        f.write(ciphertext)
