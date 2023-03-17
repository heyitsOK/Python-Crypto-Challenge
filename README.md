# Python Crypto Challenge
This project consists of two parts that demonstrate the security vulnerabilities of encrypting data in AES ECB and CBC modes.

## Part 1 - Extracting Plaintext from AES CBC Mode Ciphertext
In this part, I implemented a Python function get_plaintext() that takes a byte string ciphertext that has been encrypted in AES CBC mode and extracts the plaintext using a decrypt function that uses AES ECB mode. This showcases the vulnerability of AES CBC mode to plaintext injection attacks.

## Part 2 - Image Encryption with AES ECB and CBC Modes
In this part, I implemented two Python functions ecb_penguin() and cbc_penguin() which both encrypt an image using AES ECB and CBC modes respectively. The header and trailing bytes are reconnected to the encrypted ciphertext, and the image is visible. This demonstrates how the use of AES ECB mode can lead to visible patterns in encrypted images, while AES CBC mode can be vulnerable to padding oracle attacks.

---

Overall, this project serves as a reminder of the importance of choosing secure encryption modes and understanding their limitations.
