from ..Module import * 
from ..Utils import *
import random as ran
import random 
import requests
from discord.ui import Button, View






class TriviaView(View):
    def __init__(self, correct_answer, user):
        super().__init__(timeout=15)
        self.correct_answer = correct_answer
        self.user = user
        self.result = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user == self.user

    @discord.ui.button(label="Option 1", style=discord.ButtonStyle.primary)
    async def option1(self, interaction: discord.Interaction, button: Button):
        self.result = button.label
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="Option 2", style=discord.ButtonStyle.primary)
    async def option2(self, interaction: discord.Interaction, button: Button):
        self.result = button.label
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="Option 3", style=discord.ButtonStyle.primary)
    async def option3(self, interaction: discord.Interaction, button: Button):
        self.result = button.label
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label="Option 4", style=discord.ButtonStyle.primary)
    async def option4(self, interaction: discord.Interaction, button: Button):
        self.result = button.label
        await interaction.response.defer()
        self.stop()


games = {}
c4games = {}

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
            row, col = ran.choice(available_moves)
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







class GameGroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    group = app_commands.Group(name="game", description="Play games")

    @group.command(name="tictactoe", description="Play a game of tictactoe")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def tictactoe_callback(self, ctx: discord.Interaction, row:int, col:int):
        user_id = str(ctx.user.id)
        if user_id in c4games:
                try:
                    row, col = row - 1, col - 1
                    if c4games[user_id].make_move(row, col):
                        if c4games[user_id].winner:
                            await ctx.response.send_message(f"{c4games[user_id].winner} wins 100 Coins!\n{c4games[user_id].display_board()}")
                            db.add_coins(ctx.user.id,100)
                            del c4games[user_id]
                        elif c4games[user_id].is_draw():
                            await ctx.response.send_message(f"It's a draw!\n{c4games[user_id].display_board()}")
                            del c4games[user_id]
                        else:
                            await ctx.response.send_message(f"Moved \n{c4games[user_id].display_board()}")
                            c4games[user_id].bot_move()
                            if c4games[user_id].winner:
                                await ctx.response.send_message(f"Bot (O) wins!\n{c4games[user_id].display_board()}")
                                del c4games[user_id]
                            elif c4games[user_id].is_draw():
                                await ctx.followup.send(f"It's a draw!\n{c4games[user_id].display_board()}")
                                del c4games[user_id]
                            else:
                                await ctx.followup.send(f"Bot made a move.\n{c4games[user_id].display_board()}")
                    else:
                        await ctx.response.send_message("Invalid move! Try again.")
                except ValueError:
                    await ctx.response.send_message("pls provide row and column as numerals ong")
        else:
            c4games[user_id] = GameBoard(rows=3,cols=3,win_length=3)
            await ctx.response.send_message(f"tictactoe started! {ctx.user.mention} my bro is X.\n{c4games[user_id].display_board()}")

     @app_commands.command(name="eightball", description="Ask the 8-ball a question.")
     @app_commands.check(commandCheck)
     @app_commands.user_install()
     async def eightball_callback(self, ctx: discord.Interaction, question: str):
        """ Consult 8ball to receive an answer """
        ballresponse = [
            "Yes", "No", "Take a wild guess...", "Very doubtful",
            "Sure", "Without a doubt", "Most likely", "Might be possible",
            "You'll be the judge", "no... (╯°□°）╯︵ ┻━┻", "no... baka",
            "senpai, pls no ;-;", "It is certain.", "Ask again later.",
            "Better not tell you now.", "Don't count on it.", "My sources say no.",
            "Outlook not so good."
        ]

        answer = random.choice(ballresponse)
        await ctx.response.send_message(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @group.command(name="connect4", description="Play a game of connect4")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def c4_callback(self,ctx: discord.Interaction, row:int, col:int):
        global c4games
        user_id = str(ctx.user.id)
        if user_id in c4games:
                print("eee")
                try:
                    print("eee")
                    row, col = row - 1, col - 1
                    if c4games[user_id].make_move(row, col):
                        if c4games[user_id].winner:
                            await ctx.response.send_message(f"{c4games[user_id].winner} win 100 coins!\n{c4games[user_id].display_board()}")
                            db.add_coins(ctx.user.id,100)
                            del c4games[user_id]
                        elif c4games[user_id].is_draw():
                            await ctx.response.send_message(f"It's a draw!\n{c4games[user_id].display_board()}")
                            del c4games[user_id]
                        else:
                            await ctx.response.send_message(f"Moved \n{c4games[user_id].display_board()}")
                            c4games[user_id].bot_move()
                            if c4games[user_id].winner:
                                await ctx.response.send_message(f"Bot (O) wins!\n{c4games[user_id].display_board()}")
                                del c4games[user_id]
                            elif c4games[user_id].is_draw():
                                await ctx.followup.send(f"It's a draw!\n{c4games[user_id].display_board()}")
                                del c4games[user_id]
                            else:
                                await ctx.followup.send(f"Bot made a move.\n{c4games[user_id].display_board()}")
                    else:
                        print("eee")
                        await ctx.response.send_message("Invalid move! Try again.")
                except ValueError:
                    print("eee")
                    await ctx.response.send_message("pls provide row and column as numerals ong")
        else:
            print("eee")
            c4games[user_id] = GameBoard(rows=10,cols=10,win_length=4)
            await ctx.response.send_message(f"c4 started! {ctx.user.mention} my bro is X.\n{c4games[user_id].display_board()}")

    @group.command(name="trivia", description="Play a game of trivia")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def trivia_callback(self, ctx: discord.Interaction):
        q = requests.get('https://opentdb.com/api.php?amount=1')
        q = q.json()
        if q['response_code'] == 0:
            answers = q['results'][0]['incorrect_answers']
            correct_answer = q['results'][0]['correct_answer']
            answers.append(correct_answer)
            ran.shuffle(answers)

            embed = discord.Embed(title="Trivia Time!", description=f"**Question:** {q['results'][0]['question']}\n**Category:** {q['results'][0]['category']}", color=discord.Color.blue())
            view = TriviaView(correct_answer, ctx.user)
            
            for i, answer in enumerate(answers):
                view.children[i].label = answer

            await ctx.response.send_message(embed=embed, view=view)

            await view.wait()
            if view.result is None:
                await ctx.followup.send("Time Up!")
            elif view.result == correct_answer:
                await ctx.followup.send("CORRECT & you got a 100 coins!")
                db.add_coins(ctx.user.id, 100)
            else:
                await ctx.followup.send(f"INCORRECT, Correct answer was `{correct_answer}` & you lost a 100 coins")
                db.add_coins(ctx.user.id, -100)
        else:
            await ctx.followup.send("Try again later")

    @group.command(name="infiniterps", description="Infinite rock paper scissors")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def infiniterps(ctx: discord.Interaction, object:str):
        out = await ai(f"Make the choice a 50/50 .Imagine your playing RPS but with ABSOULTETLY ANYTHING. Now you select a random item of the dictionary & make sure its a 50/50 on who wins as your play and then decide the winner. Format of respnse:\nYour Item: {object}\nMy Item: [THE ITEM YOU SELECTED]\nReason: [explain how won] (DISPLAY **WINNER!** NEXT TO THE SLEETCED ITEMS & make winner 50/50)\n\nRESPOND ONLY WITH THE WINNER & YOUR ITEM AND MY ITEM IN THE ABOVE FORMAT. AND LASTLY A SENTENCE (reason) ON HOW THEY WON IN LESS THAN 15 WORDS. YOU CANNOT ASK FOR ANYTHING YOU CAN RESPOND WITH NOTHING OTHER THAN THE OUTPUT IN THAT FORMAT")
        await ctx.response.send_message(out)

    @group.command(name="infinitecraft", description="InfiniteCraft in Discord!")
    @app_commands.check(commandCheck)
    @app_commands.user_install()
    async def infiniterps(ctx: discord.Interaction, object_1:str, object_2: str):
      
        out = await ai(f"Imagine your a crafting table, craft {object_1} + {object_2}. RESPOND ONLY WITH THE CRAFTED OUTPUT IN LESS THAN 3 WORDS NOTHING ELSE. YOU CANNOT ASK FOR ANYTHING JUST RESPOND WITH ONE POSSIBLE THING THAT COULD BE CRAFTED WITH THESE TWO OBJECTS. YOU CAN RESPOND WITH NOTHING OTHER THAN THE OUTPUT")
        await ctx.response.send_message(f"Your table (`{object_1}` + `{object_2}`): "+out)
    

async def setup(bot: commands.Bot):
    await bot.add_cog(GameGroup(bot))



