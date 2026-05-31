class chb():
    def cc(self):
        self.nm = "Claude Hooper Bukowski"
        print ("The idealistic young man from Flushing, Queens, who gets drafted into the Vietnam War and wrestles with the decision of whether to fight or follow his pacifist friends.")
class gb():
    def cc(self):
        self.nm = "George Berger"
        print ("The irreverent, charismatic leader of the hippie tribe.")
class sf():
    def cc(self):
        self.nm = "Sheila Franklin"
        print ("An NYU student and political activist who is heavily involved in social causes and caught in a love triangle with Claude and Berger.")
class hud():
    def cc(self):
        self.nm = "LaFayette Johnson"
        print ("A militant African-American member of the tribe who declares himself the president of the United States of Love.")
class wf():
    def cc(self):
        self.nm = "Woof Dachshund"
        print ("A gentle, free-loving member of the group who blurs traditional gender and sexual norms.")
class gn():
    def cc(self):
        self.nm = "Jeannie Ryan"
        print ("A pregnant tribe member who has deep, unrequited feelings for Claude.")
class dc():
    def cc(self):
        self.nm = "Dionne & Crissy"
        print ("Prominent members and vocalists within the hippie tribe who help drive the story's music and activism.")



print("""
Choose a character:
1. Claude Hooper Bukowski
2. George Berger
3. Shelia Franklin
4. LaFayette Johnson
5. Woof Dachshund
6. Jeannie Ryan
7. Dionne & Crissy
""")
cca = input("Which character's personality from (Hair The Musical) do you want to know? ")
if cca == "1":
    hair = chb()
elif cca == "2":
    hair = gb()
elif cca == "3":
    hair = sf()
elif cca == "4":
    hair = hud()
elif cca == "5":
    hair = wf()
elif cca == "6":
    hair = gn()
elif cca == "7":
    hair = dc()
else :
    print ("Sir, it's not on the list...")

if hair:
    hair.cc()
