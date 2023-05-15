# Create a class 

class Television:
    
    # Create constructor and instance variables
    def __init__(self, channel, volume_level, power):
        self.channel = int(channel)
        self.volume_level = int(volume_level)
        self.power = bool(power)
        
    # Create a turn on method
    def turn_on (self):
        power_on = "Turns on this TV."
        return power_on
    
    # Create a turn off method
    def turn_off (self):
        power_off = "This turns off the TV."
        return power_off
    
    # Create a get channel method
    def get_channel (self):
        channel_num = self.channel
        channel_message = "Returns the channel for this TV." 
        return str(channel_num) + channel_message
    
        
    
    
    