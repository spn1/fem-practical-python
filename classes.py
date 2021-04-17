class Character:
    current_level = 1
    initial_level = 1

    def __init__(self, character_class, current_level):
        self.character_class = character_class
        self.current_level = current_level

    @classmethod
    def get_current_level(clazz):
        return clazz.current_level

    def get_level(self):
        return self.current_level

    def __str__(self):
        return f'This character is a {self.character_class} at level {self.current_level}'

    def __repr__(self):
        return f'Character({self.character_class}, {self.current_level})'

class Warrior(Character):
    def __init__(self, name, current_level):
        super().__init__('Warrior', current_level)
        self.name = name

    def rend(self):
        print(f'{self.name} the {self.character_class} uses Rend!')

class Priest(Character):
    def __init__(self, name, current_level):
        super().__init__('Priest', current_level)
        self.name = name

    def smite(self):
        print(f'{self.name} the {self.character_class} uses Smite!')

print(__name__)

if __name__ == '__main__':
    test_warrior = Warrior('Cucumber', 17)
    test_priest = Priest('Persimmon', 34)

    test_warrior.rend();
    test_priest.smite();