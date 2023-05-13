# Create a class 

class Television:
    
    def __init__(self, channel, volume_level, power):
        self.channel = int(channel)
        self.volume_level = int(volume_level)
        self.power = bool(power)
    
    def try_lang (self):
        try_natin = self.power
        return try_natin
    