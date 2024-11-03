import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = list(file_name)

    def get_all_words(self, *file_names):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utF-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                words = list(text.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        one_word = {}
        for name, words in self.get_all_words().items():
            one_word[name] = words.index(word)
        return one_word

    def count(self, word):
        word = word.lower()
        count_words = {}
        for name, words in self.get_all_words().items():
            count_words[name] = words.count(word)
        return count_words


finder = WordsFinder('test.txt')
finder1 = WordsFinder('test_file.txt')
finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder.get_all_words())  # Все слова
print(finder1.get_all_words())  # Все слова
print(finder2.get_all_words())
print(finder.find('tEXt'))  # Все слова
print(finder1.find('Найти'))  # Все слова
print(finder2.find('FACE'))  #
print(finder2.count('Child'))
print(finder.count('UTf8'))
print(finder1.count('для'))
