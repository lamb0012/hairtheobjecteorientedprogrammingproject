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
        
