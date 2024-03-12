# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:06:58 2024

@author: Leen
"""
import lea
import elgamal
import rsa
import numpy as np
import math
import random
from tinyec import registry
from tinyec import ec
import secrets 



class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

def get_bin(number: int, n: int)-> str:
    '''Returns binary representation of number filled with 0's to length n'''
    return bin(number)[2:].zfill(n)

def get_random_bits(n: int) -> str:
    '''Returns sequence of random bits of length n'''
    i = random.randint(0,pow(2,n)-1)
    bin_key = get_bin(i,n)
    return bin_key

def compress(publicKey):
    return (hex(publicKey.x)) + (hex(publicKey.y % 2)[2:])


def main():
    
    ################################# Generate plaintext #################################
    # Generate random plaintext of size 128
    # P = hex(int(get_random_bits(256), 2))

    ################################# EC & ElGamal #################################
    # curve.g : Base Point
    curve = registry.get_curve('brainpoolP160r1') 
    # Ka, Kb : alice and bob's private keys
    Ka = secrets.randbelow(curve.field.n) # alice's private key
    Kb = secrets.randbelow(curve.field.n) # bob's private key

    # (y1,y2)
    y1 = Ka * curve.g # alice's public key
    # for this part the plaintext P is a point on the curve
    #y2 = curve.g
    EC_Point = Point()
    EC_Point.x = 0x4A92BDA82A2E168896D94D428A08F7CCF443B04129999AC646F18115C6D353868
    EC_Point.y = 0x21FB819707ECA9EF71075C3EED28C726694AEC06AADC8052A60B7AA29E3A1063
    #y2 = compress(EC_Point) + compress(Ka*(Kb * curve.g))
    # print(EC_Point.x)
    # x = ec.Point(curve, 0x4A92BDA82A2E168896D94D428A08F7CCF443B04129999AC646F18115C6D353868, 0x21FB819707ECA9EF71075C3EED28C726694AEC06AADC8052A60B7AA29E3A1063)
    # print(type(x))
    
   

# Example coordinates
    # print(type(y2))
    # print(type(y1))
    ################################# LEA #################################
    LEA_Key = get_random_bits(128) # get symmetric key
    P = get_random_bits(128)
    # now we encrypt the symmetric key using bob's public key
    #C = lea.lea_encrypt(P,LEA_Key)

    # # now encrypt LEA key with bob's public key
    # CK = lea.lea_encrypt(LEA_Key,Kb * curve.g)

    # # Sign Ciphertext with Alice's secret key
    # S = lea.lea_encrypt(C,Ka * curve.g)
    
    # Alice sends S, C, CK to bob ..
    # now bob has to verify 
  


if __name__ == "__main__":
    main()
