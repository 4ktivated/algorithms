import string

def valid_pass(passwor):
    dig = 0
    u_w = 0
    l_w = 0
    for char in password:
        if char in string.digits:
            dig += 1
        elif char in string.ascii_lowercase:
            l_w += 1
        elif char in string.ascii_uppercase:
            u_w +=1
    if u_w > 0 and l_w > 0 and dig > 0:
            return 'YES'
    else:
        return 'NO'


password = 'abcABC9'
print(valid_pass(password))