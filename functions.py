from typing import List, Any, Dict, Tuple, Union, Generator, Optional
# creating a Class that the user can utilize in order to create different national parks

STATES = ["CA", "FL", "TX", "NY", "RI", "WS"]

class Wildlife:
    def __init__(self, name: str, number_of_legs: int, species: str):
        self.name: str = name
        self.leg_count: int = number_of_legs
        self.species: str = species

class Monument: # TODO
    def __init__(self):
        pass
    
class MonumentLibrary: # TODO
    def __init__(self):
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
        pass # TODO
        
    
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
    
    def add_trail(self, new_trail: str):
        self.__trails.append(new_trail)
    
    def add_monument(self, monument: str):
        self.__monuments.append(monument)
    
    def trail_count(self) -> int:
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
    a = NationalPark(name="Yosemite", county="Santa Clara", state="CA", terrain_type="desert", perimeter=5000)
    b = NationalPark(name="Yellowstone", county="Pensicola", state="NY", terrain_type="forest", perimeter=9825.67)
    lib = NationalParkLibrary()
    
    a.add_wildlife(species="deer", name="Dolly", number_of_legs=4)
    a.add_wildlife(species="wolf", name="Speedy", number_of_legs=4)
    a.add_wildlife(species="squirrel", name="Nutter", number_of_legs=2)
    
    b.add_wildlife(species="moose", name="Cranky", number_of_legs=4)
    b.add_wildlife(species="parrot", name="Chatty", number_of_legs=2)
    
    lib.add_park(a)
    lib.add_park(b)
    
    print(a,b)
    print(a.monuments, b.monuments) # [Monument(..), Monument(...)] [Monument(..), Monument(..)]

    #not sure what i dd but i my last action merged my branch and i lost the entire functions section of the project. copied from repository. 