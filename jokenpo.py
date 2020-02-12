"""
O objetivo é fazer um juiz de Jokenpo
que dada a jogada dos dois jogadores
informa o resultado da partida.

As regras são as seguintes:

Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra
"""


# Imports


import pytest
from enum import Enum, auto

# Atribuições


class Resultado(Enum):
    PEDRA = auto()
    EMPATE = auto()
    TESOURA = auto()
    PAPEL = auto()
    FOO = auto()
    BAR = auto()


regras = {
    Resultado.TESOURA: Resultado.PAPEL,
    Resultado.PEDRA: Resultado.TESOURA,
    Resultado.PAPEL: Resultado.PEDRA,
}

# Jokenpo


def jokenpo(player1: Resultado, player2: Resultado) -> Resultado:
    """Função que avalia uma rodada de jokepo
    
    Arguments:
        Resultado1 {Resultado} -- Primeiro Resultado 
        Resultado2 {Resultado} -- Segundo Resultado
    
    Returns:
        Resultado -- O vencedor ou empate!
    """
    if player1 == player2:
        return Resultado.EMPATE
    return player1 if regras[player1] == player2 else player2


# Testes de Empates


def test_pedra_pedra() -> None:
    assert jokenpo(Resultado.PEDRA, Resultado.PEDRA) == Resultado.EMPATE


def test_tesoura_tesoura() -> None:
    assert jokenpo(Resultado.TESOURA, Resultado.TESOURA) == Resultado.EMPATE


def test_papel_papel() -> None:
    assert jokenpo(Resultado.PAPEL, Resultado.PAPEL) == Resultado.EMPATE


# Testes de Batalhas


def test_pedra_tesoura() -> None:
    assert jokenpo(Resultado.PEDRA, Resultado.TESOURA) == Resultado.PEDRA


def test_tesoura_pedra() -> None:
    assert jokenpo(Resultado.TESOURA, Resultado.PEDRA) == Resultado.PEDRA


def test_papel_pedra() -> None:
    assert jokenpo(Resultado.PAPEL, Resultado.PEDRA) == Resultado.PAPEL


def test_pedra_papel() -> None:
    assert jokenpo(Resultado.PEDRA, Resultado.PAPEL) == Resultado.PAPEL


def test_tesoura_papel() -> None:
    assert jokenpo(Resultado.TESOURA, Resultado.PAPEL) == Resultado.TESOURA


def test_papel_tesoura() -> None:
    assert jokenpo(Resultado.PAPEL, Resultado.TESOURA) == Resultado.TESOURA


# Teste de exceção(Irá lançar uma exceção quando os players não jogarem: Resultado.PEDRA, PAPEL OU TESOURA)
def test_foo_bar() -> None:
    with pytest.raises(KeyError):
        jokenpo(Resultado.FOO, Resultado.BAR)
