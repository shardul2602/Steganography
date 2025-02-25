from PIL import Image
import argparse
import binascii

def text_to_binary(text):
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text + '1111111111111110'  # Delimiter to mark the end

def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 254)

def encode_image(input_image, output_image, secret_text):
    image = Image.open(input_image)
    pixels = image.load()
    width, height = image.size
    binary_text = text_to_binary(secret_text)
    data_index = 0
    
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            for i in range(3):
                if data_index < len(binary_text):
                    pixel[i] = (pixel[i] & ~1) | int(binary_text[data_index])
                    data_index += 1
            pixels[x, y] = tuple(pixel)
            if data_index >= len(binary_text):
                image.save(output_image)
                print(f"Text successfully hidden in {output_image}")
                return
    print("Error: Image size too small to hide the text!")

def decode_image(encoded_image):
    image = Image.open(encoded_image)
    pixels = image.load()
    width, height = image.size
    binary_text = ""
    
    for y in range(height):
        for x in range(width):
            for i in range(3):
                binary_text += str(pixels[x, y][i] & 1)
    
    delimiter = "1111111111111110"
    if delimiter in binary_text:
        binary_text = binary_text[:binary_text.index(delimiter)]
        hidden_text = binary_to_text(binary_text)
        print("Hidden text:", hidden_text)
    else:
        print("No hidden text found!")

def main():
    parser = argparse.ArgumentParser(description='Steganography CLI Tool')
    parser.add_argument('mode', choices=['encode', 'decode'], help='Mode: encode to hide text, decode to retrieve text')
    parser.add_argument('--input', required=True, help='Input image path')
    parser.add_argument('--output', help='Output image path (required for encoding)')
    parser.add_argument('--text', help='Text to hide (required for encoding)')
    
    args = parser.parse_args()
    
    if args.mode == 'encode':
        if not args.output or not args.text:
            print("Error: Encoding requires --output and --text arguments.")
            return
        encode_image(args.input, args.output, args.text)
    elif args.mode == 'decode':
        decode_image(args.input)

if __name__ == '__main__':
    main()
