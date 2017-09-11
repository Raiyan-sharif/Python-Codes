
class Raiyan:
    def __init__(self,**kwargs):
        self._Data=kwargs
    def GetName(self):
        return self._Data["Name"]
    def GetAge(self):
        return self._Data["Age"]
