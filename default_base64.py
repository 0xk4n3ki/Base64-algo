set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def index(a):
    if(a == "="):
        return 0
    else:
        return set.find(a)

def encrypt(t):
    cipher = ""
    rem = len(t) % 3
    for i in range(0, len(t) - rem, 3):
        a = bin(ord(t[i]))[2:]
        b = bin(ord(t[i+1]))[2:]
        c = bin(ord(t[i+2]))[2:]
        if(len(a) <= 8):
            a = "0" * (8-len(a)) + a
        if(len(b) <= 8):
            b = "0" * (8-len(b)) + b
        if(len(c) <= 8):
            c = "0" * (8-len(c)) + c
        hexValue = a + b + c
        cipher += set[int(hexValue[0:6], 2)] + set[int(hexValue[6:12], 2)] + set[int(hexValue[12:18], 2)] + set[int(hexValue[18:24], 2)]
    if(rem == 1):
        a = bin(ord(t[len(t)-1]))[2:]
        if(len(a) <= 8):
            a = "0" * (8-len(a)) + a
        hexValue = a + "0" * 4
        cipher += set[int(hexValue[0:6], 2)] + set[int(hexValue[6:12], 2)] + "=="
    elif(rem == 2):
        a = bin(ord(t[len(t) - 2]))[2:]
        b = bin(ord(t[len(t) - 1]))[2:]
        if(len(a) <= 8):
            a = "0" * (8-len(a)) + a
        if(len(b) <= 8):
            b = "0" * (8-len(b)) + b
        hexValue = a + b + "0" * 2
        cipher += set[int(hexValue[0:6], 2)] + set[int(hexValue[6:12], 2)] + set[int(hexValue[12:18], 2)] + "="
    return cipher

def decrypt(t):
    text = ""
    hexValue = ""
    for i in t:
        a = bin(index(i))[2:]
        hexValue += "0" * (6 - len(a)) + a
    rem = len(hexValue) % 32
    if(rem != 0):
        hexValue += "0" * (32 - rem)
    for i in range(0, len(hexValue), 8):
        text += chr(int(hexValue[i:i+8], 2))
    return text

def main():
    a = input("[+] Enrypt or Decypt(e/d)... ")

    # if user give input other than e or d
    if(str(a) != "e" and str(a) != "d"):
        print("[+] Enter e or d :)")
        return 0

    # user input
    f = "[+] Enter the text to "
    if(a=="e"):
        d = "Encrypt : "
    else:
        d = "Decrypt : "
    userInput = input(f + d)

    if(a=="e"):
        cipher =  encrypt(userInput)
        print(f"[+] Encrypted cipher : {cipher}")
    else:
        text =  decrypt(userInput)
        print(f"[+] Decrypted text : {text}")

if __name__ == "__main__":
    main()
