# Affine chipper
# rumus affine chipper = (a*x + b) % m

# mengubah password menjadi bentuk chippered
def encrypt(password):
    encrypted = ''

    for c in password:
        a = 8;  b = 3;   m = 95
        x = ord(c) - 32
        ex = chr(((a * x + b) % m) + 32)
        if c == '#': ex = '='
        encrypted += ex

    return encrypted


# mengubah bentuk chippered menjadi password semula
def decrypt(encrypted):
    decrypted = ''

    for c in encrypted:
        a = 12
        b = 3
        m = 95
        x = ord(c) - 32
        dx = chr((a * (x - b) % m) + 32)
        if c == '=': dx = '#'
        decrypted += dx

    return decrypted