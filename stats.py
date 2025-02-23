def word_count(string):
        words = string.split()
        return len(words)
def letter_count(string):
    string = str.lower(string)
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count