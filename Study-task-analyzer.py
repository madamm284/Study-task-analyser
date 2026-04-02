def count_subject_frequency(text):

    if not text.strip():
        return {}

    import string

    for p in string.punctuation:
        text = text.replace(p, "")
    

    text = text.lower()
    words = text.split()
    frequency = {}

    

    def process_word(words, index):

        if index == len(words):
            return

        word = words[index]
        stop_words = ["the", "is", "a", "to", "and" ,"also"]

        if word in stop_words:
           process_word(words, index + 1)
           return


        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

        process_word(words, index + 1)

    process_word(words, 0)

    return frequency
  
text="This is a drill!! To study today: Python, React , German, Python and JS , also German and Polish!!"
frequency_dict=count_subject_frequency(text)

for word, count in frequency_dict.items():
    print(f"{word}: {count}")

user_text = input("Enter your study list: ")

frequency_dict = count_subject_frequency(user_text)

for word, count in sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")