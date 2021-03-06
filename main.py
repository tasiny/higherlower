import random
from art import logo
from art import vs
from game_data import data
end_game = False
def random_influencer():
    influencer = random.choice(data)
    return influencer
user_score = 0
influencer_list = []
influencer_list.append(random_influencer())
influencer_list.append(random_influencer())
while influencer_list[0] == influencer_list[1]:
    influencer_list[1] = influencer_list.append(random_influencer())
follower_count_list = [(influencer_list[0]['follower_count']), (influencer_list[1]['follower_count'])]

print(f"Compare A: {influencer_list[0]['name']}, a {influencer_list[0]['description']}, from {influencer_list[0]['country']}")

print(f"Against B: {influencer_list[1]['name']}, a {influencer_list[1]['description']}, from {influencer_list[1]['country']}")
while end_game == False:
    user_choice = input("Which one has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if influencer_list[0]['follower_count'] == max(follower_count_list):
            user_score += 1
            print(user_score)
            influencer_list = [influencer_list[0]]
            follower_count_list = [influencer_list[0]['follower_count']]
            influencer_list.append(random_influencer())
            while influencer_list[0] == influencer_list[1]:
                influencer_list[1] = influencer_list.append(random_influencer())
            follower_count_list.append(influencer_list[1]['follower_count'])
            print(f"Compare A: {influencer_list[0]['name']}, a {influencer_list[0]['description']}, from {influencer_list[0]['country']}")
            print(f"Compare B: {influencer_list[1]['name']}, a {influencer_list[1]['description']}, from {influencer_list[1]['country']}")

        else:
            end_game = True
            print("Game over")
            print(f"Your final score was: {user_score}.")

    elif user_choice == 'b':
        if influencer_list[1]['follower_count'] == max(follower_count_list):
            user_score += 1
            print(user_score)
            influencer_list = [influencer_list[1]]
            follower_count_list = [influencer_list[0]['follower_count']]
            influencer_list.append(random_influencer())
            while influencer_list[0] == influencer_list[1]:
                influencer_list[1] = influencer_list.append(random_influencer())
            follower_count_list.append(influencer_list[1]['follower_count'])
            print(f"Compare A: {influencer_list[0]['name']}, a {influencer_list[0]['description']}, from {influencer_list[0]['country']}")
            print(f"Compare B: {influencer_list[1]['name']}, a {influencer_list[1]['description']}, from {influencer_list[1]['country']}")
        else:
            end_game = True
            print("Game over")
            print(f"Your final score was: {user_score}.")
