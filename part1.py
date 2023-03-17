#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = AES.block_size


def decrypt(ciphertext: bytes) -> bytes:
    key = bytes.fromhex("2c4b295fe9ca7c02208e22d25e2875a8")
    cipher = AES.new(key, AES.MODE_ECB)

    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        print(f"ERROR: {e}")
        return -1

    return decrypted


def encrypt(plaintext: bytes) -> bytes:
    key = bytes.fromhex("2c4b295fe9ca7c02208e22d25e2875a8")
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted = cipher.encrypt(plaintext)
    ciphertext = iv + encrypted

    return ciphertext


def get_plaintext(ciphertext: bytes):
    """
        I started by storing the iv in a variable as it is prefixed to the ciphertext. Next I calculated
        how many sets of BLOCK_SIZE bytes there were in the ciphertext and storing that in length. Then
        I looped in the range of 1 - length and decrypted ciphertext blocks using BLOCK_SIZE multiplied
        by i. I then XORed the decrypted data with the iv, updated the plaintext and the iv, and looped
        until I reached the end of the ciphertext. Finally I returned plaintext
    """
    iv = ciphertext[:BLOCK_SIZE]
    plaintext = b""
    length = (len(ciphertext[BLOCK_SIZE:]) // BLOCK_SIZE) + 1
    print(length)
    for i in range(1, length):
        decrypted = decrypt(ciphertext[BLOCK_SIZE*i:BLOCK_SIZE*(i+1)])
        xored = bytes([x ^ y for (x,y) in zip(decrypted,iv)])
        plaintext += xored
        iv = ciphertext[BLOCK_SIZE*i:BLOCK_SIZE*(i+1)]
    return plaintext


if __name__ == "__main__":
    key = get_random_bytes(BLOCK_SIZE)
    plaintext = b"comp3109_3cb_5uck5_4v01d_17!!!!!"
    ciphertext = encrypt(plaintext)

    decrypted = get_plaintext(ciphertext)
    print(decrypted)
    assert decrypted == plaintext
