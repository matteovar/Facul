import rsa

(pub_key, priv_key) = rsa.key.newkeys(330)
mensagem = b'32158238Matteo'
crypto = rsa.encrypt(mensagem, pub_key)
mensagem = rsa.decrypt(crypto, priv_key)
print("Mensagem criptografada: ", crypto)
print('**********************************')
print('Mensagem descriptografada: ',mensagem)

