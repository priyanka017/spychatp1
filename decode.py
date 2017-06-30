from steganography.steganography import Steganography
count = 1
while count < 11:
    output_path = "secret" + str(count) + ".jpg"
    text = Steganography.decode(output_path)
    print("\n\nImage no - %d after decoding --- " % (count))
    print(text)
    count+=1
