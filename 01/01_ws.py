
import random
# secret = 'test'
# secret = 'rapido'
secret_list = ['terra', 'placebo', 'unique', 'katamaran', 'agnostic', 'elbow']

def user_input(lght):
    # c = input("Give a letter (if more than 1 whole phrase guess assumed)")
    while True:
        c = input("Give a letter (if more than 1 whole phrase guess assumed):").lower().lstrip().rstrip()
        if c.isdigit():
            print("Phrase doesn't contains digits! Try again.")
        elif c == '':
            print("No input! Try again.")
        elif 1 < len(c) < lght:
            print("Too short for guessing! Try again.")
        else:
            break
    print(f"your input is '{c}'")
    return c

def check_if_in_phrase(char, phr, masked_phr):
    print(10*'===')
    result = 0
    pos = []
    for i, n in enumerate(phr):
        if n == char and masked_phr[i] == '*':
            # print(f"FOUND not discover char {char} at index {i}")
            pos.append(i)
            break
        elif n == char and masked_phr[i] != '*':
            # print(f"char {char} at index {i} ALREADY REVEALED")
            continue
        else:
            result = -1
    if len(pos) > 0:
        result = pos[0]
        # masked_phr[counter] = char
    else:
        result = -1

    # print(f"masked after check: {masked_phr}, counter: {counter}, pos: {pos}")
    # print('check in phraseout', result)
    return result


def ui_geom(ui, secretq, cnt):
    game_result = 2
    ui_len = len(ui)
    if len(secretq) < ui_len:
        print(f'Phrase {ui} longer than secret - you loose!')
        game_result = 1 #'Loose by clumsiness'
    elif len(secretq) == ui_len:
        print(f'Guess phrase try')
        if ui.lower() == secretq.lower():
            print(f'Phrase match! You win!')
            game_result = 0 #'Win by guessing!'
            cnt = cnt
            # break
        else:
            print(f'Phrase not match!')
            cnt -= 1
    else:
        game_result = 2
    # print('GEOM: ', game_result, cnt)
    return game_result, cnt

def main():
    secretq = random.choice(secret_list).lower()
    # print(secretq)
    masked_string = len(secretq) * '*'.split()
    tolerance = 3
    available_moves = len(secretq)+tolerance
    cnt = available_moves
    game_results = ['Win by guessing!', 'Loose by clumsiness', 'Win by teddious work!', 'Defeat. You was not able to guess secret in']
    game_result = 0

    ui_hist = []
    print(f"START: {masked_string} You have to guess {len(secretq)} letters.")

    while (cnt > 0) and ('*' in masked_string):
        ui = user_input(len(secretq))
        ui_hist.append(ui)
        game_result, cnt = ui_geom(ui, secretq, cnt)

        if (game_result == 0) or (game_result == 1):
            break

        else:
            res = check_if_in_phrase(ui, secretq, masked_string)
            if res == -1:
                print("FAIL!")
                cnt += res
            else:
                print("MATCH!")
                masked_string[res] = ui.upper()

            print(f"Current phrase is: {masked_string}, guessed {len(secretq)-masked_string.count('*')}/{len(secretq)}, try {cnt}")

            if cnt == 0:
                game_result = 3

    print(20*'##')
    print(f"Secret phrase: '{secretq}', length: {len(secretq)}")
    print(f"Game result: {game_results[game_result]} in {len(ui_hist) if cnt > 0 else available_moves} moves!")
    print(f"HITS: {len(ui_hist)  if game_result == 0 else len(secretq)-masked_string.count('*')}")
    print(f"ALL MOVES: {len(ui_hist)}")
    # print(f"MISTAKES: {'guessing was flawless!' if cnt == available_moves else len(ui_hist) - len(secretq)-masked_string.count('*')}")
    print(f"HISTORY of MOVES: {ui_hist}")
    print(20 * '##')
main()

