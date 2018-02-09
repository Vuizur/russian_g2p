from Grapheme2Phoneme import Grapheme2Phoneme
from Accentor import Accentor
import json
import codecs

words = open('/home/dino/sphinx/wordlist')
words = words.readlines()
words = ['я']
acc = Accentor()
g2p = Grapheme2Phoneme()
new_simple_words = {}
with open('new', 'w') as f:
    for word in words:
        word = word.strip()
        print(word)
        res, added_simple_words = acc.do_accents([word])
        new_simple_words = {**new_simple_words, **added_simple_words}
        if len(res) != 1:
            print('word has many vars', res)
            word2transcribe = word
        else:
            print('word has one var', res)
            word2transcribe = res[0][0]
        print(word2transcribe)
        transcriptions = g2p.word_to_phonemes(word2transcribe)
        print('{} {}\n'.format(word, ' '.join(transcriptions)))
        f.writelines('{} {}\n'.format(word, ' '.join(transcriptions)))

#with codecs.open('new_simple_words.json', mode='w', encoding='utf-8', errors='ignore') as fp:
#	data = json.dump(new_simple_words, fp)

