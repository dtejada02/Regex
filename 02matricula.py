2
import re

text = input()
pattern = "(\\b(E-|E |E|)[0-9]{4}( |-|)[A-Z]{3}\\b)"
results = re.findall(pattern, text)

for match in results:
    print(match[0])