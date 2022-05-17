books = {
    "margaret Atwood": ["the handmaiden's tale", "the blind assassin"], 
    "j.r.r. tolkien" : ["the hobbit", "the lord of the rings", "the silmarillion"], 
    "roald dahl": ["charlie and the chocolate factory", "matilda", "james and the giant preach"]
    }

while True:
    author_name = input("Enter author name (ctrl+c to quit): ").lower()
    mode = input("[A]dd or [S]earch? ").upper()
    if mode == 'S':
        book_results = books.get(author_name, ["None"])
        print (f"Books by {author_name}: ", ', '.join(sorted(book_results)))
    elif mode == 'A':
        title = input("Enter title to add: ").lower()
        if author_name in books:
            books [author_name].append(title)
        else:
            books[author_name] = [title]
    else:
        print ("invalid mode")
