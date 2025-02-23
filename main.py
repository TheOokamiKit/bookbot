def main ():
    import sys
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    def get_book_text(filepath):
        #grabs the specified file and outputs it to a string
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    #imports functions from supplimental file
    #word_count takes a string and seperates it at spaces then returns a number of segments
    #letter_count returns the number of characters in the string
    #sortdis is supposed to sort the dictonary reported by letter_count by most frequently found to least frequently found
    from stats import(
        word_count,
        letter_count,
        sortdis
    )


    #provides the filepath to the book to evaluate then prints the word count to console
    book_source = sys.argv[1]
    contents = get_book_text(book_source)
    words = word_count(contents)
    letters = letter_count(contents)
    sorted_letters = sortdis(letters)

    #formating for readablity
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_source}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if not letter["char"].isalpha():
            continue
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")
    

main()
