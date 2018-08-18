import string #use this package
#Simple letter substitution cipher that replaces with 'n' letter after it

def decode_rot(n, cipher_text):
  result = ""
  abc = list(string.ascii_lowercase)
  fieldset = list(string.ascii_lowercase)
  for i in range(n):
      fieldset += abc
  for i in list(cipher_text):
      current = abc.index(i)
      letter = fieldset[current + n]
      result += letter
  print('Decoding ROT %s result is: %s ' %(n, result))

print(50*"*")
decode_text = "czggjrjmgy"
print("Text to decode: %s" % decode_text)
print(50*"*")

decode_rot(5, decode_text)
