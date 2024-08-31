class WordsFinder:

    def __init__(self, *file_names):                             #создаем объект с неограниченным кол-м текстовых файлов
        self.file_names = file_names

    def get_all_words(self):                         #метод вывода текстового файла в консоль по словам в список словаря
        all_words = {}
        for file_ in self.file_names:
            with open(file_, 'r', encoding='utf-8') as f:
                strings_ = f.read()
                f.seek(0)
                symbols_to_remove = "',', '.', '=', '!', '?', ';', ':', ' - '"
                for symbol in symbols_to_remove:                               #стираем символы в нашем тексте
                    strings_ = strings_.replace(symbol, ' ')
                all_words.update({file_: strings_.lower().split()})
        return all_words

    def find(self, word):                                                #метод поиска первого совпадения искомого слова
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() in words[i]:
                    break
        return {name: i}

    def count(self, word):                                                      #метод поиска кол-ва совпадений по слову
        for name, words in self.get_all_words().items():
            cnt = 0
            for i in range(len(words)):
                if word.lower() in words[i]:
                    cnt += 1
        return {name: cnt}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего