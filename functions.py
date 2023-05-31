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
    
class Trail:
    DIFFICULTIES: Tuple[str] = ("intermediate", "moderate", "advanced")
    TRAIL_TYPES: Tuple[str] = ("one way", "loop", "out and back")
    TRAIL_LENGTH_MEASUREMENT_TYPES: Tuple[str] = ("miles", "kilometers")
    TRAIL_NAME_UNALLOWED_CHARACTERS: str = r":;'\"=+-_}{}[]|\*<>?/~@$"
    
    def __init__(self, name: str, length: float, length_measurement_type: str, difficulty: str, peak_elevation: int, type_of_trail: str): 
        self.__max_elevation: int = 90000
        self.__max_length: float = 300
        self.__is_open: bool = True
        self.set_length_measurement_type(length_measurement_type)
        self.length: float = length # TODO: create property and setter functions for length {DONE}
        self.name: str = name # TODO: create a setter for name {DONE}
        self.peak_elevation = peak_elevation
        self.trail_type = type_of_trail
        self.difficulty = difficulty
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        for illegal_character in self.TRAIL_NAME_UNALLOWED_CHARACTERS:
            if illegal_character in name:
               raise ValueError(f"The name {name} is not allowed because the character '{illegal_character}' is not allowed.") 
        
        self.__name = name 
    
    @property
    def difficulty(self) -> str:
        return self.__difficulty
    
    @difficulty.setter
    def difficulty(self, level: str):
        if level.lower() in self.DIFFICULTIES:
            self.__difficulty = level.lower()
        else:
            raise ValueError(f"The difficulty level '{level}' is not allowed. Choose one of the following: {self.DIFFICULTIES}")
    
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        if length >= 0 and length <= self.__max_length:
            self.__length = length
        elif length > self.__max_length:
            raise ValueError(f"The maximum length cannot be more than {self.__max_length}")
        else:
            raise ValueError("The length cannot be less than 0")

    @property
    def trail_type(self) -> str:
        return self.__trail_type
    
    @trail_type.setter
    def trail_type(self, trail_type_value: str):
        if trail_type_value.lower() in self.TRAIL_TYPES:
            self.__trail_type = trail_type_value.lower()
        else:
            raise ValueError(f"The trail type '{trail_type_value}' is not allowed. Choose one of the following: {self.TRAIL_TYPES}")

    @property
    def is_open(self) -> bool:
        return self.__is_open
    
    @property
    def peak_elevation(self) -> int:
        return self.__peak_elevation
    
    @peak_elevation.setter
    def peak_elevation(self, elevation: int):
        if elevation >= 0 and elevation < self.__max_elevation:
            self.__peak_elevation = elevation
        elif elevation > self.__max_elevation:
            raise ValueError(f"The peak elevation cannot be more than {self.__max_elevation}")
        else:
            raise ValueError("The peak elevation cannot be negative")
    
    @property
    def length_measurement_type(self) -> str:
        return self.__length_measurement_type

    def set_length_measurement_type(self, length_measurement_type: str):
        if length_measurement_type in self.TRAIL_LENGTH_MEASUREMENT_TYPES:
            self.__length_measurement_type = length_measurement_type.lower() 
        else:
            raise ValueError(f"The trail length measurement type '{length_measurement_type}' is not allowed. Choose one of the following: {self.TRAIL_LENGTH_MEASUREMENT_TYPES}")
    
    def __repr__(self) -> str:
        return f"The trail name is {self.name}, it is a {self.trail_type} that is {self.__length} {self.__length_measurement_type} long with an elevation gain of {self.peak_elevation} feet. This trail is for more {self.difficulty} hikers, hike at your own risk."

    def __str__(self) -> str:
        return self.__repr__()

class TrailLibrary: 
    def __init__(self): 
        self.__library: List[Trail] = []
    
    def __len__(self) -> int:
        return len(self.__library)
    
    def __iter__(self) -> Generator[Trail, None, None]:
        for trail in self.__library:
            yield trail

    def __repr__(self) -> str:
            return "\n".join([str(trail) for trail in self.__library])
    
    def __contains__(self, trail_to_find: Trail) -> bool:
        for trail in self.__library: 
            if trail == trail_to_find:
                return True
        
        return False
    
    def add_trail(self, trail: Trail):    
        if self.trail_exists_by_name(trail_name=trail.name) == True:
            raise ValueError(f"Oh no! Trail '{trail.name}' already exists")
        else:
            self.__library.append(trail)
    
    def remove_trail(self, trail_name: str) -> bool:
        index: int = 0
        
        while index < len(self.__library):
            trail: Trail = self.__library[index]
            
            if trail.name == trail_name:
                self.__library.remove(trail)
                return True
            else: 
                index += 1
        
        return False

    def trail_exists_by_name(self, trail_name: str) -> bool:
        return len(self.find_trails_by_name(trail_name=trail_name)) >= 1
    
    def find_trails_by_name(self, trail_name: str) -> List[Trail]:
        trails_found: List[Trail] = []
        
        for trail in self.__library:
            if trail.name == trail_name:
                trails_found.append(trail)
        
        return trails_found

class NationalPark:
    def __init__(self, name: str, county: str, state: str, terrain_type: str, perimeter: float):
        self.__county: str = county
        self.__state: str = state
        self.__terrain_type: str = terrain_type
        self.__monuments: MonumentLibrary = MonumentLibrary()
        self.__trail: TrailLibrary = TrailLibrary()
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
    
    def add_trail(self, name: str, length: float,length_measurement_type: str,  difficulty: str, peak_elevation: int, trail_type):
        new_trail: Trail = Trail(name= name, length= length,length_measurement_type=length_measurement_type, difficulty= difficulty, peak_elevation= peak_elevation, type_of_trail=trail_type)
        self.__trail.add_trail(new_trail)

    def remove_trail(self, trail_name: str):
        if trail_name in self.__trail:
            self.__trail.remove_trail(trail_name)
    
    def add_monument(self, name: str, **opt):
        monuments: Monument = Monument(name= name, year_built= opt.get("year_built", 1920), historic_value= opt.get("historic_value", "unknown"))
        self.__monuments.add_monument(monuments)
    
    def remove_monument(self, monument_name: str):
        if monument_name in self.__monuments:
            self.__monuments.remove_monument(monument_name) 

    def trail_count(self) -> int:
        return len(self.__trail)
    
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

    a = Trail(name='Jones Peak', length=5, length_measurement_type="miles", difficulty= "advanced", peak_elevation=3000, type_of_trail="Out and back")
    b = Trail(name="Strawberry Peak", length= 6.5, length_measurement_type= "miles", difficulty="Advanced", peak_elevation=2700, type_of_trail="Out and Back")
    c = Trail(name= "Mt Baldy", length=14, length_measurement_type="miles",  difficulty="Advanced", peak_elevation = 5000, type_of_trail="Loop")

    parks.add_trail(a.name, a.length, a.length_measurement_type, a.difficulty, a.peak_elevation, a.trail_type)
    parks.add_trail(b.name, b.length, b.length_measurement_type,  b.difficulty, b.peak_elevation, b.trail_type)
    parks.add_trail(c.name, c.length, c.length_measurement_type, c.difficulty, c.peak_elevation, c.trail_type)

    
    d = Trail(name="Strawberry Peak", length=10, length_measurement_type="kilometers", difficulty="moderate", peak_elevation=550, type_of_trail="loop")
    
    parks.add_trail(d.name, d.length, d.length_measurement_type, d.difficulty, d.peak_elevation, d.trail_type)
    
    parks.remove_trail(b.name)

    assert parks.trail_count() == 2
    
    
    

 
