input_data = 'data'
encoded = ''.join([chr(ord(c)^0xAA) for c in input_data])
print(encoded)