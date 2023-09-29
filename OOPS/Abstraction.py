'''
Abstraction : Abstraction is a process to handling complexity by hiding unneccesary information from user.

--> For Abstraction you have to import ABC class and abstract class method

ABC:- Abstract Base Class

--> Abstraction will show only necessary information to user
'''

from abc import ABC

class RBI(ABC):
    def roi(self):
        pass

class BOI(RBI):
    def roi(self):
        return 6.5
    
class SBI(RBI):
    def roi(self):
        return 7.1
    
sbi = SBI()
boi = BOI()

print(boi.roi())
print(sbi.roi())