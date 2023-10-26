import zlib

message = b"she sells sea shells on the sea shore. the shells that she sells are sea shells, i'm sure."
print(len(message))

compressed_message = zlib.compress(message)
print(compressed_message)
print(len(compressed_message))

decompressed_message = zlib.decompress(compressed_message)
print(decompressed_message)
print(len(decompressed_message))

print(message == decompressed_message, message is decompressed_message)
