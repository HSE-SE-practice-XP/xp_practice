import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class TicTacToeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')
        self.setGeometry(100, 100, 300, 300)

        self.current_player = 'X'  # Игрок X начинает игру
        self.board = [''] * 9

        self.buttons = []
        for i in range(9):
            button = QPushButton('', self)
            button.setGeometry((i % 3) * 100, (i // 3) * 100, 100, 100)
            button.clicked.connect(lambda state, button=button, index=i: self.on_button_click(button, index))
            self.buttons.append(button)

        self.status_label = QLabel('Ход игрока X', self)
        self.status_label.setGeometry(10, 250, 280, 40)

    def on_button_click(self, button, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            button.setText(self.current_player)

            if self.check_winner():
                self.status_label.setText(f'Победил игрок {self.current_player}!')
                for btn in self.buttons:
                    btn.setEnabled(False)
            elif '' not in self.board:
                self.status_label.setText('Ничья!')
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText(f'Ход игрока {self.current_player}')

    def check_winner(self):
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != '':
                return True
        return False

def main():
    app = QApplication(sys.argv)
    window = TicTacToeApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()