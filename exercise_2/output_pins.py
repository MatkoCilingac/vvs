from exercise_2.rgb_led import RGBled

RGBledInstancia: RGBled
'''while True:
    blue_light.value(1)
    green_light.value(0)
    red_light.value(0)
    sleep(2)
    blue_light.value(0)
    green_light.value(1)
    red_light.value(0)
    sleep(2)
    blue_light.value(0)
    green_light.value(0)
    red_light.value(1)
    sleep(2)'''

print("vyber si farbu: "
      "1 = cervena"
      "2 = zelena"
      "3 = modra"
      "4 = slabomodra"
      "5 = zlta"
      "6 = ruzova")
      
while True:
    try:
            cislo: int = int(input("cislo > "))
    except ValueError:
            print("please enter a number")
            continue

    if cislo == 1:
        RGBledInstancia.ukaz_modra()
    elif cislo == 2:
        RGBledInstancia.ukaz_zlta()
    elif cislo == 3:
        RGBledInstancia.ukaz_cervena()
    elif cislo == 4:
        RGBledInstancia.ukaz_ruzova()
    elif cislo == 5:
        RGBledInstancia.ukaz_zelena()
    elif cislo == 6:
        RGBledInstancia.ukaz_slabomodra()
    else:
        print("nespravne cislo")

