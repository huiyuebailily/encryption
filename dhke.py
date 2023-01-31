class DHKE_User:

    def __init__(self, private_key):
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self, p, g):
        # alternatively you can do (g**self.private_key % p) but it will be much slower when dealing with large numbers
        # look up how pow is implemented in python if you are interested :)
        return pow(g, self.private_key, p)

    def generate_full_key(self, other_partial_key, p):
        self.full_key = pow(other_partial_key, self.private_key, p)


def encrypt_message(message, key):
    encrypted_message = ""

    for character in message:
        encrypted_message += chr(ord(character) + key)

    return encrypted_message


# TODO: implement this function based on how encrypt_message works
# HINT: Look up chr() and ord()
def decrypt_message(encrypted_message, key):

    pass


if __name__ == "__main__":
    p = 151
    g = 9

    Alice = DHKE_User(20)
    Bob = DHKE_User(17)

    en_message = "[[~~omr\[£ [©­´«¯¤ª©[± ­±¤ ²[­ ® ©¯¯¤ª©[¤®[¯£ " \
                 "[ ®¯[«­ ® ©¯¯¤ª©[[£± [ ± ­[£\[ud"

    # TODO: decrypt the message
    original_message = None
