"""
Создайте программу, хранящую информацию о великих баскетболистах.
Нужно хранить имя, фамилию, год рождения и рост (в сантиметрах) баскетболиста.
Требуется реализовать возможность добавления, удаления, поиска.
Используйте словарь для хранения данных баскетболиста.
"""

import string
import datetime

LIST_OF_PLAYERS = []
KEYS = ["name", "last name", "birth year", "height"]
TEAM_ONE = []
TEAM_TWO = []


class NameTooLong(Exception):
    pass


class LastNameTooLong(Exception):
    pass


class IllegalHeight(Exception):
    pass


class IllegalName(Exception):
    pass


class IllegalLastName(Exception):
    pass


class BasketballPlayer:
    def __init__(self, name, last_name, birth_year, height):
        self.name = name
        self.last_name = last_name
        self._birth_year = birth_year
        self.height = height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if len(val) > 50:
            raise NameTooLong("The name is toooo long! ")
        illegal_chars = string.digits + string.punctuation + string.whitespace
        for char in val:
            if char in illegal_chars:
                raise IllegalName(val + ":" + char)
        self._name = val

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, val):
        if len(val) > 50:
            raise LastNameTooLong("The last name is toooo long! ")
        illegal_chars = string.digits + string.punctuation + string.whitespace
        for char in val:
            if char in illegal_chars:
                raise IllegalLastName(val + ":" + char)
        self._last_name = val

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def age(self):
        date_now = datetime.datetime.now().year
        age = date_now - self.birth_year
        return age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        legal_chars = string.digits
        for char in val:
            if char not in legal_chars:
                raise IllegalHeight(val)
        self._height = val

    # b. написать функцию которая считывает из файла всех баскетболистов,
    @staticmethod
    def read_from_csv():
        with open(file="famous_basketball_players.csv", mode="r") as file:
            for line in file:
                list_of_players = line.split(",")
                list_of_players = [line.rstrip() for line in list_of_players]
                players_with_keys = dict(zip(KEYS, list_of_players))
                LIST_OF_PLAYERS.append(players_with_keys)

    # c. Написать функцию которая “красиво“ выводит на экран данные одного баскетболиста
    @classmethod
    def print_one_player(cls, obj):
        print(f"Name: {obj['name']}" + "\n" +
              f"Last name: {obj['last name']}" + "\n" +
              f"Birth year: {obj['birth year']}" + "\n" +
              f"Height (cm): {obj['height']}" + "\n")

    # d. Написать функцию которая “красиво“ выводит на экран данные всех баскетболистов
    @classmethod
    def print_all_players(cls):
        print("Here is the list of all basketball players" + "\n")
        for player in LIST_OF_PLAYERS:
            BasketballPlayer.print_one_player(player)

    # e. написать функцию которая принимает от пользователя данные нового баскетболиста и добавляет их в список
    @classmethod
    def add_bas_player(cls):
        temp = []
        print(f"Lets add a new basketball player to the list.")
        for i in range(len(KEYS)):
            values = str(input(f"Please enter his\her {KEYS[i]}: "))
            temp.append(values)
        LIST_OF_PLAYERS.append(dict(zip(KEYS, temp)))

    # f. написать функцию которая сохраняет всех баскетболистов в файл
    @classmethod
    def save(cls):
        with open('filename.json', 'w') as myfile:
            for line in LIST_OF_PLAYERS:
                myfile.write(str(line) + "\n")

    # g. написать функцию поиска баскетболиста по имени или фамилии
    @classmethod
    def search_player(cls):
        name_last_name = str(input(f"Please enter {KEYS[0]} or {KEYS[1]} of the basketball player to search "))
        for value in LIST_OF_PLAYERS:
            if name_last_name in value.values():
                print(value)
                break
        else:
            print("Basketball player not found")

    # h. написать функцию которая напечатает данные 3 самых высоких баскетболистов
    @classmethod
    def print_three_tallest_players(cls):
        sorted_list_of_players = sorted(LIST_OF_PLAYERS, key=lambda value: value["height"], reverse=True)
        print(f"There are 3 tallest players from the list: " + '\n' + f"{sorted_list_of_players[0:3]}")

    # i. написать функцию которая удаляет баскетболиста из списка по имени и фамилии
    @classmethod
    def del_bas_player(cls):
        remove_player_name = str(input("Please enter the name of the player to delete: "))
        remove_player_last_name = str(input("Please enter the last name of the player to delete: "))
        for item in LIST_OF_PLAYERS:
            if remove_player_name == item["name"] and remove_player_last_name == item["last name"]:
                LIST_OF_PLAYERS.remove(item)
                cls.print_all_players()

    # j. написать функцию main которая будет предлагать пользователю описанные выше возможности и выполнять их.
    # Программа будет работать до тех пор пока пользователь не ввел -1 для выхода.
    # В завершении программы программа будет сохранять список баскетболистов в файл.
    @classmethod
    def main(cls):
        BasketballPlayer.read_from_csv()
        input_number = None

        print("There are the possibilities of the program:"
              "\n1. To print info about a single player."
              "\n2. To print info of all players."
              "\n3. To add a new player to the list"
              "\n4. To save the list of players to a new file."
              "\n5. To find a player in the list."
              "\n6. To print info about three tallest players."
              "\n7. To delete a player."
              "\n-1. To Save & Quit."
              "\n")

        while input_number != -1:
            input_number = int(input("Please enter the number "))

            if input_number == 1:
                BasketballPlayer.print_one_player(obj=LIST_OF_PLAYERS[0])
            elif input_number == 2:
                BasketballPlayer.print_all_players()
            elif input_number == 3:
                BasketballPlayer.add_bas_player()
            elif input_number == 4:
                BasketballPlayer.save()
            elif input_number == 5:
                BasketballPlayer.search_player()
            elif input_number == 6:
                BasketballPlayer.print_three_tallest_players()
            elif input_number == 7:
                BasketballPlayer.del_bas_player()
        else:
            BasketballPlayer.save()
            print("Thanks for your time!")


