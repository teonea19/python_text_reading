# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    my_file = open("./story.txt", "r")
    read_file_content = my_file.read()
    print(read_file_content)
    print("*******************")

    new_data = read_file_content.split()
    print(new_data)

    print("*******************")

    count = {}
    for i in new_data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(read_file_content("./story.txt"))

