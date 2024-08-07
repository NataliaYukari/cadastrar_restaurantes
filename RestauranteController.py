import RestauranteModel as Model

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()
