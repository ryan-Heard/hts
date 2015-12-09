
from PIL import Image
import os

def get_image_info():
    command =  'cd %HOMEPATH%\Pictures && cd'
    findFolder = os.popen(command).read().strip()
    fileFound = findFolder +'/'+'test.jpg' #have this be some kind of raw


import sys, os
from PIL import Image

def get_refined_image(arg):
    #This is going to take the file and turn it into a workable picture.
    im = Image.open(arg)
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
    for line in sys.argv[1:]:
        im = get_refined_image(line)
        morse_list = get_morse(im)

        print(moorse_ciper(morse_list, True))

main()
