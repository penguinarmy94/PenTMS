from typing import List, Any, Dict, Tuple, Union, Generator, Optional

# def max_of_two(x, y):
#     if x > y:
#         return x
#     return y

# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))

# print(max_of_three(10, 11, 12))

# def sum_of_numbers(a, b, c, d, e):
#     sum = a+b+c+d+e
#     return sum 

# print(sum_of_numbers(8, 2, 3, 0, 7))
#works 

# print(sum((8, 2, 3, 0, 7)))

# multiply all the numbers in a list function 
# def product_of_numbers(a, b, c, d, e):
#     product = a * b * c *d *e 
#     return product

# print(product_of_numbers(8, 2, 3, -1, 7))
#works 

# reverse a string function 
# def reverse_the_string(string):
#     rstr1 = ''
#     index = len(string)
#     while index > 0:
    #     rstr1 += string[index -1]
    #     index = index -1
    # return rstr1

# print(reverse_the_string("1234abcd"))
#got solution from the website 

#write a python function to calculate the factorial of a number 
# come back to this one 


#write a function to check whether a number falls within a given range 
# def number_within_range_check(number):
#     if number in range(0, 40):
#         print("Yes, it is within the range")
#     else: 
#         print("This number is not within the range")
# number_within_range_check(100)
#works 

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




# list_of_parks = []
# y = True 
# while y:
#     p_name = input("Please enter the park name: ")
#     p_county = input("Please enter the county where it is found: ")
#     p_state = input("Please enter the state in which it is found: ")
#     p_type = input("Please enter the type of terrain (Desert, Mountain, Mixed): ")

#     new_park = NationalPark(p_name, p_county, p_state, p_type)
#     list_of_parks.append(new_park)
#     print(list_of_parks)

#     again = input("Would you like to enter another park? (Y/N) ").upper()
#     if again == 'N':
#         y = False
#     else: 
#         True

# list_of_hikes = []

# class Hikes: 
#     def __init__(self, name, forest, state, elevation_gain, difficulty):
#         self.name = name
#         self.forest = forest
#         self.state = state
#         self.elevation_gain = elevation_gain
#         self.difficulty = difficulty


# strawberry_peak = Hikes("Strawberry Peak", "Angeles", "California", "3000", "Hard")
# print(f"{strawberry_peak.name}, {strawberry_peak.forest}, {strawberry_peak.state}")


# function that takes a list of numbers as input and returns the average of all the numbers in the list 
# def average(*numbers):
#     return sum(numbers) / len(numbers)

# sum = average(10, 12, 40, 60)
# print(sum)

#building a dictionary
# cardict = {
#     "brand" : "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }

# print(cardict)

























# class gym():
#     def __init__(self,gymname):
#         self.gymname=gymname
#         self.memlist=[]
#     def regMem(self,obj):
#         if obj.ageMember()==True:
#            self.memlist.append(obj)
#            return True, "mem in!!!"
#     def printMem(self):
#         for n in self.memlist:
#             print(n)

# class gymMember():
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def __str__(self):
#         return(str(self.fname)+str(self.lname)+str(self.age))

#     def ageMember(self):
#         if self.age>=18:
#             return True
#     def printMemlist(self):
#         for n in self.memlist:
#             print(n)

# yes='y'
# g=gym("EzGym") # shift this line outside of the while loop
# while yes=="y":
#     name=input('enter f name')
#     lname=input('enter l name')
#     age=int(input('enter age'))
#     n=gymMember(name,lname,age)
#     print(g.regMem(n))
#     g.printMem()

# class above taken from stackoverflow, mostly to review different examples of classes and functions within 


 