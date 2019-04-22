__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
import string
def start_vowel(str):
    k=1
    if str[0] in string.ascii_uppercase:
        k=0
        str=str.lower()
    str=list(str)
    s=list()
    if str[-1] not in string.ascii_letters:
        s=str[0:-1]
        s.append('a')
        s.append('y')
        s.append(str[-1])
        str=s
    else:
        str.append('a')
        str.append('y')
    if k==0:
        str[0]=str[0].upper()
    str="".join(str)
    return str

def start_consonant(str):
    p=1
    if str[0] in string.ascii_uppercase:
        p=0
        str=str.lower()
    r=list()
    for i in range(len(str)):
        if str[i] not in ['a','e','i','o','u']:
            r.append(str[i])
        else:
            break
    if str[-1] not in string.ascii_letters:
        k = list(str[i:-1])
        for j in r:
            k.append(j)
        k.append('ay')
        k.append(str[-1])
        if p == 0:
            k[0] = k[0].upper()
    else:
        k=list(str[i:])
        for j in r:
            k.append(j)
        k.append('ay')
        if p==0:
            k[0]=k[0].upper()
    k="".join(k)
    return k


def pig_latin(str):
    l=len(str)
    result=list()
    for i in range(l):
        if str[i][0] in ['a','e','i','o','u']:
            if i==0:
                result.append(start_vowel(str[i]))
            else:
                result.append(start_vowel(str[i]))
        else:
            result.append(start_consonant(str[i]))
    result=" ".join(result)
    print(result)
def main(argv=None):

    try:

        while True:
            l=input()
            l=l.split()
            pig_latin(l)

    except KeyboardInterrupt as e:
        print(e, file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())