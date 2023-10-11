# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[], play_order={}):
    if prev_play=='':
        prev_play='R'
    prediction='S'
    opponent_history.append(prev_play)

    if(len(opponent_history)>=5):
        last_five = "".join(opponent_history[-5:])
        # print(last_five)
        play_order[last_five] = play_order.get(last_five, 0) + 1
        # print("ye hai play order", play_order)
        potential_plays=["".join([*opponent_history[-4:],v]) for v in ['R', 'P', 'S']]
        sub_order={
            k:play_order[k]
            for k in potential_plays if k in play_order
        }
        # print(sub_order)
        # print(play_order)

        if sub_order:
            prediction=max(sub_order, key=sub_order.get)[-1]


    viable_options={'P':'S','R':'P', 'S':'R' }
 
    guess = viable_options[prediction]
    # print(guess)

    # guess = viable_options[most_frequent]


    # print(guess)
    return guess
