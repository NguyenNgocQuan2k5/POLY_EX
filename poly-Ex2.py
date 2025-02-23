import os
os.system('cls')

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return self.name + ' ' + self.surname

    def __add__(self,other):
        return f'{self.name} {other.name}'
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
        
class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people  

    def __str__(self):
        return f'Group {self.name} with members {", ".join([str(person) for person in self.people])}'

    def __repr__(self):
        return f"Group(name='{self.name}', people={self.people})"

    def __add__(self,other):
        return Group(self.name + other.name, self.people + other.people)
  
if __name__ == "__main__":
    p0 = Person('Aliko', 'Dangote')
    p1 = Person('Bill', 'Gates')
    p2 = Person('Warren', 'Buffet')
    p3 = Person('Elon', 'Musk')
    p4 = p2 + p3
    first_group = Group('__VIP__', [p0, p1, p2])
    second_group = Group('Special', [p3, p4])
    third_group = first_group + second_group
    print(len(first_group.people))
    print(second_group)
    print(third_group.people[0])
    for person in third_group.people:
        print(person)