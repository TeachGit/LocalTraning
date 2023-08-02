class Television:
    def __init__(self, power=False, channel=1, volume=10):
        self.power = power
        self.channel = channel
        self.volume = volume

    def show(self):
        print("Status of TV is : Power {0} Channel {1} Volume {2}".format(self.power, self.channel, self.volume))

    def setChannel(self, channel):
        if self.power == True and channel > 0:
            self.channel = channel
        else:
            print("Channel must bigger than zero")

    def setVolume(self, volume):
        if self.power == True and volume > 0 and volume < 100:
            self.volume = volume
        else:
            print("Volume must be between ")

    def powerOn(self):
        self.power = True

    def powerOff(self):
        self.power = False

    def channelUp(self):
        if self.power == True and self.channel < 50:
            self.channel = self.channel + 1


tv = Television()
tv.show()
tv.powerOn()
tv.setChannel(20)
tv.setVolume(15)
tv.show()
