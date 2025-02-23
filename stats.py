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

def sort_by(dict):
    return dict["num"]

def sortdis(dictionary):
    sorted_list = []
    for i in dictionary:
        sorted_list.append({"char":i, "num": dictionary[i]})
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list