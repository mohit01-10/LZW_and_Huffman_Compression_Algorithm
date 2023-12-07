import os
import base64
import time

def compress_and_decompress_lzw():
    from LZW_Compressor import LZWCompression
    path="Binary_Files_before_Compression/"
    start_time = time.time()
    for i in os.listdir(path):

        if not "DS_Store" in i:
            file_name,file_extension=os.path.splitext(""+i)

            file= LZWCompression(path+i)
            print('Compressing , please wait!!')
            compressed_file_path=file.compress()
            print('Location of compressed file : ',compressed_file_path,"\n")
        
            print('Decompressing , please wait!!')
            decompressed_file_path=file.decompress(compressed_file_path)
            print('Location of decompressed file : ',decompressed_file_path)

    for i in os.listdir("LZW_files/Binary_Files_after_Decompression/"):
        if not "DS_Store" in i:
            file_name,file_extension=os.path.splitext("LZW_files/Binary_Files_after_Decompression/"+i)

            string=""
            for ch in i:
                if (ch!="_"):
                    string=string+ch
                else:
                    break
        
            r = open((file_name+file_extension), "rb")
            fh=open(("LZW_files/Files_After_Conversion/"+string),"wb")
            abcd=r.read()
            fh.write(base64.decodebytes(abcd))
            fh.close()
            r.close()

    end_time = time.time()
    size=0
    for i in os.listdir("LZW_files/Binary_Files_after_Decompression"):
        if not "DS_Store" in i:
            stat=os.stat("LZW_files/Binary_Files_after_Decompression/"+i)
            size=size+stat[6]
    print("Size of All Binary files before Compression is " ,(size) , " Bytes or " ,(size/1024), " KB (KiloBytes)")

    size1=0
    for i in os.listdir("LZW_files/Binary_Files_after_LZW_Coding"):
        if not "DS_Store" in i:
            stat=os.stat("LZW_files/Binary_Files_after_LZW_Coding/"+i)
            size1=size1+stat[6]

    print("\nSize of All Binary files After Compression is " ,(size1), " Bytes or ",(size1/1024)," KB (KiloBytes)")
    saved=size-size1
    print("Thus Space saved = ",(saved) ," Bytes or ",(saved/1024)," KB (KiloBytes)\n\n")
    p=saved/size*100
    r1=round(p)
    print("Thus percentage of space saved = " ,(p) ," % \n")
    print("Which is approximately " ,(r1) ,"%\n\n" )

    elapsed_time = end_time - start_time
    print("Time taken for LZW Compression and Decompression: {:.4f} seconds\n".format(elapsed_time))

def compress_and_decompress_huffman():
    from Huffman_Compressor import huffmanCoding
    path="Binary_Files_before_Compression/"
    start_time = time.time()
    for i in os.listdir(path):
    
        if not "DS_Store" in i:
            file_name,file_extension=os.path.splitext(""+i)
        
            file=huffmanCoding(path+i)
            print('Compressing , please wait!!')
            compressed_file_path=file.compress()
            print('Location of compressed file : ',compressed_file_path,"\n")
            print('Decompressing , please wait!!')
            decompressed_file_path=file.decompress(compressed_file_path)
            print('Location of decompressed file : ',decompressed_file_path)

    for i in os.listdir("Huffman_files/Binary_Files_after_Decompression/"):
        if not "DS_Store" in i:
            file_name,file_extension=os.path.splitext("Huffman_files/Binary_Files_after_Decompression/"+i)
            #print(i)
            string=""
            for ch in i:
                if (ch!="_"):
                    string=string+ch
                else:
                    break
            
            r = open((file_name+file_extension), "rb")
            fh=open(("Huffman_files/Files_After_Conversion/"+string),"wb")
            abcd=r.read()
            fh.write(base64.decodebytes(abcd))
            fh.close()
            r.close()

    end_time = time.time()    
    size=0
    for i in os.listdir("Huffman_files/Binary_Files_after_Decompression"):
        if not "DS_Store" in i:
            stat=os.stat("Huffman_files/Binary_Files_after_Decompression/"+i)
            size=size+stat[6]
    print("Size of All Binary files before Compression is " ,(size) , " Bytes or " ,(size/1024), " KB (KiloBytes)")

    size1=0
    for i in os.listdir("Huffman_files/Binary_Files_after_Huffman_Coding"):
        if not "DS_Store" in i:
            stat=os.stat("Huffman_files/Binary_Files_after_Huffman_Coding/"+i)
            size1=size1+stat[6]
    print("\nSize of All Binary files After Compression is " ,(size1), " Bytes or ",(size1/1024)," KB (KiloBytes)")
    saved=size-size1
    print("Thus Space saved = ",(saved) ," Bytes or ",(saved/1024)," KB (KiloBytes)\n\n")
    p=saved/size*100
    r2=int(p)
    print("Thus percentage of space saved = " ,(p) ," % \n")
    print("Which is approximately " ,(r2) ,"%\n\n" )
    elapsed_time = end_time - start_time
    print("Time taken for Huffman Compression and Decompression: {:.4f} seconds\n".format(elapsed_time))


def main():
    for i in os.listdir("Files_To_Compress_or_Convert"):
   
        if "." in i:
            if not "DS_Store" in i:
                file_name,file_extension=os.path.splitext("Files_To_Compress_or_Convert/"+i)

            with open((file_name+file_extension), "rb") as a:
                with open(("Binary_Files_before_Compression/"+i+"_Binary_Text_File.txt"),"wb") as w:
                    str = base64.encodebytes(a.read())
                    w.write(str)

    while True:
        print("\nChoose Compression Algorithm:")
        print("1. LZW Compression")
        print("2. Huffman Compression")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            print("\nUsing LZW Compression Algorithm\n")
            compress_and_decompress_lzw()
        elif choice == "2":
            print("\nUsing Huffman Compression Algorithm\n")
            compress_and_decompress_huffman()
        elif choice == "3":
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()