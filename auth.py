import bcrypt


password = b'12'
password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
password_hashed = str(password_hash, 'utf-8')
print(password_hash,'\n',password_hashed)
print(bytes(password_hashed, 'utf-8'))
print(len(password_hashed))

if bcrypt.checkpw(b'12', password_hash):
    print('match')
else:
    print('no match')