class BasketballTeam(BasketballPlayer):
    def __init__(self, name, last_name, birth_year, height):
        super().__init__(name, last_name, birth_year, height)

    @classmethod
    def add_bas_players(cls):
        temp_one = []
        temp_two = []
        input_number = None

        print(f"To play basketball you need to recruit players."
              "\nEach team must contain 5 players."
              "\nPlease chose the team where to add a basketball player:"
              "\n1. Team one"
              "\n2. Team two"
              "\n-1. Let's go to play!")

        while input_number != -1:
            input_number = int(input("Please enter the number: "))
            if input_number == 1:
                for i in range(len(KEYS)):
                    values = str(input(f"Please enter his\her {KEYS[i]}: "))
                    temp_one.append(values)
                TEAM_ONE.append(dict(zip(KEYS, temp_one)))
            elif input_number == 2:
                for i in range(len(KEYS)):
                    values = str(input(f"Please enter his\her {KEYS[i]}: "))
                    temp_two.append(values)
                TEAM_TWO.append(dict(zip(KEYS, temp_two)))

            if len(TEAM_ONE) and len(TEAM_TWO) < 5:
                print("Not all players in teams!"
                      f"\nTeam one has {len(TEAM_ONE)} player(s)."
                      f"\nTeam two has {len(TEAM_TWO)} player(s).")
            if len(TEAM_ONE) and len(TEAM_TWO) == 5:
                print("Teams recruited!")
        else:
            print("You are ready to play the game!")

    @classmethod
    def print_team_one(cls):
        print("\nHere is the list of Team one" + "\n")
        for player in TEAM_ONE:
            BasketballPlayer.print_one_player(player)

    @classmethod
    def print_team_two(cls):
        print("Here is the list of Team two" + "\n")
        for player in TEAM_TWO:
            BasketballPlayer.print_one_player(player)


if __name__ == '__main__':
    BasketballPlayer.main()

    BasketballTeam.add_bas_players()
    BasketballTeam.print_team_one()
    BasketballTeam.print_team_two()
