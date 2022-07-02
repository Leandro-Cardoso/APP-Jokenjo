if __name__ == '__main__':
    from random import randint

class Jokenpo:
    def __init__(self):
        self.gamemode = 0
        self.players = ['', '']
        self.scores = [0, 0]
        self.choices = ['', '']
        self.all_choices = ['rock', 'paper', 'scissors']
    def set_game_mode(self, gamemode = 0):
        '''Gamemode = 0 (P1 VS CPU), Gamemode = 1 (P1 VS P2)'''
        gamemodes = [0, 1]
        if self.gamemode not in gamemodes:
            self.gamemode = 0
        else:
            self.gamemode = gamemode
    def set_players(self, p1 = 'p1', p2 = 'p2'):
        p1 = str(p1).title().split()
        p1 = ' '.join(p1)
        if self.gamemode == 0:
            p2 = 'CPU'
        elif self.gamemode == 1:
            p2 = str(p2).title().split()
            p2 = ' '.join(p2)
        self.players = [p1, p2]
    def win_score(self, player, score = 1):
        for i in range(len(self.players)):
            if player == self.players[i]:
                self.scores[i] += score
    def make_choices(self, choice1, choice2):
        if self.gamemode == 0:
            choice2 = self.all_choices[randint(0, 2)]
        self.choices[0] = choice1
        self.choices[1] = choice2
        # VERIFICAR SE OPÇÃO EXISTE
    # FUNÇÃO PARA VERIFICAR SE P1 GANHOU, EMPATOU OU PERDEU
    def winner(self) -> str:
        '''Return the winner (P1 name, P2 name or None)'''
        pass

if __name__ == '__main__':
    # Tests:
    game = Jokenpo()

    game.set_players(' leandro   cardoso', ' luna  dark')
    print('Gamemode:', game.gamemode, 'Players:', game.players)
    game.set_game_mode(1)
    game.set_players(' leandro   cardoso', ' luna  dark')
    print('Gamemode:', game.gamemode, 'Players:', game.players)

    game.win_score(game.players[0])
    game.win_score(game.players[0])
    game.win_score(game.players[1])
    print(game.players[0] + ':', game.scores[0])
    print(game.players[1] + ':', game.scores[1])

    game.set_game_mode(0)
    game.make_choices('scissors', 'paper')
    print(game.players[0] + ':', game.choices[0])
    print(game.players[1] + ':', game.choices[1])
