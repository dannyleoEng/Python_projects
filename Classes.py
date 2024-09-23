import time
class Microwave:
    def __init__(self, model: str, power_rating: str, meal: str, power_level: int):
        self.meal = meal
        self.model = model
        self.power_rating = power_rating
        self.power_level = power_level
        self.turned_on: bool = False

    def turn_on(self):
        if self.turned_on:
            print(f"{self.model} is already turned on!!!!")
        else:
            self.turned_on = True
            print(f"{self.model} is now turned on")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"{self.model} is now turned off")
        else:
            print(f"{self.model} is already off!")

    def run(self, second: int):
        if self.turned_on:
            print(f"{self.model} is now running for {second} seconds")
            print(f"cooking {self.meal} .........")
            time.sleep(second)
            print("---------------")
            print(f"{self.meal} is nicely done 😎")
        else:
            print(f"{self.model} must be turned on first!!")
    def status(self):
        if self.turned_on:
            print(f"{self.model} is on and running at {self.power_level} watts with a power rating of {self.power_rating} is currently cooking {self.meal} ")
        else:
            self.turned_on = False
            print(f"{self.model} is off and running at {self.power_level} watts with a power rating of {self.power_rating} is currently cooking {self.meal}")


scanfrost: Microwave = Microwave("Scanfrost", "B", "rice", 240)
scanfrost.turn_on()
scanfrost.status()
scanfrost.run(5)
scanfrost.turn_off()