# Create a class 

class Television:
    
    # Create constructor and instance variables
    def __init__(self, channel, volume_level, power):
        self.channel = int(channel)
        self.volume_level = int(volume_level)
        self.power = bool(power)
        
    # Create a turn on method
    def turn_on (self):
        power_on = "Turns on this tv."
        return power_on
    
    
    