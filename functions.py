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
    
    def __init__(self, name: str, length: float, length_measurement_type: str, difficulty: str, peak_elevation: int, type_of_trail: str): 
        self.__max_elevation: int = 90000
        self.__is_open: bool = True
        self.__length: float = length # TODO: create property and setter functions for length
        self.__name: str = name # TODO: create a setter for name
        self.peak_elevation = peak_elevation
        self.trail_type = type_of_trail
        self.difficulty = difficulty
        
        self.set_length_measurement_type(length_measurement_type)

    
    @property
    def name(self) -> str:
        return self.__name
    
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
    
    def set_length_measurement_type(self, length_measurement_type: str):
        if length_measurement_type.lower() in self.TRAIL_LENGTH_MEASUREMENT_TYPES:
            self.__length_measurement_type = length_measurement_type
        else:
            raise ValueError(f"The trail length measurement type '{length_measurement_type}' is not allowed. Choose one of the following: {self.TRAIL_LENGTH_MEASUREMENT_TYPES}")
    
    def __repr__(self) -> str:
        return f"The trail name is {self.name}, it is a {self.trail_type} that is {self.__length} {self.__length_measurement_type} long with an elevation gain of {self.peak_elevation} feet. This trail is for more {self.difficulty} hikers, hike at your own risk."
    
class TrailLibrary: 
    def __init__(self): 
        self.__library: List[Trail] = []
    
    def add_hikes(self, hike_name: str):
        self.__library.append(hike_name)
    
    def remove_hikes(self, hike_name: str):
        index = 0
        while index < len(self, self.__library):
            hike: Trail = self.__library[index]
            if hike.name == hike_name:
                self.__library.remove(hike)
                break
            else: 
                index += 1

    def __len__(self) -> int:
        return len(self.__library)
    
    def __iter__(self) -> Generator[Trail, None, None]:
        for hike in self.__library:
            yield hike
    
    def __repr__(self) -> str:
            return "\n".join([str(hikes) for hikes in self.__library])
    
    def __contains__(self, name: str) -> bool:
        for hike in self.__library: 
            if hike.name == name:
                return True 
        
        return False


class NationalPark:
    def __init__(self, name: str, county: str, state: str, terrain_type: str, perimeter: float):
        self.__county: str = county
        self.__state: str = state
        self.__terrain_type: str = terrain_type
        self.__monuments: MonumentLibrary = MonumentLibrary()
        self.__trails: TrailLibrary = TrailLibrary()
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
        new_hike: Hike = Hike(name= name, length= length, difficulty= difficulty, elevation_gain= elevation_gain, type_of_trail=trail_type)
        self.__trails.add_hikes(new_hike)

    def remove_hike(self, hike_name: str):
        if hike_name in self.__trails:
            self.__trails.remove_hikes(hike_name)
    
    def add_monument(self, name: str, **opt):
        monuments: Monument = Monument(name= name, year_built= opt.get("year_built", 1920), historic_value= opt.get("historic_value", "unknown"))
        self.__monuments.add_monument(monuments)
    
    def remove_monument(self, monument_name: str):
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

    a = Trail(name="Jones Peak", length=-5, length_measurement_type="kilometers", difficulty= "advanced", peak_elevation=3000, type_of_trail="Out and back")
    # b = Trail("Strawberry Peak", 6.5, "Advanced", 2700, "Out and Back")
    # c = Trail("Mt Baldy", 14, "Advanced", 5000, "Hard")

    # parks.add_hikes(a.name, a.length, a.difficulty, a.elevation_gain, a.trail_type)
    # parks.add_hikes(b.name, b.length, b.difficulty, b.elevation_gain, b.trail_type)
    # parks.add_hikes(c.name, c.length, c.difficulty, c.elevation_gain, c.trail_type)

    # print(a, b)
    # print(c)

    # assert parks.hikes_count() == 3
    
    
    # parks.remove_hike(a.name)
    # assert parks.hikes_count() == 2
    
    print(a)
    
    
    # print(a,b)
    # print(a.monuments, b.monuments) # [Monument(..), Monument(...)] [Monument(..), Monument(..)]

    #monumentlibrary object has no attribute append 
    #monumentlibrary len() function
    #not sure what i dd but i my last action merged my branch and i lost the entire functions section of the project. copied from repository. 
