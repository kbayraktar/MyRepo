import textwrap

with open('lorem.txt', 'r') as file:
    text = file.read()

wrapped_text = textwrap.fill(text, width=120)

with open('lorem_wrapped.txt', 'w') as file:
    file.write(wrapped_text)