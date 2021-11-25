import hashlib
text = input() # Строка
byte_text = text.encode() # Переводим в байты
hash_text_sha256 = hashlib.sha256(byte_text).hexdigest()
hash_text_sha384 = hashlib.sha384(byte_text).hexdigest()
hash_text_sha512 = hashlib.sha512(byte_text).hexdigest()
# Можно или так
#hash_text_sha256 = hashlib.sha256(text.encode()).hexdigest() # или так, но данный вариант используется чаще
print('sha256:', hash_text_sha256)
print('sha384:', hash_text_sha384)
print('sha512:', hash_text_sha512)
