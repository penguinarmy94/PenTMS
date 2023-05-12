from typing import List, Any, Dict, Tuple, Union, Generator, Optional
# creating a Class that the user can utilize in order to create different national parks

STATES = ["CA", "FL", "TX", "NY", "RI", "WS"]

class Wildlife:
    def __init__(self, name: str, number_of_legs: int, species: str):
        self.name: str = name
        self.leg_count: int = number_of_legs
        self.species: str = species

class Monument: # TODO
    def __init__(self, name: str, year_built: int, historic_value: str):
        self.year: int = year_built
        self.name: str = name
        self.historic_value: str = historic_value

    def __repr__(self) -> str:
        return f"The monument's name is {self.name}, it was built in {self.year}, and it is valuable because {self.historic_value}"
class MonumentLibrary: # TODO
    def __init__(self):
        self.__library: List[Monument] = []
    
    def add_monument(self, monument_name: str):
        self.__library.append(monument_name)
    
    def remove_monument(self, monument_name: str):
        index = 0
        while index < len(self.__library):
            monument: Monument = self.__library[index]
            if monument.name == monument_name:
                self.__library.remove(monument)
                break
            else:
                index += 1

    def __contains__(self, name: str) -> bool:
        for monument in self.__library:
            if monument.name == name:
                return True
            
        return False

    def __len__(self) -> int:
        return len(self.__library)
    
    def __iter__(self) -> Generator[Monument, None, None]:
        for monument in self.__library:
            yield monument

    def __repr__(self) -> str:
        return "\n".join([str(monuments) for monuments in self.__library])
    

class Hikes:
    def __init__(self, name: str, length: float, difficulty: str, elevation_gain: int, type_of_trail: str): 
        self.length: float = length
        self.elevation_gain: int = elevation_gain
        self.trail_type: str = type_of_trail
        self.difficulty: str = difficulty
        self.name: str = name

    def __repr__(self) -> str:
        return f"The trail name is {self.name}, it is a {self.trail_type} that is {self.length} miles long with an elevation gain of {self.elevation_gain} feet. This trail is for more {self.difficulty} hikers, hike at your own risk."
    
class HikeLibrary: 
    def __init__(self): 
        self.__library = List[Hikes] = []
    
    def add_hikes(self, hike_name: str):
        self.__library.append(hike_name)
    
    def remove_hikes(self, hike_name: str):
        index = 0
        pass



class NationalPark:
    def __init__(self, name: str, county: str, state: str, terrain_type: str, perimeter: float):
        self.__county: str = county
        self.__state: str = state
        self.__terrain_type: str = terrain_type
        self.__monuments: MonumentLibrary = MonumentLibrary()
        self.__trails: List[str] = []
        self.perimeter: float = perimeter
        self.name: str = name 
        self.__wildlife: List[Wildlife] = []
    
    def __repr__(self) -> str:
        return f"{self.name} [{self.county}, {self.state}] => {self.wild_life_types()} live in this {self.__terrain_type} that is {self.perimeter} acres long"
    
    @property
    def county(self) -> str:
        return self.__county
    
    @property
    def state(self) -> str:
        return  self.__state
    
    @property
    def wildlife(self) -> Tuple[Wildlife]:
        return tuple(self.__wildlife)
    
    @property
    def monuments(self) -> Tuple[Monument]:
        return tuple(self.__monuments)
        
    
    @county.setter
    def county(self, new_county: str):
        if ";" in new_county:
            raise ValueError("The value for new_county cannot have ;")
        else:
            self.__county = new_county
    
    @state.setter
    def state(self, new_state: str):
        if new_state not in STATES:
            raise ValueError(f"The state {new_state} is not allowed!")
        else:
            self.__state = new_state
    
    def add_hikes(self, name: str, length: float, difficulty: str, elevation_gain: int, trail_type):
        new_hike: Hikes = Hikes(name= name, length= length, difficulty= difficulty, elevation_gain= elevation_gain, type_of_trail=trail_type)
        self.__trails.append(new_hike)
    
    def add_monument(self, name: str, **opt):
        monuments: Monument = Monument(name= name, year_built= opt.get("year_built", 1920), historic_value= opt.get("historic_value", "unknown"))
        self.__monuments.add_monument(monuments)
    
    def remove_monument(self, monument_name):
        if monument_name in self.__monuments:
            self.__monuments.remove_monument(monument_name) 

    def hikes_count(self) -> int:
        return len(self.__trails)
    
    def monument_count(self) -> int:
        return len(self.__monuments)
    
    def add_wildlife(self, species: str, **options):
        wildlife: Wildlife = Wildlife(name=options.get("name", "Undefined"), number_of_legs=options.get("number_of_legs", 4), species=species)
        self.__wildlife.append(wildlife)
    
    def wild_life_types(self) -> List[str]:
        wildlife_types: List[str] = []
        
        for wildlife in self.__wildlife:
            if wildlife.species not in wildlife_types:
                wildlife_types.append(wildlife.species)
        
        return wildlife_types
        

class NationalParkLibrary:
    def __init__(self):
        self.__library: List[NationalPark] = []
    
    def add_park(self, park: NationalPark):
        self.__library.append(park)

    def __repr__(self) -> str:
        return "\n".join([str(park) for park in self.__library])
    
    def __iter__(self) -> Generator[NationalPark,None,None]:
        for park in self.__library:
            yield park

if __name__ == "__main__":
    # a = NationalPark(name="Yosemite", county="Santa Clara", state="CA", terrain_type="desert", perimeter=5000)
    # b = NationalPark(name="Yellowstone", county="Pensicola", state="NY", terrain_type="forest", perimeter=9825.67)
    # lib = NationalParkLibrary()

    
    # a.add_wildlife(species="deer", name="Dolly", number_of_legs=4)
    # a.add_wildlife(species="wolf", name="Speedy", number_of_legs=4)
    # a.add_wildlife(species="squirrel", name="Nutter", number_of_legs=2)
    
    # b.add_wildlife(species="moose", name="Cranky", number_of_legs=4)
    # b.add_wildlife(species="parrot", name="Chatty", number_of_legs=2)

    # a.add_monument(name="Big Tower", year_built= 1930, historic_value= "None")
    # a.add_monument(name="Small Tower", year_built= 1850, historic_value="Some")

    # b.add_monument(name="Big Rock", year_built= 1950, historic_value= "Giant Rock! ")

    # a.add_monument()
    
    # lib.add_park(a)
    # lib.add_park(b)
    
    # a = Monument(name="Big Tower", year_built= 1930, historic_value= "None")
    # b = Monument(name="Small Tower", year_built= 1850, historic_value="Some")
    
    
    parks = NationalPark("Yosemite", "Mariposa", "CA", "Mixed", 5000)
    

    # # assert parks.monument_count() == 2
    # print(parks.monuments)
    # parks.remove_monument(a.name)
    # print(parks.monuments)

    a = Hikes(name="Jones Peak",length= 7,difficulty= "Advanced",elevation_gain= 3000,type_of_trail= "Out and Back")
    b = Hikes("Strawberry Peak", 6.5, "Advanced", 2700, "Out and Back")

    parks.add_hikes(a.name, a.length, a.difficulty, a.elevation_gain, a.trail_type)
    parks.add_hikes(b.name, b.length, b.difficulty, b.elevation_gain, b.trail_type)
    print(a, b)

    assert parks.hikes_count() == 2
    
    # print(a,b)
    # print(a.monuments, b.monuments) # [Monument(..), Monument(...)] [Monument(..), Monument(..)]

    #monumentlibrary object has no attribute append 
    #monumentlibrary len() function