import tkinter as tk
import random


class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttons = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.winner_label = tk.Label(self.window, text='', font=('normal', 16))
        self.restart_button = tk.Button(self.window, text='Restart', font=('normal', 16), command=self.reset_game)

        self.create_buttons()
        self.place_labels_and_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=10, height=3,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def place_labels_and_buttons(self):
        self.winner_label.grid(row=3, columnspan=3)
        self.restart_button.grid(row=4, columnspan=3)

    def on_button_click(self, i, j):
        if self.buttons[i][j]['text'] == '' and self.current_player == 'X':
            self.buttons[i][j]['text'] = 'X'
            self.current_player = 'O'
            self.check_winner()
            self.computer_move()
            self.check_winner()

    def computer_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == '']
        if available_moves:
            i, j = random.choice(available_moves)
            self.buttons[i][j]['text'] = 'O'
            self.current_player = 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                self.display_winner(self.buttons[i][0]['text'])
                return
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                self.display_winner(self.buttons[0][i]['text'])
                return
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            self.display_winner(self.buttons[0][0]['text'])
            return
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            self.display_winner(self.buttons[0][2]['text'])
            return

        # Check for a tie
        if all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
            self.display_winner("Tie")

    def display_winner(self, winner):
        self.winner_label.config(text=f"{winner} wins!" if winner != "Tie" else "It's a Tie!")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['state'] = 'normal'
        self.current_player = 'X'
        self.winner_label.config(text='')

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
