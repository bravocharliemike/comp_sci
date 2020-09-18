import random # we'll need the random module to roll the dice

class DicePile:

    def __init__(self, initQuantity, initSides, rollOnCreate=False): # constructor
        self.setQuantity(initQuantity)
        self.setSides(initSides)
        self.__rollCount = 0
        self.rolled = False  # flag to detemine if pile has been rolled
        
        # If user wants to roll the dice right after creating them
        if rollOnCreate:
            self.roll()
        

    def __str__(self): # generate a string representation of the object
        if self.rolled:
            print('The dice have been rolled!')
            resultString = str(self.__results) + f' (roll count: {str(self.__rollCount)})' 
        else:
            resultString = 'not rolled' + f' (roll count: {str(self.__rollCount)})'

        dicescription = self.dicescription()  # builds the string
        return dicescription + ': ' + resultString

    def dicescription(self):
        dicescription = str(self.__quantity) + 'd' + str(self.__sides)
        return dicescription

    def roll(self): # roll the dice
        self.__results = [] # set results to empty list

        for i in range(self.__quantity): # generate random numbers and add to results list
            self.__results.append(random.randint(1, self.__sides)) 
        self.__rollCount += 1
        self.rolled = True

    def getResults(self): # get results list (None if not rolled)
        return self.__results

    def getQuantity(self): # get quantity attribute
        return self.__quantity

    def getSides(self): # get sides attribute
        return self.__sides

    def getRollCount(self):  # get roll count attribute
        return self.__rollCount


    def setQuantity(self, newQuantity): # set quantity attribute
        if int(newQuantity) < 1:
            raise ValueError('dice quantity cannot be less than 1')
        else:
            self.__quantity = int(newQuantity)
            self.__results = None
            self.rolled = False

    def setSides(self, newSides): # set sides attribute
        if int(newSides) < 2:
            raise ValueError('dice sides cannot be less than 2')
        else:
            self.__sides = int(newSides)
            self.__results = None
            self.rolled = False

    def maxTotal(self):
        """Returns the maximum possible sum of a roll"""
        return self.__quantity * self.__sides

    def getAverage(self):
        """Returns the average of the roll results (returns float)"""
        if self.rolled:
            average = sum(self.__results) / self.__quantity
            return average
        else:
            raise AttributeError('Dice have not been rolled!')

    def sortResults(self):
        """Sorts the __results attribute"""
        if self.rolled:
            self.__results.sort()
        else:
            raise AttributeError('dice have not been rolled')

