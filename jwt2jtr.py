#########################################################################################
# Title: JWT2JTR
# Author: Marco Lugo
# Description: takes in a JWT (JSON Web Tokens) token and converts it into a format
#	       that can be directly fed into John the Ripper (JTR) to crack the 
#              HMAC-SHA256 key.
#
#	       Please note that as of March 2018, not all JWT hashes are supported by
#	       JTR. Hashcat may be a good alternative.
#
# Example usage:
#
# python jwt2jtr.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ.-xN_h82PHVTCMA9vdoHrcZxH-x5mb11y1537t3rGzcM
# output:           eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiJiMDhmODZhZi0zNWRhLTQ4ZjItOGZhYi1jZWYzOTA0NjYwYmQifQ#fb137f87cd8f1d54c2300f6f7681eb719c47fb1e666f5d72d79dfbb77ac6cdc3
#########################################################################################


import sys
import base64
import binascii


jwt_input = sys.argv[1]
jwt_parts = jwt_input.split('.')


if len(jwt_parts) != 3:
    print 'ERROR: JWT must have header, payload and signature.'
    exit(-1)


def jwt_decode(jwt_encoded):
    jwt_encoded += '=' * (-len(jwt_encoded) % 4) #add padding if necessary
    return base64.urlsafe_b64decode(jwt_encoded)

def hex_signature(jwt_encoded):
    jwt_decoded = jwt_decode(jwt_encoded)
    return binascii.hexlify(jwt_decoded)


if __name__ == '__main__':
    jtr = jwt_parts[0] + '.' + jwt_parts[1] + '#' + hex_signature(jwt_parts[2])
    print jtr
