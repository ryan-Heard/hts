from PIL import Image
import os



def get_image_info():
    command =  'cd %HOMEPATH%\Pictures && cd'
    findFolder = os.popen(command).read().strip()
    fileFound = findFolder +'/'+'TEST.jpg' #have this be some kind of raw

    im = Image.open(fileFound)


    print(im.mode)
    print(os.path.isfile(fileFound) )

    return im


def get_positions(im_info):
    last_found = 0
    current = 0
    ascii_chars = []
    pix = im_info.load()

    '''
    for i in range(0, im_info.size[0]):
        for j in range(0,im_info.size[1]):
            if pix[i,j] == (255,255,255):
                current = (i*100)+j
                ascii_chars.append(chr(current - last_found)) #append char equiv.
                print(current - last_found)
                last_found = current
    '''

    return ascii_chars

info = get_image_info()
print(info.size)
refined_output = get_positions(info)

#print(refined_output)





#im = Image.open("dead_parrot.jpg") #Can be many different formats.
#pix = im.load(
