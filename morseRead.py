
import sys, os
from PIL import Image

def get_refined_image():
    #This is going to take the file and turn it into a workable picture.
    im = Image.open(sys.argv[1])
    im.load()
    rbg_im = im.convert('RGB')

    return rbg_im


def get_morse(im_info):
    last_found = 0
    current = 0
    ascii_chars = ""
    pix = im_info.load()

    for i in range(0, im_info.size[1]):
        for j in range(0, im_info.size[0]):
            if pix[j,i] != (0,0,0):
                current = j+(i*100)
                ascii_chars += chr(current - last_found)
                last_found = current

    ascii_chars = ascii_chars.strip().split(' ')
    print(ascii_chars)
    return ascii_chars

def moorse_ciper(raw,invert):
        code = {'A': '.-','B': '-...','C': '-.-.',
        'D': '-..','E': '.','F': '..-.',
        'G': '--.','H': '....','I': '..',
        'J': '.---','K': '-.-','L': '.-..',
        'M': '--','N': '-.','O': '---',
        'P': '.--.','Q': '--.-','R': '.-.',
     	'S': '...','T': '-','U': '..-',
        'V': '...-','W': '.--','X': '-..-',
        'Y': '-.--','Z': '--..',
        '0': '-----','1': '.----','2': '..---',
        '3': '...--','4': '....-','5': '.....',
        '6': '-....','7': '--...',  '8': '---..',
        '9': '----.'
        }
        translated = ""

        if invert:
            code = dict([[v,k] for k,v in code.items()])

        for elm in raw:
            try:
                translated += code[elm]
            except:
                translated += ' '

        return translated

def main():
    im = get_refined_image()
    morse_list = get_morse(im)

    print(moorse_ciper(morse_list, True))

    test = ".- / - . ... -".split(' ')
    print('Test: '+moorse_ciper(test,True))

main()
