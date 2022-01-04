# Implementation of caesar cipher
# Author: Diamond Mohanty
# Date: 04-Jan-2022

class CaesarCipher():
    def __init__(self, shift: int) -> None:
        self._shift = shift
        self._encoder = [None] * 26
        self._decoder = [None] * 26

        for idx in range(len(self._encoder)):
            self._encoder[idx] = chr(ord('A') + (idx + shift) % 26)
            self._decoder[idx] = chr((idx - shift) % 26 + ord('A'))
        
    
    def encrypt(self, text: str) -> str:
        tmp = list(text)
        for i in range(len(tmp)):
            if tmp[i].isupper():
                tmp[i] = self._encoder[ord(tmp[i]) - ord('A')]
        
        return ''.join(tmp)

    def decrypt(self, text: str) -> str:
        tmp = list(text)
        for i in range(len(tmp)):
            if tmp[i].isupper():
                tmp[i] = self._decoder[ord(tmp[i]) - ord('A')]
        
        return ''.join(tmp)


# Test Code
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."

cipher = CaesarCipher(3)
cipher_text = cipher.encrypt(message)
print('Encrypted Text: ', cipher_text)
print('Decrypted Text: ', cipher.decrypt(cipher_text))