

# Explanation video: http://youtu.be/sxFIxD8Gd3A
 

 
plain_text = "This is a test. ABC abc"
 
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)