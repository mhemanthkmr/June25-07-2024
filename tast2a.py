# Initial list of favorite Marvel superheroes
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. Length of the list
length_of_list = len(heros)
print(f"Length of the list: {length_of_list}")

# 2. Add 'black panther' at the end of the list
heros.append('black panther')
print(f"List after adding 'black panther' at the end: {heros}")

# 3. Add 'black panther' after 'hulk'
heros.remove('black panther')
heros.insert(heros.index('hulk') + 1, 'black panther')
print(f"List after adding 'black panther' after 'hulk': {heros}")

# 4. Replace 'thor' and 'hulk' with 'doctor strange' in one line
heros[1:3] = ['doctor strange']
print(f"List after replacing 'thor' and 'hulk' with 'doctor strange': {heros}")
