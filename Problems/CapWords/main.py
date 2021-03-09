phrase = input()

phrase = phrase.replace('_', ' ')
class_name = phrase.title().replace(' ', '')
print(class_name)
