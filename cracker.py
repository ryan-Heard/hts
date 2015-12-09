import sys
from collections import Counter

def get_words(files):
    words = [];

    with open(files) as f:
        content = f.read()
        content = content.split('.')

    for partial in range(1,len(content)-2,3):
        tup = (int(content[partial]),int(content[partial+1]),int(content[partial+2]))
        words.append(decode_words(tup))

    return words

def decode_words(tups):
    word_val = sum(tups)
    return word_val

def convert_to_ascii(value,key):
    value = value - key
    return chr(value)

def main():
    files = sys.argv[1:]

    for name in files:
        decoded = "";
        print('\n <=================[BEGIN DECODE OF '+name+']===========================>\n')
        chunks = get_words(name)
        data = Counter(chunks)
        key = data.most_common(1)[0][0] - 32

        for jumble in chunks:
            decoded += convert_to_ascii(jumble,key)

        print(decoded)

        print("\n <=====================[END]=======================>")
main()
