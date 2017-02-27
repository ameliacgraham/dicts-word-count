# put your code here.

word_count_dict = {}

def get_words():
    new_file = open("test.txt")
    for line in new_file:
        new_line = line.rstrip()
        words = new_line.split(" ")
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
    # for key in word_count_dict:
    #     print "{} {}".format(key, word_count_dict[key])

    for word, count in word_count_dict.items():
        print "{} {}".format(word,count)



get_words()