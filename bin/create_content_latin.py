import lorem
text = lorem.text()
formatted_text = ''
line_length = 0
for word in text.split():
    if line_length + len(word) + 1 > 120:
        formatted_text += '\n'
        line_length = 0
    formatted_text += word + ' '
    line_length += len(word) + 1
formatted_text = formatted_text[:50000]

with open('lorem.txt', 'w') as f:
    f.write(formatted_text)
