from enum import Enum
from abc import ABC, abstractmethod

class Vector2D():
    def __init__(self):
        self.x = 0
        self.y = 0

    def __add__(self, vec):
        pass

    def __sub__(self, vec):
        pass



class EnumSeason(Enum):
    none = 0
    winter = 1
    summer = 2

class EnumTribe(Enum):
    none = 0
    player = 1
    opponent = 2




class Item():
    def __init__(self):
        self.is_consumable = False
        self.coins_collect = 0


class Fruit(Item):
    def __init__(self):
        super().__init__()
        self.is_consumable = True
    
    def collect(self):
        pass


class Forest(Item):
    def __init__(self):
        super().__init__()


class Building(Item):
    def __init__(self):
        super().__init__()
        self.level = 0

class Sawmill(Building):
    def __init__(self):
        super().__init__()

class Village(Building):
    def __init__(self):
        super().__init__()

    def capture(self):
        pass



class Actor(ABC):
    def __init__(self):
        self.tribe = EnumTribe.none
        self.coins_cost = 0
        self.move_steps = 0
        self.power_attack = 0
        self.power_defense = 0
        self.experience = 0
        self.level = 0

    @abstractmethod
    def move(self, pos: Vector2D):
        pass


class Warrior(Actor):
    def __init__(self):
        super().__init__()

    def move(self, pos: Vector2D):
        pass

class Horseman(Actor):
    def __init__(self):
        super().__init__()

    def move(self, pos: Vector2D):
        pass

class Knight(Horseman):
    def __init__(self):
        super().__init__()

    def move(self, pos: Vector2D):
        pass



class MapTile():
    def __init__(self):
        self.position = Vector2D()
        self.season = EnumSeason.none
        self.tribe = EnumTribe.none
        self.items_on_tile = list[Item]
        self.actor_on_tile = list[Actor]
        self.is_visible_for_tribe = list[EnumTribe]



class Game():
    def __init__(self):
        self.map_size = Vector2D()
        self.turn = 0
        self.__map_tiles = list[MapTile]
    
    def get_map_tiles(self):
        return self.__map_tiles

    def new_game(self):
        pass

    def update_step(self, tribe: EnumTribe, actor: Actor):
        pass

game = Game()
print(game.turn)
apple = Fruit()
print(apple.is_consumable)
player = Knight()
player.tribe = EnumTribe.opponent
print(player.tribe.value)