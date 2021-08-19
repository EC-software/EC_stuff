from cryptography.fernet import Fernet

# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
print(f"key: {key}")
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(f"token: {token}")
clear = f.decrypt(token)
print(f"clear: {clear}")
