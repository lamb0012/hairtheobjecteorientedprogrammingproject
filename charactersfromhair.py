from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self):
        self.nm = ""

    @abstractmethod
    def cc(self, hair):
        pass

class chb(Character):
    def __init__(self):
        self.nm = "Claude Hooper Bukowski"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("The idealistic young man from Flushing, Queens, who gets drafted into the Vietnam War and wrestles with the decision of whether to fight or follow his pacifist friends.")


class gb(Character):
    def __init__(self):
        self.nm = "George Berger"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("The charismatic leader of the hippie tribe.")


class sf(Character):
    def __init__(self):
        self.nm = "Sheila Franklin"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("An NYU student and political activist who is heavily involved in social causes and caught in a love triangle with Claude and Berger.")

class hud(Character):
    def __init__(self):
        self.nm = "LaFayette Johnson"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("A militant African-American member of the tribe who declares himself the president of the United States of Love.")

class wf(Character):
    def __init__(self):
        self.nm = "Woof Dachshund"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("A gentle, free-loving member of the group who blurs traditional gender and sexual norms.")

class gn(Character):
    def __init__(self):
        self.nm = "Jeannie Ryan"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("A pregnant tribe member who has deep, unrequited feelings for Claude.")

class dc(Character):
    def __init__(self):
        self.nm = "Dionne & Crissy"

    def cc(self, hair):
        print(self.nm)
        print(hair.style())
        print("Prominent members and vocalists within the hippie tribe who help drive the story's music and activism.")


        
