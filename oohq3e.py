from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
import random as rnd


class Card:
    def __init__(self, type):
        self.type = type
        switch = {
            1: "images/bell.png",
            2: "images/bullet.png",
            3: "images/controller.png",
            4: "images/house.png",
            5: "images/light_snowflake.png",
            6: "images/light_star.png",
            7: "images/pen.png",
            8: "images/pink_snowflake.png",
            9: "images/present.png",
            10: "images/snowman.png",
            11: "images/tree.png",
            12: "images/yellow_snowflake.png"
        }
        try:
            self.link = switch[type]

        except KeyError:
            print(type, "is an invalid type, there is no such memory card, please try again!")

    def __str__(self):
        types = {
            1: "bell.png",
            2: "bullet",
            3: "controller.png",
            4: "house.png",
            5: "light_snowflake.png",
            6: "light_star.png",
            7: "pen.png",
            8: "pink_snowflake.png",
            9: "present.png",
            10: "snowman.png",
            11: "tree.png",
            12: "yellow_snowflake.png"
        }
        return types[self.type]

    def __eq__(self, other):
        if self.type == other.type:
            return True
        return False


class MemoryGame(App):
    def card_shuffle(self):
        rnd.shuffle(self.card_list)

    def score_update(self):
        print(f"Current status: Player has flipped: {self.player_turn}, successful flips {self.score}")

    def unflip_cards(self, id):
        index = id - 1
        self.display_list[index].clear_widgets()
        self.add_button(str(id))

    def flip_cards(self, id):
        index = id - 1
        if index in self.winnerindexes:
            return 0

        self.turn_counter += 1

        if self.turn_counter == 3:
            self.turn_counter = 0
            first_card, second_card = self.flipped_cards
            self.player_turn += 1

            is_pair = False
            print(f"First card: {first_card + 1}, Second card: {second_card + 1}")
            if self.card_list[first_card] == self.card_list[second_card]:
                print("The 2 cards are the same!")
                is_pair = True
                self.score += 1
                self.score_update()
                self.winnerindexes.append(first_card)
                self.winnerindexes.append(second_card)
                if self.score + 1 == 8:
                    print("Congratulations, just flip the last two cards, and you won the game!")

            if not is_pair:
                print("The two cards are not the same! - Unflipping the cards.")
                self.unflip_cards(first_card + 1)
                self.unflip_cards(second_card + 1)
                self.flipped_cards = [0, 0]

            return 0

        self.display_list[index].clear_widgets()
        memory_photo = Image(source=self.card_list[index].link)
        self.display_list[index].add_widget(memory_photo)
        self.flipped_cards[self.turn_counter - 1] = id - 1

    def add_button(self, id):
        b = Button(
            text=id,
            size_hint=(1, 0.5),
            bold=True,
            color=(0, 0, 0),
            background_color=(0, 12, 15, 1)
        )
        self.display_list[int(id) - 1].add_widget(b)
        b.bind(on_press=lambda x: self.flip_cards(int(b.text)))
        self.button_list.append(b)

    def fill_buttons(self):
        for id in range(1, (self.amount_of_cards * 2) + 1):
            self.add_button(str(id))

    def fill_sub_layouts(self):
        for layout in self.display_list:
            self.window.add_widget(layout)

    def build(self):
        self.amount_of_cards = 8
        self.flipped_cards = [0, 0]
        self.display_list = [GridLayout(cols=1) for i in range(self.amount_of_cards * 2)]
        self.winnerindexes = []

        self.card_list = []
        self.player_turn = 0
        self.turn_counter = 0
        self.score = 0

        for i in range(self.amount_of_cards):
            self.card_list.append(Card(i + 1))
            self.card_list.append(Card(i + 1))

        self.card_shuffle()
        self.window = GridLayout()
        self.window.cols = 4
        self.button_list = []
        self.fill_sub_layouts()
        self.fill_buttons()
        print("Let the game begin!")
        self.score_update()
        return self.window


if __name__ == "__main__":
    MemoryGame().run()
