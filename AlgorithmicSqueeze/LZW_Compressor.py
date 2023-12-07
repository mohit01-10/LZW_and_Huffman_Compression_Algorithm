
# In[ ]:

import os

class LZWCompression:

    def __init__(self, path):
        self.path = path
        self.dictionary = {chr(i): i for i in range(256)}

    def compress(self):
        filename, extension = os.path.splitext(self.path)
        string = ""
        length = len(filename)
        for i in range(length - 1, 0, -1):
            if filename[i] != "/":
                string = string + filename[i]
            else:
                break
        string2 = "".join(reversed(string))
        output_path = "LZW_files/Binary_Files_after_LZW_Coding/" + string2 + "_compressed.bin"

        with open(self.path, 'r') as file, open(output_path, 'wb') as output:
            text = file.read().rstrip()
            compressed_text = self.lzw_compress(text)
            output.write(compressed_text)

        print('Compressed')
        return output_path

    def decompress(self, input):
        filename, extension = os.path.splitext(self.path)
        string = ""
        length = len(filename)
        for i in range(length - 1, 0, -1):
            if filename[i] != "/":
                string = string + filename[i]
            else:
                break
        string2 = "".join(reversed(string))
        output_path = "LZW_files/Binary_Files_after_Decompression/" + string2 + "AfterConversionAndDecoding.txt"

        with open(input, 'rb') as file, open(output_path, 'w') as output:
            compressed_text = file.read()
            decompressed_text = self.lzw_decompress(compressed_text)
            output.write(decompressed_text)

        print('Decompressed')
        return output_path

    def lzw_compress(self, text):
        compressed_text = bytearray()
        current_code = 256
        dictionary = self.dictionary.copy()
        buffer = ""
        for char in text:
            buffer += char
            if buffer not in dictionary:
                dictionary[buffer] = current_code
                current_code += 1
                buffer = buffer[:-1]
                compressed_text.extend(self.int_to_bytes(dictionary[buffer]))
                buffer = char

        if buffer in dictionary:
            compressed_text.extend(self.int_to_bytes(dictionary[buffer]))

        return compressed_text

    def int_to_bytes(self, value):
        # Helper method to convert an integer to a byte array
        return value.to_bytes((value.bit_length() + 7) // 8 or 1, 'big')


    def lzw_decompress(self, compressed_text):
        decompressed_text = ""
        current_code = 256
        dictionary = {i: chr(i) for i in range(256)}
        buffer = chr(compressed_text[0])
        decompressed_text += buffer
        for code in compressed_text[1:]:
            if code in dictionary:
                entry = dictionary[code]
            elif code == current_code:
                entry = buffer + buffer[0]
            else:
                raise ValueError("Bad compressed code")
            decompressed_text += entry
            dictionary[current_code] = buffer + entry[0]
            current_code += 1
            buffer = entry
        return decompressed_text
