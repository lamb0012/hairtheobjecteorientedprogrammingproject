from hairstyle import curly_hair, straight_hair, fluffy_hair, no_hair, toomuch_hair
from characterfromhair import chb, gb, sf, hud, wf, gn, dc


hair_list = {
    "curly": CurlyHair,
    "straight": StraightHair,
    "fluffy": FluffyHair,
    "bald": Bald,
    "forest": ForestHair
}

character_list = {
    "1": chb,
    "2": gb,
    "3": sf,
    "4": hud,
    "5": wf,
    "6": gn,
    "7": dc
}

print("Choose hairstyle: (curly / straight / fluffy / bald / forest)")
hair_choice = input("Hair: (input choices above) ")

print("""
Choose character:
1. Claude
2. George
3. Sheila
4. LaFayette
5. Woof
6. Jeannie
7. Dionne & Crissy
""")

char_choice = input("Character: (input numbers corelated to the character) ")

hair = hair_list.get(hair_choice)
character = character_list.get(char_choice)

if hair and character:
    hair_obj = hair()
    char_obj = character()
    char_obj.cc(hair_obj)
else:
    print("Yo, can't you read the list?")
