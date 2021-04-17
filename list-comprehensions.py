characters = ['Persimmon', 'Parsnip', 'Peregrin']
character_length = []

for character in characters:
    character_length.append(len(character));

print(f'Before: {character_length}');

comp = [ len(name) for name in characters ];
print(f'After: {comp}')

comp_if = [ name for name in characters if len(name) >= 8 ]
print(f'After 2: {comp_if}')