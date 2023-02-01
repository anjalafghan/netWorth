
class GetNetworth():

    def __init__(self):
        pass
    
    def getMortgage(self):
        return 150.0
    
    def getLiability(self):
        mort = self.getMortgage()
        return 1.0

    def getAsset(self):
        return 2.0
    
    def calculateNetworth(self,asset,liability):
        return asset - liability

