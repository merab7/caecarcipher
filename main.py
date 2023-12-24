import sys

def enigma():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt :   ").lower()

    if direction not in ['encode', 'decode']:
        print("\n\nPlease check your spelling. You only have two options: 'encode' to encrypt and 'decode' to decrypt.")
        return enigma()

    text_in = input("\nType your message:\n").lower()
    shift = int(input("\n\nType the shift number:\n"))
    
    def again_in():
        again = input("\n\nIf you want to continue, press 'Y' to cantinue or X to exit :   ")
        
        if again.lower() =="y":
            return enigma()
        elif again.lower() == "x":
            sys.exit()
        else:
            print("\n\nPlease check your spelling. You only have two options: 'Y' to cantinue or X to exit.")
            return again_in()
    
    def encode(text):
        encoded_text = ""
        for x in text:
            if x in alphabet:
                index_x = alphabet.index(x)
                if index_x + shift < len(alphabet):
                    x = alphabet[index_x + shift]
                else:
                    x = alphabet[(index_x + shift) - len(alphabet)]
                encoded_text += x
            else:
                encoded_text += x
        
        print(encoded_text)
        again = again_in()
        if again.lower() == "x":
            sys.exit()

    def decode(text):
        decoded_text = ""
        for x in text:
            if x in alphabet:
                index_x = alphabet.index(x)
                x = alphabet[index_x - shift]
                decoded_text += x
            else:
                decoded_text += x

        print(decoded_text)
        again = again_in()
        if again.lower() == "x":
            sys.exit()

    if direction == "encode":
        encode(text_in)
    elif direction == "decode":
        decode(text_in)

enigma()
