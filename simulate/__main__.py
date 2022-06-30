import random

total_num_cards = 207
cards_per_pack = 8

available_cards = []
for c in range(0, total_num_cards):
    available_cards.append(c)

number_of_simulations = 100
sum_samples = 0
for i in range(0, number_of_simulations):
    collection = []
    total_samples = 0

    while len(collection) < 207:
        sampled_cards = random.sample(available_cards, cards_per_pack)
        #print(sampled_cards)
        for sampled_card in sampled_cards:
            total_samples += 1
            if sampled_card not in collection:
                collection.append(sampled_card)
    print(total_samples)
    sum_samples += total_samples
print('average: ', sum_samples / number_of_simulations)
print('average packs: ', sum_samples / number_of_simulations / cards_per_pack)

