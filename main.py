def main ():
    def get_book_text(filepath):
        #grabs the specified file and outputs it to a string
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    from stats import word_count
    from stats import letter_count


    #provides the filepath to the book to evaluate then prints the word count to console
    contents = get_book_text("books/frankenstein.txt")
    words = word_count(contents)
    letters = letter_count(contents)
    print(f"{words} words found in the document")
    print(letters)

main()
