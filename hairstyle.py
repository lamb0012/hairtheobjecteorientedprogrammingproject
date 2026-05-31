class curly_hair():
    def style(self):
        self.style = "curly hair"
        print("You'll be curly.")
class straight_hair():
    def style(self):
        self.style = "straight hair"
        print("You'll be straight.")
class fluffy_hair():
    def style(self):
        self.style = "fluffy hair"
        print("You'll be fluffy.")
class no_hair():
    def style(self):
        self.style = "bald"
        print("You'll be bald.")
class toomuch_hair():
    def style(self):
        self.style = "forest hair"
        print("You'll be having all the hair you like.")

style = input("What style would you like : (/curly/straight/fluffy/bald/forest) ")

if style == "curly":
    hair = curly_hair()
elif style == "straight":
    hair = straight_hair()
elif style == "fluffy":
    hair = fluffy_hair()
elif style == "bald":
    hair = no_hair()
elif style == "forest":
    hair = toomuch_hair()
else :
    print ("Sir, it's not on the menu...")

if hasattr(hair, "style"):
    hair.style()
