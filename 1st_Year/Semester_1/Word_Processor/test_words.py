import word_processor
import unittest

class test_word_processor(unittest.TestCase):


    def test_convert_to_word_list(self):

        self.assertEqual(word_processor.convert_to_word_list("TEST"), ["test"])
        self.assertEqual(word_processor.convert_to_word_list("This Is A Test"), ["this", "is", "a", "test"])
        self.assertEqual(word_processor.convert_to_word_list("This Is,a.Test..."), ["this", "is", "a", "test"])
        self.assertEqual(word_processor.convert_to_word_list(",.; This ,  .; IS    ,.; A ,.; TEST"), ["this", "is", "a", "test"])


    def test_words_longer_than(self):

        self.assertEqual(word_processor.words_longer_than(5, "This is a test"), [])
        self.assertEqual(word_processor.words_longer_than(4, "This is a test"), [])
        self.assertEqual(word_processor.words_longer_than(3, "This is a test"), ["this", "test"])
        self.assertEqual(word_processor.words_longer_than(1, "This is a test"), ["this", "is", "test"])
    

    def test_words_lengths_map(self):

        self.assertEqual(word_processor.words_lengths_map("This is a test"), {4: 2, 2: 1, 1: 1})
        self.assertEqual(word_processor.words_lengths_map("This is also a test"), {4: 3, 2: 1, 1: 1})
        self.assertEqual(word_processor.words_lengths_map("This is a also test with memes"), {4: 4, 2: 1, 1: 1, 5: 1})
        self.assertEqual(word_processor.words_lengths_map("My name jeff"), {2: 1, 4: 2})
    

    def test_letters_count_map(self):

        self.assertEqual(word_processor.letters_count_map("This is a test"), {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 2, 'j': 0, 'k': 0, 'l': 0,
         'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 3, 't': 3, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})

        self.assertEqual(word_processor.letters_count_map("This is also a test"), {'a': 2, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 2, 'j': 0, 'k': 0, 'l': 1,
         'm': 0, 'n': 0, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 4, 't': 3, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})

        self.assertEqual(word_processor.letters_count_map("my name jeff"), {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 2, 'f': 2, 'g': 0, 'h': 0, 'i': 0, 'j': 1, 'k': 0, 'l': 0,
         'm': 2, 'n': 1, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 1, 'z': 0})

    def test_most_used_character(self):

        self.assertEqual(word_processor.most_used_character("this is a test"), 's')
        self.assertEqual(word_processor.most_used_character("this is also a test"), 's')
        self.assertEqual(word_processor.most_used_character("aaaaaaaaaaaaaaaaaaaaaaaab"), 'a')
        self.assertEqual(word_processor.most_used_character("aaaabbbb"), 'a')
        self.assertEqual(word_processor.most_used_character(""), None)
        self.assertEqual(word_processor.most_used_character("1234"), None)
        self.assertEqual(word_processor.most_used_character("123a456"), None)
        self.assertEqual(word_processor.most_used_character("abc123a456"), None)
        

if __name__ == '__main__':
    unittest.main()