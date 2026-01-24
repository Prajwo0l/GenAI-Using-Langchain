from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """

# Define a class named Car
class Car:
    # Constructor to initialize instance attributes
    def __init__(self, make, model, year):
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute

    # Method (function inside a class) to display car information
    def describe(self):
        return {self.year} {self.make} {self.model}

    # Method to start the car
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running.")

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Access object attributes
print(my_car.describe())  # Output: 2023 Toyota Camry

# Call object methods (functions)
my_car.start_engine()     # Output: The Toyota Camry's engine is now running.   

"""

splitter= RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=300,
        chunk_overlap=0

)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks[1])