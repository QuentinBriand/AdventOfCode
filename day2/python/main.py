from enum import Enum

class AdventOfCodeParts(Enum):
    PART_ONE = 1
    PART_TWO = 2

class RoundResults(Enum):
    WIN = 6
    LOSE = 0
    TIE = 3

class PossiblePlays(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class PossiblePlaysEnemy(Enum):
    A = PossiblePlays.ROCK
    B = PossiblePlays.PAPER
    C = PossiblePlays.SCISSORS

class PossiblePlaysYou(Enum):
    X = PossiblePlays.ROCK
    Y = PossiblePlays.PAPER
    Z = PossiblePlays.SCISSORS

class WantedRound(Enum):
    X = RoundResults.LOSE
    Y = RoundResults.TIE
    Z = RoundResults.WIN

ALL_MOVES = {
    RoundResults.WIN: {
        PossiblePlays.ROCK: PossiblePlays.SCISSORS,
        PossiblePlays.PAPER: PossiblePlays.ROCK,
        PossiblePlays.SCISSORS: PossiblePlays.PAPER
    },
    RoundResults.LOSE: {
        PossiblePlays.SCISSORS: PossiblePlays.ROCK,
        PossiblePlays.ROCK: PossiblePlays.PAPER,
        PossiblePlays.PAPER: PossiblePlays.SCISSORS
    },
    RoundResults.TIE: {
        PossiblePlays.ROCK: PossiblePlays.ROCK,
        PossiblePlays.PAPER: PossiblePlays.PAPER,
        PossiblePlays.SCISSORS: PossiblePlays.SCISSORS
    }
}

def open_input():
    filepath = '../../resources/day02_input'
    with open(filepath) as fp:
        lines = fp.readlines()
    return lines

def is_winning(enemy: PossiblePlays, you: PossiblePlays) -> RoundResults:
    if (enemy == you):
        return RoundResults.TIE
    if(ALL_MOVES[RoundResults.WIN][you] == enemy):
        return RoundResults.WIN
    else:
        return RoundResults.LOSE

def find_good_move(enemy: PossiblePlays, result: RoundResults):
    if result == RoundResults.LOSE: result = RoundResults.WIN
    elif result == RoundResults.WIN: result = RoundResults.LOSE

    return ALL_MOVES[result][enemy]

def play_round(round: str):
    moves = round.split(' ')
    enemy : PossiblePlays = PossiblePlaysEnemy[moves[0][0]].value
    you : PossiblePlays = PossiblePlaysYou[moves[1][0]].value
    your_score = you.value + is_winning(enemy, you).value
    enemy_score = enemy.value + is_winning(you, enemy).value

    desired_round = WantedRound[moves[1][0]].value
    wanted_move = find_good_move(enemy, desired_round)
    return {
        "YOURS": {
            "PART_ONE": your_score,
            "PART_TWO": wanted_move.value + desired_round.value
        },
        "ENEMY": {
            "PART_ONE": enemy_score,
            "PART_TWO": enemy.value + desired_round.value
        }
    }

if __name__ == '__main__':
    lines = open_input()
    your_total_score = 0
    enemy_total_score = 0

    your_total_score_part_two = 0
    enemy_total_score_part_two = 0

    for line in lines:
        result = play_round(line)
        your_total_score += result['YOURS'][AdventOfCodeParts.PART_ONE.name]
        enemy_total_score += result['ENEMY'][AdventOfCodeParts.PART_ONE.name]

        your_total_score_part_two += result['YOURS'][AdventOfCodeParts.PART_TWO.name]
        enemy_total_score_part_two += result['ENEMY'][AdventOfCodeParts.PART_TWO.name]

    print("Your Total Score: ", your_total_score)
    print("Enemy Total Score: ", enemy_total_score)
    print()
    print("------------------ PART TWO ------------------")
    print("Your Total Score: ", your_total_score_part_two)
    print("Enemy Total Score: ", enemy_total_score_part_two)