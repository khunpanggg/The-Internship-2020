"""Sorting Aconyms"""
def main():
    """ main function """
    box = ""
    lst = []
    lst_word = []
    num = int(input())
    for _ in range(num):
        name = input().split()
        lst.append(name)
    # print(lst)
    for i in lst:
        for j in i: # loop word
            j = j[0]
            if j.isupper():
                box += j
        lst_word.append(box)
        box = ""
    for i in sorted(lst_word, key=len, reverse=True):
        print(i)
main()