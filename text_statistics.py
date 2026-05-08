class Text:

    def __init__(self, text):
        self.text=text
    def print_statistics(self):
        print(f"Number of words: {len(self.text.split())}")
        sentence_count = 0
        for word in self.text.split():
            if word.endswith(('.', '!', '?')):
                sentence_count += 1
        print(f"Number of sentences: {sentence_count}")
        text = self.text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
        unique_words=set(text.lower().split())
        print(f"Number of unique words: {len(unique_words)}")


    def count_word(self):
        text = self.text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
        word_count={}
       
        for word in text.split():
             
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
        for key, value in word_count.items():
            print(f"{key} appears {value} times")

    def replace_word(self, word_needed, word_replacement):
        text=self.text.replace(word_needed,word_replacement)
        print(f"({word_needed},{word_replacement}): stored text becomes {text}")

obj = Text("Hello world! Hello Python. How are you?")
obj.print_statistics()
obj.count_word()
obj.replace_word("Hello", "Hi")






        
                     
                     
        