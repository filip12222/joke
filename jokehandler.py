import requests








import datetime


class jokehandler:
    
    def __init__(self, adress):
        self.adress = adress
        self.nu = datetime.datetime.now()
        #print(f"\nConstructor till klassen körs: {funcnu}\n")
        
    def get_joke(self):
        req = requests.get(self.adress)
        json_data = req.json()
        joke = json_data['joke']
        
        return joke