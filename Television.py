# Create a class 

class Television:
    
    # Create constructor and instance variables
    def __init__(self, channel, volume_level, power):
        self.channel = int(channel)
        self.volume_level = int(volume_level)
        self.power = bool(power)
        
    # Create a turn on method
    def turn_on (self):
        return 
    
    # Create a turn off method
    def turn_off (self):
        return
    
    # Create a get channel method
    def get_channel (self):
        channel_num = self.channel
        return channel_num
    
    # Create a set channel method
    def set_channel (self):
        return 
    
    # Create get volume method
    def get_volume (self):
        get_volume = self.volume_level
        return get_volume
    
    # Create set volume method
    def set_volume (self):
        return
    
    # Create channel up method
    def channel_up (self):
        return
    
    