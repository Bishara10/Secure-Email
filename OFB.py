import lea
import random

# LEA encryption in OFB mode
def encryption_decryption_LEA_OFB(message: str, key: str, initialV: str, block_size: int):

    # Split message to blocks of 128 bits
    blocks = []
    msg = message # a copy of the message
    if (len(msg) < block_size):
        msg.zfill(block_size)
        blocks.append(msg)
    else:
        while(msg != ""):
            blocks.append(msg[:block_size])
            msg = msg[block_size:]
    
    if (len(blocks[-1]) < block_size):
        blocks[-1] = (blocks[-1]).zfill(block_size)
    
    # encrypt with LEA in blocks of 128 bits each
    next_iv = initialV
    n = len(blocks) # number of blocks

    #final ciphertext blocks
    C = ""

    # Perform LEA encryption on all blocks
    for i in range(n):
        # set initial vector for next block to be the current ciphertext with left shifting s_bits 
        next_iv = next_iv[block_size:] + next_iv[:block_size]
        # encrypt block with LEA 
        encryption = lea.lea_encrypt(block=next_iv, key=key)
        # print(encryption)


        # select first s bits from the encrypted text and from the plaintext
        e_s_bits = encryption[:block_size]
        p_s_bits = blocks[i][:block_size] 
        # xor sbits with original plaintext
        Ci = lea.XOR(e_s_bits, p_s_bits)

        # C.append(Ci)
        C += Ci

        # print(next_iv)

    # return ciphertext
    return C
