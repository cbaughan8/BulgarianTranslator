




def main ():
    bg_en = {}
    f = open("bg-en.txt", encoding='utf-8', mode="r")
    arr = f.read().split('\n')
    bg_en_arr = [a.split('\t') for a in arr]
    print(bg_en_arr)

    for pair in bg_en_arr:
        if len(pair) == 2:
            bg_en[pair[0]] = pair[1]

    print(bg_en)

    




if __name__ == '__main__':
    main()


