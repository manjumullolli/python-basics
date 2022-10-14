def searcher():
    import time
    #some 4 sec time consuming task
    book="This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print('your text is in the book')
        else:
            print('text is not in the book')

search=searcher()
print('search started')
next(search)
print('next metod run')
search.send('harry')
search.close()
# search.send('harry')
# input('press any key')
# search.send('harry and')
# input('press any key')
# search.send('thi d')
# input('press any key')
# search.send('joker')
# input('press any key')
# search.send('like video')