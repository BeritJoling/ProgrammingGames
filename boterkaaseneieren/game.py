import tkinter as tk
from typing import NamedTuple
from tkinter import font
from itertools import cycle


#tool (tuple) die klassen bouwt die aan bepaalde eisen moeten voldoen.
class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

#variabelen
BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)


class BoterKaasEnEieren:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    #gebruikt een lijstbegrip om een eerste lijst met waarden mee tegeven aan ._current_moves. Het begrip creëert een lijst met lijsten.
    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        """De laatste regel van deze methode roept aan ._get_winning_combos()en 
        wijst de retourwaarde toe aan ._winning_combos. U implementeert deze nieuwe methode in 
        de volgende sectie."""
        self._winning_combos = self._get_winning_combos()


    #De logica is dat je door middel van combinaties een rij of diagonaal kunt vormen en daardoor het spel wint.
    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    #De .is_valid_move() methode neemt een Moveobject als argument mee.
    def is_valid_move(self, move):
        """Retourneert True als de zet geldig is en anders False."""
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    #Verwerk de bewegingen van spelers om een ​​winnaar te vinden
    def process_move(self, move):
        """Verwerk de huidige zet en controleer of het een overwinning is."""
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        """Retourneert True als het spel een winnaar heeft en anders False."""
        return self._has_winner

    #controleert op gelijkspel
    def is_tied(self):
        """Retourneert True als het spel gelijk is, anders False."""
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    #Wisselt spelers tussen beurten
    def toggle_player(self):
        """Retourneert een gewisselde speler."""
        self.current_player = next(self._players)

    def reset_game(self):
        """Reset de spelstatus om opnieuw te spelen."""
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []


class Speelveld(tk.Tk):
    def __init__(self, game):
        super().__init__()
        """.titleattribuut wordt gedefenieert zodat de weergegeven tekst op de 
        titelbalk van het venster verschijnt."""
        self.title("Boter Kaas en Eieren")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    #hier wordt het menu gemaakt dat linksbovenin in de balk van de applicatie verschijnt.
    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Opnieuw spelen", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Afsluiten", command=quit)
        menu_bar.add_cascade(label="Menu", menu=file_menu)

    #hier wordt het weergavepaneel en het labelwidget gebruikt om de status en het resultaat van het spel te laten zien.
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ben je de klaar voor?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    #maakt het bordvenster
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        """Omgaan met de zet van een speler."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Speler "{self._game.current_player.label}" heeft gewonnen!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s beurt"
                self._update_display(msg)

    #update de knop
    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    #wijzigt de textweergave
    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color
        
    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        """Reset het spelbord om opnieuw te spelen."""
        self._game.reset_game()
        """Wijzigt de weergavetekst naar: "Klaar voor om opnieuw te spelen?" """
        self._update_display(msg="Klaar voor om opnieuw te spelen?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")


#maakt het speelbord en voort de hoofdloop uit (bord.mainloop()).
def main():
    """Maak het bord van het spel en voert de hoofdlus uit."""
    game = BoterKaasEnEieren()
    board = Speelveld(game)
    board.mainloop()

#If __name__ constructie controleert de uitvoering van de code.
if __name__ == "__main__":
    """aanroep voor main() vindt alleen plaats als u het .pybestand uitvoert 
    als een uitvoerbaar programma."""
    main()
