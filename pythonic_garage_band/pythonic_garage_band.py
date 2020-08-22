from abc import abstractmethod, ABC
class Band(ABC):
    
    all_bands=[]
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.all_bands.append(self)
    
    def play_solos(self):
        solo=[]
        for i in self.members :
            solo.append(i.play_solo())
        return solo
    
    def play_song(self):
        return self.song
    
    
    def __str__(self):
        members = ','.join(str(v) for v in self.members)
        return f'{self.name} band, the members are {self.members}'
    
    def __repr__(self):
        
        return f'{self.name} band, the members are {self.members}'
    
    @classmethod
    def to_list(cls):
        return cls.all_bands


class Musician(ABC):

    def __init__(self,name):
        self.name = name
        # self.members = members
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    @staticmethod
    def play_solo():
        pass
   
   @staticmethod
   def get_instrument():
       pass
   
  
class Guitarist(Musician):
   def play_solo(self):
       return "waa"
   
   def get_instrument(self):
       return "Guitar"


class Bassist(Musician):
   def __init__(self,name,instrument):
       self.instrument = instrument
       super().__init__(name)
   def play_solo(self):
       return "tantantan"
   
   def get_instrument(self):
       return self.instrument


class Drummer(Musician):
   def play_solo(self):
       return "dum dum  dum"
   def get_instrument(self):
       return "Drum"


if __name__ == "__main__" :
    guitarist = Guitarist("guitarist")
    drummer = Drummer("drummer")
    bassist = Bassist("bassist","Bass guitar")
    tbep = Band("The Black Eyed Peas", [guitarist,drummer])
    print(bassist.get_instrument())
  