#!/usr/bin/python3
""" Module contains validUTF8 function """


def validUTF8(data):
    """ Determine if a given data set represents a valid UTF-8 encoding """
    following_bytes = 0

    for byte in data:
        byte &= 255

        if following_bytes == 0:
            if byte >> 7 == 0:
                following_bytes = 0
            elif byte >> 5 == 0b110:
                following_bytes = 1
            elif byte >> 4 == 0b1110:
                following_bytes = 2
            elif byte >> 3 == 0b11110:
                following_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            following_bytes -= 1

    return following_bytes == 0
