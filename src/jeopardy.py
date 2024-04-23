def print_scores(heading_message):
    print(heading_message)
    print("Player 1:   ", scores["1"])
    print("Player 2:   ", scores["2"])
    print("Player 3:   ", scores["3"])
    print()


def get_wager():
    while True:
        wager = input("How much did they lose/gain? Please enter a negative number or positive number (ex. -200 or 200): ")
        try:
            return int(wager)
            break
        except ValueError:
            if wager == "":
                return ""
            print(f"Error: {wager} is not a valid wager")


def play_round(question_count):
    for n in range(question_count):
        print(f"Question {n+1} of {question_count}")

        unanswered_players = set(["1", "2", "3"])
        while unanswered_players:
            player = str(input("Which player answered? Please answer player 1, player 2, or player 3, or ENTER to move on: "))
            if not player:
                break  # move on
            elif player not in scores:
                print(f"Player {player} isn't a valid player")
            elif player not in unanswered_players:
                print(f"Player {player} has already answered")

            wager = get_wager()
            if not wager:
                continue

            scores[player] += wager
            unanswered_players.remove(player)
            if wager > 0:
                break  # first positive answer moves one
            
        print_scores("Running total scores:")


scores = {"1": 0, "2": 0, "3": 0}
question_count = 2

play_round(question_count)
print_scores("Here are the scores before starting Double Jeopardy:")

play_round(question_count)
print_scores("Here are the final totals for the contestants to make wagers!")

## TODO: We could take wagers here and enforce what they can be
##        then we could print the real total!
