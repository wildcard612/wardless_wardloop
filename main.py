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

recoup(3000, 100, 1500)

dmg_tkn(3000, 50)