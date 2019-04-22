__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
import unit6utils
import string
import inspect
import os
from unit6utils import get_temp_dir

def are_anagrams(first, second):
    if first==None or second==None:
        return False
    if len(first)==0 and len(second)==0 :
        return True
    first=first.lower()
    second=second.lower()
    second1=list(second)
    le=len(second)
    lf=len(first)
    for j in range(len(first)):
        if first[j]==" ":
            continue
        c=0
        k=0
        for i in range(len(second)):
            if second[i] == " ":
                continue
            elif second[i]==first[j]:
                k=i
                c=1
        if c==0:
            return False
        else:
            if k+1<len(second):
                second = second[:k]+second[k+1:]
            else:
                second=second[:k]

    l=j
    for j in range(len(second1)):
        if second1[j]==" ":
            continue
        c=0
        k=0
        for i in range(len(first)):
            if first[i] == " ":
                continue
            elif first[i]==second1[j]:
                k=i
                c=1
        if c==0:
            return False
        else:
            if k+1<len(first):
                first = first[:k]+first[k+1:]
            else:
                first=first[:k]
    if j==le-1 and l==lf-1:
        return True

    return False
def inside(l,r):
    o = 0
    for o in range(len(r)):
        if l in r[o]:
            return False
    return True
def for_grouping(source):
    f=open(source,"rt")
    l=f.readlines()
    lines=list()
    for i in range(len(l)):
        if l[i][0] in string.ascii_letters:
            p=l[i]
            lines.append(p)
    k=list(lines[-1])
    k.append("\n")
    lines.remove(lines[-1])
    k="".join(k)
    lines.append(k)
    r=list()
    j=0
    while j in range(len(lines)):
        i=0
        a=0
        while i in range(j,len(lines)):
            if i!=j:
                d=0
                m=list()
                if are_anagrams(lines[j],lines[i]):
                    a=1
                    if inside(lines[i],r):
                        m.append(lines[i])
                        lines.remove(lines[i])
                        i=i-1
                    else:
                        o=0
                        d=1
                        for o in range(len(r)):
                            if lines[i] in r[o]:
                                r[o].append(lines[i])
                        lines.remove(lines[i])
                        i=i-1
                    if inside(lines[j],r):
                        m.append(lines[j])

                if (len(m)>0) and (d==0):
                    o = 0
                    d = 1
                    if len(m)==1:
                        for o in range(len(r)):
                            if lines[j] in r[o]:
                                r[o].append(m[0])
                    else:
                        r.append(m)
            i=i+1

        if a==0:
            x=list()
            x.append(lines[j])
            r.append(x)
        lines.remove(lines[j])
        j=-1
        j=j+1


    f.close()
    return r
def sorting_anagrams(r):
    i=0
    for i in range(len(r)):
        r[i].sort(key=lambda s: s.lower())
    r.sort(key=lambda s:s[0].lower())
    r.sort(key=lambda s:len(s),reverse=True)
    return r

import itertools
def writing_into_output_file(destination,r):
    from more_itertools import flatten
    r=list(flatten(r))
    r="".join(r)
    f1=open(destination,"wb")
    f1.write(r.encode())
    f1.close()
def anagram_sort(source,destination):
    r=for_grouping(source)
    r=sorting_anagrams(r)
    writing_into_output_file(destination,r)

def main(*argv):
    if argv is None:
        argv = sys.argv

    try:

        source = argv[0]
        destination=argv[1]

        anagram_sort(source,destination)
    except Exception as e:
        print(e, file=sys.stderr)
        return 1
if __name__ == "__main__":
    sys.exit(main(input("enter input filename:"),input("enter destination filename:")))