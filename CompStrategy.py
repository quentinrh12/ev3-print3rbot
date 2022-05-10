

class CompositionalStrategy():

    def __init__(self) -> None:

        self.ruleOfThirds = []

        self.correlatedWords = []
        self.secondaryCompStrategy = None
    
    def newElements(self) -> None:
        """Generates a new random set of compositional elements"""
        pass

    def listCorrelatedWords(self) -> list:
        return self.correlatedWords

    def addSecondaryCompStrategy(self, secondaryCompStrategy) -> None:
        """Adds """
        self.secondaryCompStrategy = secondaryCompStrategy


class RuleOfThirds(CompositionalStrategy):

    def __init__(self) -> None:
       self.title = "RuleOfThirds"

class Symmetry(CompositionalStrategy):

    def __init__(self, title) -> None:
       self.title = "Symmetry"

class Framing(CompositionalStrategy):

    def __init__(self, title) -> None:
       self.title = "Framing"

class Radial(CompositionalStrategy):

    def __init__(self, title) -> None:
       self.title = "Radial"

class Wandering(CompositionalStrategy):

    def __init__(self, title) -> None:
       self.title = "Wandering"

class Diagonal(CompositionalStrategy):

    def __init__(self, title) -> None:
       self.title = "Diagonal"