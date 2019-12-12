import json

class Device:

    def __init__(self, idDevice, name, ip, state):
        self.__id = idDevice
        self.__name = name
        self.__ip = ip
        self.__state = state
        
    @staticmethod
    def encodeDevice(obj):
        return {"id":obj.__id,"name":obj.__name,"ip":obj.__ip,"state":obj.__state}
