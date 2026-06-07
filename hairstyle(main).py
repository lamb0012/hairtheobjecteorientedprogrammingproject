from abc import ABC, abstractmethod

class Hairstyle(ABC):
    @abstractmethod
    def style(self):
        pass

class curly_hair(Hairstyle):
    def style(self):
        self.style = "curly hair"
        print("You'll be curly.")
class straight_hair(Hairstyle):
    def style(self):
        self.style = "straight hair"
        print("You'll be straight.")
class fluffy_hair(Hairstyle):
    def style(self):
        self.style = "fluffy hair"
        print("You'll be fluffy.")
class no_hair(Hairstyle):
    def style(self):
        self.style = "bald"
        print("You'll be bald.")
class toomuch_hair(Hairstyle):
    def style(self):
        self.style = "forest hair"
        print("You'll be having all the hair you like.")

choice = input("What style would you like : (/curly/straight/fluffy/bald/forest) ")

def aply_styles(hair: Hairstyle):
    hair.style()

styles = {
    "curly": curly_hair,
    "straight": straight_hair,
    "fluffy": fluffy_hair,
    "bald": no_hair,
    "forest": toomuch_hair
}

hair_class = styles.get(choice)

if hair_class:
    hair = hair_class()
    aply_styles(hair)
else :
    print ("Sir, it's not on the menu...")
