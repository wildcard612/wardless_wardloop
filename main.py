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
def compute_ticks_degen(damage_interval=0.198, damage_amount=2480, total_duration=3.0, tick_duration=0.033, progenesis = 37, petri = 40):
    total_recoup_from_one_hit = (damage_amount * (1 - progenesis / 100)) * (1 - petri * 1.41 / 100 )
    num_ticks = int(total_duration / tick_duration)

    ticks_degen = []
    for tick in range(1, num_ticks + 1):
        current_time = tick * tick_duration
        total_recoup_this_tick = 0

        # Przeszukujemy wszystkie serie obrażeń zadane w ciągu ostatnich 3 sekund
        for time_since_last_hit in range(0, int(total_duration/damage_interval) + 1):
            if 0 < current_time - time_since_last_hit * damage_interval <= 3:
                total_recoup_this_tick += 2 * tick_duration * (current_time - time_since_last_hit * damage_interval) * total_recoup_from_one_hit / (total_duration ** 2)

        ticks_degen.append(round(total_recoup_this_tick, 5))

    return ticks_degen

ticks_degen = compute_ticks_degen()
print("First tick degen:", ticks_degen[0])
print("Last tick degen:", ticks_degen[-1])
print("Scaled last tick degen to 1s:", ticks_degen[-1] / 0.033)


def compute_ticks(damage_interval=0.198, damage_amount=2480, recoup_percentage=1.2, total_duration=3.0, tick_duration=0.033):
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

        ticks.append(round(total_recoup_this_tick, 5))

    return ticks

ticks = compute_ticks()
print("First tick:", ticks[0])
print("Last tick:", ticks[-1])
print("Scaled last tick to 1s:", ticks[-1] / 0.033)

def recoup_dif():
    result = []
    for rec, degen in zip(ticks, ticks_degen):
        result.append(rec -degen)

    return result




#print(ticks)


def compute_cumulative_net_gain_per_tick(damage_interval=0.198, damage_amount=3280, recoup_percentage=1.2, total_duration=3.0, tick_duration=0.033, life = 3000):
    ticks = compute_ticks(damage_interval, damage_amount, recoup_percentage, total_duration, tick_duration)

    net_gains = []
    cumulative_gain = 0
    leech = life * 0.4 / 30.3
    for i, recoup in enumerate(ticks):
        current_time = i * tick_duration

        # Jeśli to tick z obrażeniami
        if current_time % damage_interval < tick_duration or current_time % damage_interval == 0:
            damage_this_tick = damage_amount * 0.1375
        else:
            damage_this_tick = 0

        net_gain = recoup - damage_this_tick - ticks_degen[i] + leech
        cumulative_gain += net_gain
        net_gains.append(cumulative_gain)

    return net_gains

# cumulative_net_gains = compute_cumulative_net_gain_per_tick()
# for i, gain in enumerate(cumulative_net_gains):
#     print(f"Tick {i+1}: {gain:.2f} HP")





def find_lowest_cumulative_net_gain(damage_interval=0.23, damage_amount=3280, recoup_percentage=1.2, total_duration=3.0,
                                    tick_duration=0.033, progenesis = 40, petri= 45, life = 2700):
    ticks = compute_ticks(damage_interval, damage_amount, recoup_percentage, total_duration, tick_duration)
    ticks_degen = compute_ticks_degen(damage_interval, damage_amount, total_duration, tick_duration, progenesis, petri)
    leech = life * 0.4 / 30.3
    net_gains = []
    cumulative_gain = 0
    for i, recoup in enumerate(ticks):
        current_time = i * tick_duration

        # Jeśli to tick z obrażeniami
        if current_time % damage_interval < tick_duration or current_time % damage_interval == 0:
            damage_this_tick = damage_amount * (1 - petri/100) * (1 -  progenesis / 100)
        else:
            damage_this_tick = 0

        net_gain = recoup - damage_this_tick - ticks_degen[i] + leech
        cumulative_gain += net_gain
        net_gains.append(cumulative_gain)

    # Znajdź najniższą wartość i jej indeks
    lowest_value = min(net_gains)
    tick_at_lowest = net_gains.index(lowest_value) + 1

    return lowest_value, tick_at_lowest

lowest_value, tick_at_lowest = find_lowest_cumulative_net_gain()
print(f"Najniższa wartość to: {lowest_value:.2f} HP, która wystąpiła w ticku {tick_at_lowest}.")


#print(recoup_dif()[25])

#print(sum(ticks_degen[:25]))