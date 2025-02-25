# Steganography CLI Tool

A simple command-line application to hide and retrieve text from images using **LSB (Least Significant Bit) Steganography**.

## Features
- Encode (hide) secret text inside an image.
- Decode (extract) hidden text from an image.
- Works with common image formats like **JPG, PNG, BMP**.

## Prerequisites
Ensure you have **Python 3.x** installed on your system.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shardul2602/Steganography.git
   cd Steganography
   ```
2. Install required dependencies:
   ```sh
   pip install pillow
   ```

## Usage

### Encode (Hide Text in an Image)
```sh
python steganography.py encode --input input.jpg --output encoded.png --text "Your Secret Message"
```
- `--input` : Original image file.
- `--output` : Output image file with hidden text.
- `--text` : Message to hide.

### Decode (Extract Hidden Text)
```sh
python steganography.py decode --input encoded.png
```
- `--input` : Encoded image file containing hidden text.

## Example
**Hiding Text:**
```sh
python steganography.py encode --input image.jpg --output secret.png --text "Hidden message here"
```

**Retrieving Text:**
```sh
python steganography.py decode --input secret.png
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Repository
GitHub Repository: [Steganography](https://github.com/shardul2602/Steganography.git)

