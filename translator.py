from translate import Translator
import sys

lines = len(sys.argv)

if lines <= 2:
    print("Please enter the command in this format -> python3 translator.py 'Your content for translation' 'language code' ")
else:
    content = sys.argv
    translator = Translator(to_lang=content[-1])
    for i in range(1, lines-1):
        translation = translator.translate(content[i])
        print(translation)

print("Job Done!")
