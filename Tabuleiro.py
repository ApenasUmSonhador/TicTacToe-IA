class Tabuleiro:
    tabuleiro = []
    def desenha_tabuleiro(self): 
        "Método responsável por mostrar estádo atual do tabuleiro marcado com 'X', 'O' ou ''."
        for i, linha in enumerate(self.tabuleiro):
            for elemento in linha:
                print(elemento if elemento else " ", end=' | ')
            if i < 2:
                print("\n", "-"*11, sep="")

    def verifica_vitoria(self):
        "Método responsável por avisar vitória no jogo"
        win = self._verifica_verticais() + self._verifica_horizontais() + self._verifica_diagonais()
        if win < 0:
            print("X win")
        elif win > 0:
            print("O win")
        else:
            print("Sem vitoriosos")

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
