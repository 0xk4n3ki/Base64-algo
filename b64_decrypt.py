import base64

s = ""

custom = "CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab0123456789+/"
default = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

example = "dYHuf2HaBS=="

for i in example:
    if(i in custom):
        s += default[custom.find(i)]
    elif(i == "="):
        s += "="

s = s.encode('utf-8')
print(base64.b64decode(s))
