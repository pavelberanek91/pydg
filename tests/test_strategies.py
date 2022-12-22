'''
Name:
    test_strategies

Description:
    Module test_strategies is used for behavior verification of strategies.py module.

Tests:
    test_instantiate_abstract_strategy
    
'''

import pytest
from strategies import strategies


def test_instantiate_abstract_strategy():
    with pytest.raises(Exception):
        agent = strategies.Strategy()


#Alway Cooperate Test
@pytest.mark.parametrize("game_history, expected_choice",
[
    (   [], 
        'cooperate'
    ),

    (   [
            ('cooperate', 'cooperate')
        ], 
        'cooperate'),

    (   [
            ('cooperate', 'defect')
        ], 
        'cooperate'
    ),

    (
        [
            ('cooperate', 'cooperate'), 
            ('cooperate', 'defect')
        ], 
        'cooperate'
    ),

    (
        [
            ('cooperate', 'defect'),
            ('cooperate', 'cooperate'),
        ], 
        'cooperate'),
])
def test_AlwaysCooperate_play(game_history, expected_choice):
    agent = strategies.AlwaysCooperate()
    agent.game_history = game_history
    choice = agent.play()
    assert choice == expected_choice


#Alway Defect Test
@pytest.mark.parametrize("game_history, expected_choice",
[
    (   [], 
        'defect'
    ),

    (   [
            ('defect', 'cooperate')
        ], 
        'defect'
    ),

    (   [
            ('defect', 'defect')
        ], 
        'defect'
    ),

    (
        [
            ('defect', 'cooperate'), 
            ('defect', 'defect')
        ], 
        'defect'
    ),

    (
        [
            ('defect', 'defect'),
            ('defect', 'cooperate'),
        ], 
        'defect'
    ),
])
def test_AlwaysDefect_play(game_history, expected_choice):
    agent = strategies.AlwaysDefect()
    agent.game_history = game_history
    choice = agent.play()
    assert choice == expected_choice


#Tit For Tat test
@pytest.mark.parametrize("game_history, expected_choice",
[
    (   [], 
        'cooperate'
    ),

    (   [
            ('cooperate', 'cooperate')
        ], 
        'cooperate'
    ),

    (   [
            ('cooperate', 'defect')
        ], 
        'defect'
    ),

    (
        [
            ('cooperate', 'cooperate'), 
            ('cooperate', 'defect')
        ], 
        'defect'
    ),

    (
        [
            ('cooperate', 'defect'),
            ('defect', 'cooperate'),
        ], 
        'cooperate'
    ),

    (
        [
            ('cooperate', 'defect'),
            ('defect', 'defect'),
        ], 
        'defect'
    ),
])
def test_TitForTat_play(game_history, expected_choice):
    agent = strategies.TitForTat()
    agent.game_history = game_history
    choice = agent.play()
    assert choice == expected_choice
    

#TODO:
#[ ] add test markings