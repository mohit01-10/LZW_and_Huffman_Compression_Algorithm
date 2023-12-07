<h1>LZW Coding Compression Project</h1>

This project uses LZW Coding Algorithm to Compress the size of any file by 25%

It can be any file whether JPEGs, PNGs, PDFs, Word files, Excel Files, PPTs, MP3 files, MP4 files, MKV files, JSON Files  etc

As we all know in today's age when photos and videos are all over the internet and social media and people share them on whatsapp, email etc, so reducing the size of all files is a huge boon.

I have used OS library, base64 library among other libraries in this project.

In this project, first we convert any type of files to binary text files. 

Then we apply LZW Coding Algorithm and compress the text files

By doing this the files sizes are reduced by 25% and thus files can easily be sent to others.

Then after receiving, they have to decompressed. So I have built a program to decompress the files also.

And then finally the decompressed binary text files are converted to their original formats so that the receiver can view them.

Also the program shows the size of binary text files before and after compression by LZW Coding and tells us how much space has been saved by compression and it's percentage

To comress any files, put them in the folder names "Files_To_Compress_or_Convert". Some sample files are already in that folder.

And then write this in command line

python Project_Main.py

OR (On Mac)

python3 Project_Main.py
