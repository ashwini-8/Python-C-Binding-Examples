from dataclasses import dataclass
import myStructure

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

def PrintStructure(p):
   return(myStructure.lib.cfunction(p))

if __name__ =="__main__":
    p = Point(1.5,2.5,3.5)
    print(p)
    PrintStructure(p.x)
