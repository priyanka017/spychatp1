from steganography.steganography import Steganography
original_image=raw_input("enter image name")
output_path=raw_input("enter output file name")
text=raw_input("enter your message")
Steganography.encode(original_image,output_path,text)
