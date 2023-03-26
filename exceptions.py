class Incorrect_data(Exception):
     def __init__(self,params):
        self.params = params
