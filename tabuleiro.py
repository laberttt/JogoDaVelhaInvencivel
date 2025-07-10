# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4
    OUTRO_TIPO = 2

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        #somando linhas
        for linha in self.matriz:
            soma = sum(linha)
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
            
        #somando colunas
        for coluna in range(0, 3):
            soma = self.matriz[0][coluna] + self.matriz[1][coluna] + self.matriz[2][coluna]
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
            
        #somando diagonal principal
        soma_diagonal_principal = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        if soma_diagonal_principal == 3:
            return Tabuleiro.JOGADOR_0
        elif soma_diagonal_principal == 12:
            return Tabuleiro.JOGADOR_X
        
        #somando diagonal secundária
        soma_diagonal_secundaria = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if soma_diagonal_secundaria == 3:
            return Tabuleiro.JOGADOR_0
        elif soma_diagonal_secundaria == 12:
            return Tabuleiro.JOGADOR_X
            
            
        # Verifica se há empate
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                    return Tabuleiro.DESCONHECIDO
        
        # Empate
        return Tabuleiro.OUTRO_TIPO