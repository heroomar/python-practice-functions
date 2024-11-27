import random

def genarate_pass(len):
    out=''
    for i in range(len):
        out += chr(random.randrange(21,125))
    return out

n=int(input("Enter length of password to generate: "))
print("Password: ", genarate_pass(n))
