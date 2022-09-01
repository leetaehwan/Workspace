def display_stuff(treasure_box):
    print("Congraturation!! you got a treasure box")
    for i, k in treasure_box.items():
        print("you have {} {}pcs".format(i, k['pcs'))

def total_silver(treasure_box, coin_per_treasure):


treasure_box = {'rope': {'coin': 1, 'pcs': 2},
                'apple': {'coin': 2, 'pcs': 10},
                'torch': {'coin': 2, 'pcs': 6},
                'gold coin': {'coin': 5, 'pcs': 50},
                'knife': {'coin': 30, 'pcs': 1},
               	'arrow': {'coin': 1, 'pcs': 30}
               }

display_stuff(treasure_box)
total_silver(treasure_box, coin_per_treasure)