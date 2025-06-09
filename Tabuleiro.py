from os import name, system
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def limpa_tela(self):
        if name == "nt":
            system('cls')
        else:
            system('clear')

    def desenha_tabuleiro(self): 
        "Método responsável por mostrar estádo atual do tabuleiro marcado com 'X', 'O' ou ''."
        for i, linha in enumerate(self.tabuleiro):
            j = 0
            for elemento in linha:
                print(elemento if elemento else ' ', end=' ')
                if j < 2:
                    print("| ", end='')
                    j+=1
            if i < 2:
                print("\n", "-"*9, sep="")

    def verifica_fim_de_jogo(self):
        "Método responsável por verificar se o jogo terminou"
        empate = self.verifica_empate()
        vitoria, _ = self.verifica_vitoria()
        return vitoria or empate
    
    def verifica_empate(self):
        "Método responsável por verificar se o jogo terminou em empate"
        for linha in self.tabuleiro:
            for elemento in linha:
                if elemento == '':
                    return False
        print("Empate")
        return True
    
    def verifica_vitoria(self):
        "Método responsável por avisar vitória no jogo"
        win = self._verifica_verticais() + self._verifica_horizontais() + self._verifica_diagonais()
        if win < 0:
            print("X win")
            return True, win
        elif win > 0:
            print("O win")
            return True, win
        print("Sem vitoriosos")
        return False, win

    def _verifica_verticais(self):
        """
        Método auxiliar para verificar vitória via verticais do tabuleiro.
        Retorna -1 caso "X" vença
        Retorna 1 caso "O" vença
        Retorna 0 caso não se aplique
        """
        for i in range(3):
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i]:
                if self.tabuleiro[0][i] == 'X':
                    return -1
                elif self.tabuleiro[0][i] == 'O':
                    return 1
        return 0

    def _verifica_horizontais(self):
        """
        Método auxiliar para verificar vitória via horizontais do tabuleiro.
        Retorna -1 caso "X" vença
        Retorna 1 caso "O" vença
        Retorna 0 caso não se aplique
        """
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2]:
                if self.tabuleiro[i][0] == 'X':
                    return -1
                elif self.tabuleiro[i][0] == 'O':
                    return 1
        return 0

    def _verifica_diagonais(self):
        """
        Método auxiliar para verificar vitória via diagonais do tabuleiro.
        Retorna -1 caso "X" vença
        Retorna 1 caso "O" vença
        Retorna 0 caso não se aplique
        """
        
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] or \
            self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0]:
            if self.tabuleiro[1][1] == 'X':
                return -1
            if self.tabuleiro[1][1] == 'O':
                return 1
        return 0

    def faz_movimento(self, jogador, movimento):
        "Método responsável por realizar movimento de jogador"
        linha, coluna = (movimento - 1) // 3, (movimento - 1) % 3
        if self.tabuleiro[linha][coluna] != '':
            movimento = int(input("Movimento inválido, tente novamente."))
            self.faz_movimento(jogador, movimento)
        else:
            self.tabuleiro[linha][coluna] = jogador

tabuleiro = Tabuleiro()
while not tabuleiro.verifica_fim_de_jogo():
    tabuleiro.limpa_tela()
    tabuleiro.desenha_tabuleiro()
    movimento = int(input("\n Digite o movimento (1-9)"))
    tabuleiro.faz_movimento('X', movimento)
    tabuleiro.verifica_vitoria()
    
    if not tabuleiro.verifica_fim_de_jogo():
        tabuleiro.limpa_tela()
        tabuleiro.desenha_tabuleiro()
        movimento = int(input("\n Digite o movimento (1-9)"))    
        tabuleiro.faz_movimento('O', movimento)
        tabuleiro.verifica_vitoria()

tabuleiro.limpa_tela()
tabuleiro.desenha_tabuleiro()
