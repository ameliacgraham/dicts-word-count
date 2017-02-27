# put your code here.

word_count_dict = {}

def get_words(file_name):
    new_file = open(file_name)
    for line in new_file:
        new_line = line.rstrip()
        words = new_line.split(" ")
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
    # for key in word_count_dict:
    #     print "{} {}".format(key, word_count_dict[key])

    for word, count in word_count_dict.iteritems():
        print "{} {}".format(word, count)



get_words("twain.txt")