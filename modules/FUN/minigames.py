from ..Module import *
import random

games = {}

class GameBoard:
    def __init__(self, rows=3, cols=3, win_length=3):
        self.rows = rows
        self.cols = cols
        self.win_length = win_length
        self.board = [[" " for _ in range(cols)] for _ in range(rows)]
        self.current_player = "X"
        self.winner = None

    def display_board(self):
        return "\n" + "\n".join([" | ".join(row) for row in self.board])

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def bot_move(self):
        available_moves = [(r, c) for r in range(self.rows) for c in range(self.cols) if self.board[r][c] == " "]
        if available_moves:
            row, col = random.choice(available_moves)
            self.make_move(row, col)

    def check_winner(self, last_row, last_col):
        return (self.check_direction(last_row, last_col, 1, 0) or  # Horizontal
                self.check_direction(last_row, last_col, 0, 1) or  # Vertical
                self.check_direction(last_row, last_col, 1, 1) or  # Diagonal \
                self.check_direction(last_row, last_col, 1, -1))   # Diagonal /

    def check_direction(self, row, col, row_dir, col_dir):
        count = 1
        for d in [1, -1]:  # Check both forward and backward directions
            r, c = row + d * row_dir, col + d * col_dir
            while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == self.current_player:
                count += 1
                r += d * row_dir
                c += d * col_dir
        return count >= self.win_length

    def is_draw(self):
        return all(self.board[row][col] != " " for row in range(self.rows) for col in range(self.cols))


async def tictactoe_callback(CommandObject, message, self, params, command_data):
    user_id = str(message.author.id)
    if len(params) < 2:
        if user_id not in games:
            games[user_id] = GameBoard()
            await message.channel.send(f"Tic Tac Toe started! {message.author.mention} my bro is X.\n{games[user_id].display_board()}")
        else:
            await message.channel.send("You already have a game in progress.")
    else:
        if user_id in games:
            try:
                _, row, col = message.content.split()
                row, col = int(row) - 1, int(col) - 1
                if games[user_id].make_move(row, col):
                    if games[user_id].winner:
                        await message.channel.send(f"<@{games[user_id]}> wins!\n{games[user_id].display_board()}")
                        del games[user_id]
                    elif games[user_id].is_draw():
                        await message.channel.send(f"It's a draw <@{games[user_id]}>!\n{games[user_id].display_board()}")
                        del games[user_id]
                    else:
                        await message.channel.send(f"Moved \n{games[user_id].display_board()}")
                        games[user_id].bot_move()
                        if games[user_id].winner:
                            await message.channel.send(f"Bot (O) wins!\n{games[user_id].display_board()}")
                            del games[user_id]
                        elif games[user_id].is_draw():
                            await message.channel.send(f"It's a draw!\n{games[user_id].display_board()}")
                            del games[user_id]
                        else:
                            await message.channel.send(f"Bot made a move.\n{games[user_id].display_board()}")
                else:
                    await message.channel.send("Invalid move! Try again.")
            except ValueError:
                await message.channel.send("pls provide row and column as numerals ong")
        else:
            await message.channel.send("You don't have an active Tic Tac Toe game.")

tictactoe_command = Command("tictactoe", 'Play tic tac toe in Discord', tictactoe_callback, FUN, aliases=['ttt', 't3'])


c4games = {}
async def c4_callback(CommandObject, message, self, params, command_data):
    user_id = str(message.author.id)
    if len(params) < 2:
        if user_id not in c4games:
            c4games[user_id] = GameBoard(rows=10,cols=10,win_length=4)
            await message.channel.send(f"c4 started! {message.author.mention} my bro is X.\n{c4games[user_id].display_board()}")
        else:
            await message.channel.send("You already have a game in progress.")
    else:
        if user_id in c4games:
            try:
                _, row, col = message.content.split()
                row, col = int(row) - 1, int(col) - 1
                if c4games[user_id].make_move(row, col):
                    if c4games[user_id].winner:
                        await message.channel.send(f"{c4games[user_id].winner} wins!\n{c4games[user_id].display_board()}")
                        del c4games[user_id]
                    elif c4games[user_id].is_draw():
                        await message.channel.send(f"It's a draw!\n{c4games[user_id].display_board()}")
                        del c4games[user_id]
                    else:
                        await message.channel.send(f"Moved \n{c4games[user_id].display_board()}")
                        c4games[user_id].bot_move()
                        if c4games[user_id].winner:
                            await message.channel.send(f"Bot (O) wins!\n{c4games[user_id].display_board()}")
                            del c4games[user_id]
                        elif c4games[user_id].is_draw():
                            await message.channel.send(f"It's a draw!\n{c4games[user_id].display_board()}")
                            del c4games[user_id]
                        else:
                            await message.channel.send(f"Bot made a move.\n{c4games[user_id].display_board()}")
                else:
                    await message.channel.send("Invalid move! Try again.")
            except ValueError:
                await message.channel.send("pls provide row and column as numerals ong")
        else:
            await message.channel.send("You don't have an active c4 game. Start one with `.c4`")

c4_command = Command("connect4", 'Play Connect4 in Discord', c4_callback, FUN, aliases=['c4', 'con4'])
