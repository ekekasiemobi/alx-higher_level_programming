#!/usr/bin/python3
if __name__ =='__main__':
    import sys
    words = sys.argv[1:]
    words_count = len(words)

    if words_count == 0:
        print(f"{words_count} arguments.")
    elif words_count == 1:
         print(f"{words_count} argument.")
    else:
         print(f"{words_count} arguments.")

    for i in range (words_count):
        index = i + 1
        word = words[i]
        print(index, ":", word)
