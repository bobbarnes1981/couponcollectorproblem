import random
import pygame

def get_available_cards():
    available_cards = []
    for c in range(0, total_num_cards):
        available_cards.append(c)
    return available_cards

def draw_graph(display, display_width, display_height, data, f):
    graph_width = display_width - (10 * 2)
    graph_height = display_height - (10 * 2)
    x_max = len(data)
    x_scale = graph_width / x_max
    y_max = max(i['avg'] for i in data)
    y_scale = graph_height / y_max
    # x axis
    pygame.draw.line(display, white, (10,display_height-10), (display_width-10,display_height-10), 2)
    for x in range(0, x_max, 10):
        x_point = int(10+(x_scale*x))
        pygame.draw.line(display, white, (x_point,display_height-10),(x_point,display_height-10+5), 1)
        t = f.render(str(x), True, white)
        display.blit(t, (x_point, display_height-10))
    # y axis
    pygame.draw.line(display, white, (10,display_height-10), (10,10), 2)
    for y in range(0, y_max, 10):
        y_point = int(display_height-10-(y_scale*y))
        pygame.draw.line(display, white, (10,y_point), (10-5,y_point), 1)
        t = f.render(str(y), True, white)
        display.blit(t, (10, y_point))
    # plot data
    prev_point = (10,display_height-10)
    for i in range(0, len(data)):
        curr_point = (int(10+(x_scale*i)),int(display_height-10-(y_scale*data[i]['avg'])))
        pygame.draw.line(display, white, prev_point, curr_point, 1)
        prev_point = curr_point

data = []
number_of_simulations = 100

pygame.init()
pygame.font.init()
f = pygame.font.SysFont('Courier', 10)

total_num_cards = 207
cards_per_pack = 8

available_cards = get_available_cards()

sum_samples = 0
for i in range(0, number_of_simulations):
    collection = []
    total_samples = 0
    opened_packs = 0

    while len(collection) < 207:
        # simulate opening pack and collecting cards
        sampled_cards = random.sample(available_cards, cards_per_pack)
        opened_packs += 1
        for sampled_card in sampled_cards:
            total_samples += 1
            if sampled_card not in collection:
                collection.append(sampled_card)
        # update data
        if len(data) < opened_packs:
            data.append({'sum': len(collection), 'avg': len(collection), 'total': 1})
        else:
            s = data[opened_packs-1]['sum'] + len(collection)
            t = data[opened_packs-1]['total'] + 1
            a = s / t
            data[opened_packs-1] = {'sum': s, 'avg': a, 'total': t}
    print(total_samples)
    sum_samples += total_samples

print('average: ', sum_samples / number_of_simulations)
print('average packs: ', sum_samples / number_of_simulations / cards_per_pack)
print(data)

# draw when finished, todo: draw during simulation

black = (0,0,0)
white = (255,255,255)

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    display.fill(black)
    draw_graph(display, display_width, display_height, data, f)
    pygame.display.update()

