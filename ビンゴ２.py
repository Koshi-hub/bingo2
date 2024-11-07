import random

class BingoCard:
    def __init__(self):
        self.card = self.generate_bingo_card()
        self.selected_numbers = set()

    def generate_bingo_card(self):
        card = []
        # 各列に対応する番号の範囲
        ranges = {
            'B': range(1, 16),
            'I': range(16, 31),
            'N': range(31, 46),
            'G': range(46, 61),
            'O': range(61, 76)
        }

        # 各列に5つの数字をランダムに選ぶ
        for column, number_range in ranges.items():
            column_numbers = random.sample(number_range, 5)
            card.append(column_numbers)

        # 'N'列の中央にフリー
        card[2][2] = 'FREE'

        return card

    def display_card(self):
        print(" B   I   N   G   O")
        for row in range(5):
            for col in range(5):
                value = self.card[col][row]
                # 'FREE'の場合はそのまま表示
                if value == 'FREE':
                    print("FREE", end="  ")
                else:
                    print(f"{value:2}", end="   ")
            print()

    def check_bingo(self):
        # 行、列、対角線のビンゴ判定
        for row in range(5):
            if all(self.card[col][row] in self.selected_numbers or self.card[col][row] == 'FREE' for col in range(5)):
                return True
        for col in range(5):
            if all(self.card[col][row] in self.selected_numbers or self.card[col][row] == 'FREE' for row in range(5)):
                return True
        if all(self.card[i][i] in self.selected_numbers or self.card[i][i] == 'FREE' for i in range(5)):
            return True
        if all(self.card[i][4-i] in self.selected_numbers or self.card[i][4-i] == 'FREE' for i in range(5)):
            return True
        return False

    def select_number(self, number):
        if number not in self.selected_numbers:
            self.selected_numbers.add(number)
            print(f"Number {number} selected!")
        else:
            self.selected_numbers.remove(number)
            print(f"Number {number} deselected!")

def main():
    bingo = BingoCard()
    bingo.display_card()

    while True:
        try:
            number = input("\nSelect a number to mark (or 'exit' to quit): ").strip()
            if number.lower() == 'exit':
                print("Game over!")
                break
            if number.isdigit():
                number = int(number)
                if 1 <= number <= 75:
                    bingo.select_number(number)
                    if bingo.check_bingo():
                        print("Bingo! You've won!")
                        break
                else:
                    print("Please enter a number between 1 and 75.")
            else:
                print("Invalid input, please enter a number or 'exit'.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")

if __name__ == "__main__":
    main()
