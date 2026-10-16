import string

user_input = input("Please input a text")
clean_text = user_input.translate(str.maketrans('', '', string.punctuation))

user_input2 = input("Please input a number")
integer = int(user_input2)

def word_count(text_to_count):
    word_list = []
    seen_words = []
    words_in_text = text_to_count.lower().split()
    
    for w in words_in_text:
        if w not in seen_words:
            count = words_in_text.count(w)
            word_dict = {"word": w, "count": count}
            word_list.append(word_dict)
            seen_words.append(w)
            
    return word_list

def top_k(text_to_count, target_count):
    data_list = word_count(text_to_count)
    result = []
    
    for my_dict in data_list:
        if my_dict["count"] == target_count:
            word_tuple = (my_dict["word"], my_dict["count"])
            result.append(word_tuple)
            
    print(result)
    
if __name__ == "__main__":
    top_k(clean_text, integer)