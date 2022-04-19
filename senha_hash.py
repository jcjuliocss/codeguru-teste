import bcrypt


senha_nova = str(raw_input('Nova senha: '))
print bcrypt.hashpw(senha_nova, bcrypt.gensalt())
