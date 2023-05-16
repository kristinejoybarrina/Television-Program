# Create a class 

class Television:
    
    # Create constructor and instance variables
    def __init__(self, name, channel, volume_level, power):
        self.name = str(name)
        self.channel = int(channel)
        self.volume_level = int(volume_level)
        self.power = bool(power)
    
    def show_name (self):
        return "Television " + str(self.name) + "'s"
    
    # Create a turn on method
    def turn_on (self):
        return "This TV has been turned on."
    
    # Create a turn off method
    def turn_off (self):
        return "This TV has been turned off."
    
    # Create a get channel method
    def get_channel (self):
        channel_number = self.channel
        return "channel is " + str(channel_number)
    
    # Create a set channel method
    def set_channel (self):
        return "New channel number has been set"
    
    # Create get volume method
    def get_volume (self):
        volume_number = self.volume_level
        return "volume is " + str(volume_number)
     
    # Create set volume method
    def set_volume (self):
        return "New volume level has been set."
    
    # Create channel up method
    def channel_up (self):
        return "The channel number increases to 1."
    
    # Create channel down method
    def channel_down (self):
        return "The channel number decreases to 1."
    
    # Create volume up method
    def volume_up (self):
        return "The volume level increases to 1."
    
    # Create volume down method
    def volume_down (self):
        return "The volume level decreases to 1."
 