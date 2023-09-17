def dmg_tkn(flat, effect):
    prog =  0.25 * (1 + (effect / 100))
    petr_dmg_left = flat * 0.4 * 0.82 / 6
    prog_dmg_left = flat * prog / 6
    dmg = flat * (1 - 0.25 * (1 + (effect / 100)) - 0.4)
    #dota =
    print(petr_dmg_left + prog_dmg_left)


def recoup(dmg, relife, max_life):
    life = 0
    life_left = max_life
    degen = 0
    for tick in range(6):
        life += dmg * relife / 100 / 6
        leech = max_life * 0.2 / 5
        degen -= 352
        life_left += life - 1050
        print(round(life), degen, leech, life_left)
       #6


        #print(life_left)

# recoup(3000, 100, 1500)
#
# dmg_tkn(3000, 50)

# def compute_ticks(damage_interval=0.198, damage_amount=3000, recoup_percentage=1, total_duration=3.0, tick_duration=0.033):
#     num_ticks = int(total_duration / tick_duration)
#     total_recoup_from_one_hit = damage_amount * recoup_percentage
#
#     # Ilość obrażeń zadanych w ciągu 3 sekund
#     hits_in_3_seconds = int(total_duration / damage_interval) + 1
#
#     ticks = []
#     for tick in range(1, num_ticks + 1):
#         total_recoup_this_tick = 0
#         for hit_number in range(hits_in_3_seconds):
#             time_since_this_hit = tick * tick_duration - hit_number * damage_interval
#             if 0 < time_since_this_hit <= 3:
#                 # Obliczenie recoup dla tego strzału w tym ticku
#                 max_hp_per_second_for_this_hit = total_recoup_from_one_hit / total_duration
#                 recoup_for_this_hit_this_tick = 0.5 * max_hp_per_second_for_this_hit * time_since_this_hit * tick_duration
#                 total_recoup_this_tick += recoup_for_this_hit_this_tick
#
#         ticks.append(total_recoup_this_tick)
#
#     return ticks
#
# ticks = compute_ticks()
# print("First tick:", ticks[0])
# print("Last tick:", ticks[-1])


# def compute_ticks(damage_interval=0.198, damage_amount=3000, recoup_percentage=0.1, total_duration=3.0,
#                   tick_duration=0.033):
#     num_ticks = int(total_duration / tick_duration)
#     total_recoup_from_one_hit = damage_amount * recoup_percentage
#     max_hp_per_second_for_one_hit = total_recoup_from_one_hit / total_duration
#
#     # Ilość obrażeń zadanych w ciągu 3 sekund
#     hits_in_3_seconds = int(total_duration / damage_interval) + 1
#
#     ticks = []
#     for tick in range(1, num_ticks + 1):
#         total_recoup_this_tick = 0
#         for hit_number in range(hits_in_3_seconds):
#             time_since_this_hit = tick * tick_duration - hit_number * damage_interval
#
#             if 0 < time_since_this_hit <= 3:
#                 recoup_rate_this_tick_for_this_hit = max_hp_per_second_for_one_hit * time_since_this_hit / total_duration
#                 recoup_for_this_hit_this_tick = recoup_rate_this_tick_for_this_hit * tick_duration
#                 total_recoup_this_tick += recoup_for_this_hit_this_tick
#
#         ticks.append(total_recoup_this_tick)
#
#     return ticks
#
#
# ticks = compute_ticks()
# print("First tick:", ticks[0])
# print("Last tick:", ticks[-1])
# print("Scaled last tick to 1s:", ticks[-1] / 0.033)



def compute_ticks(damage_interval=0.198, damage_amount=3000, recoup_percentage=0.1, total_duration=3.0, tick_duration=0.033):
    total_recoup_from_one_hit = damage_amount * recoup_percentage
    num_ticks = int(total_duration / tick_duration)

    ticks = []
    for tick in range(1, num_ticks + 1):
        current_time = tick * tick_duration
        total_recoup_this_tick = 0

        # Przeszukujemy wszystkie serie obrażeń zadane w ciągu ostatnich 3 sekund
        for time_since_last_hit in range(0, int(total_duration/damage_interval) + 1):
            if 0 < current_time - time_since_last_hit * damage_interval <= 3:
                total_recoup_this_tick += 2 * tick_duration * (current_time - time_since_last_hit * damage_interval) * total_recoup_from_one_hit / (total_duration ** 2)

        ticks.append(total_recoup_this_tick)

    return ticks

ticks = compute_ticks()
print("First tick:", ticks[0])
print("Last tick:", ticks[-1])
print("Scaled last tick to 1s:", ticks[-1] / 0.033)

# for tick in ticks:
#     print(tick)
