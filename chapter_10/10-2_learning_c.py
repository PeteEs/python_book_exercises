from pdb import line_prefix


file_path = 'chapter_10/text1.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

text_string  = ''
for line in lines:
    text_string += line

print(text_string)

text_string = text_string.replace('python','C')

print(text_string)