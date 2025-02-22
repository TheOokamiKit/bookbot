def main ():
    def get_book_text(filepath):
        #grabs the specified file and outputs it to a string
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    #provides the filepath to the book to evaluate then prints to console
    print(get_book_text("books/frankenstein.txt"))

main()
