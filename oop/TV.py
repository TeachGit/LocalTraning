class TV:
    def __init__(self, channel=1, volumeLevel=10, on=False):
        self.__channel = channel
        self.__volumeLevel = volumeLevel
        self.__on = on

    def getChannel(self):
        return self.__channel

    def setChannel(self, channel):
        if self.__on and 1 <= channel <= 120:
            self.__channel = channel

    def getVolumeLevel(self):
        return self.__volumeLevel

    def setVolumeLevel(self, volumeLevel):
        if self.__on and 1 <= volumeLevel <= 7:
            self.__volumeLevel = volumeLevel

    def isOn(self):
        return self.__on

    def setOn(self, on):
        self.__on = on

    def volumeUp(self):
        if self.__on and self.__volumeLevel < 7:
            self.__volumeLevel += 1

    def volumeDown(self):
        if self.__on and self.__ > 1:
            self.__volumeLevel -= 1

    def channelUp(self):
        if self.__channel < 120 and self.__on:
            self.__channel += 1

    def channelDown(self):
        if self.__on and self.__channel > 1:
            self.__channel -= 1

    def __str__(self):
        status = "On" if self.__on else "Off"
        return "TV is " + status + " Channel " + str(self.__channel) + " Volume " + str(self.__volumeLevel)


tv = TV(10, 5, True)
print(tv)
tv.volumeUp()
tv.channelDown()
tv.setChannel(120)
print(tv)
