def searcher():
    book=open("book.txt")
    wordlist=book.read()
    lines=book.readlines()
    book.close()

    while(True):        
        text = (yield)
        if text in wordlist:
            print("Your name is in the book")
            # for i in range(len(lines)):
            #     if text in lines[i]:
            #         z=f"In {i}th line."
            # print(z)
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("Parag")
search.send("grids")