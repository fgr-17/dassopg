class Log:

    def __init__(self,id,id_dev,state,ts):
        self.__id = id
        self.__id_dev=id_dev
        self.__state=state
        self.__ts=ts


    @staticmethod
    def encode_log(obj):
        return {"id":obj.__id,"id_dev":obj.__id_dev,"ts":obj.__ts,"state":obj.__state}

    