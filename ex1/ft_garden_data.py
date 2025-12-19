class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def test(self):
        print(self.name)

def ft_garden_data():
    plant1 = Plant("pink", 22, 5)
    plant1.test()

ft_garden_data()