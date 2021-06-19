<<<<<<< HEAD
import requests

page = requests.get('https://www.gutenberg.org/files/5200/5200-0.txt')
story = page.text

wordlist = story.lower().split()
for word in set(wordlist):
=======
import requests

page = requests.get('https://www.gutenberg.org/files/5200/5200-0.txt')
story = page.text

wordlist = story.lower().split()
for word in set(wordlist):
>>>>>>> fb34d168543fe7992330da7855fff8f06c7a3637
    print(f'{word} occurs {wordlist.count(word)}')