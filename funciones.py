def char_to_byte(char):
   
   return format(ord(char), '#010b')[-8:]

def word_to_bytes(word):
   
   bytes_list = [char_to_byte(char) for char in word]
   return ' '.join(bytes_list)

def byte_to_ascii(byte_str):
   
   decimal = int(byte_str, 2)
   return chr(decimal) + ":" + str(int(byte_str, 2))

