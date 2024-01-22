#!/usr/bin/env python3
class Rational(object):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.rat_frac = num_1/num_2
    
    def __add__(self, obj2):
        counter = 1
        denom_1 = []
        denom_2 = []
        while True:
            num1 = (self.num_2 * counter)
            num2 = (obj2.num_2 * counter)
            denom_1.append(num1)
            denom_2.append(num2)
            if num1 in denom_2 or num2 in denom_1:
                break
            counter += 1
        common_denom = 0
        for i in denom_1:
            if i in denom_2:
                common_denom = i
        numerator = (self.num_1 * (common_denom/self.num_2)) + (obj2.num_1 * (common_denom/obj2.num_2))
        return Rational(int(numerator), common_denom)
        
    
    def __sub__(self, obj2):
        counter = 1
        denom_1 = []
        denom_2 = []
        while True:
            num1 = (self.num_2 * counter)
            num2 = (obj2.num_2 * counter)
            denom_1.append(num1)
            denom_2.append(num2)
            if num1 in denom_2 or num2 in denom_1:
                break
            counter += 1
        common_denom = 0
        for i in denom_1:
            if i in denom_2:
                common_denom = i
        numerator = (self.num_1 * (common_denom/self.num_2)) - (obj2.num_1 * (common_denom/obj2.num_2))
        return Rational(int(numerator), common_denom)
        
    
    def __mul__(self, obj2):
        return Rational((self.num_1 * obj2.num_1), (self.num_2 * obj2.num_2))
    
    def __truediv__(self, obj2):
        return Rational((self.num_1 * obj2.num_2), (self.num_2 * obj2.num_1))
    
    def __eq__(self, obj2):
        return (self.num_1 / self.num_2) ==( obj2.num_1 / obj2.num_2)
    
    def __gt__(self, obj2):
        return (self.num_1 / self.num_2) > (obj2.num_1 / obj2.num_2)
    
    def __lt__(self, obj2):
        return (self.num_1 / self.num_2) < (obj2.num_1 / obj2.num_2)
    
    def __str__(self):
        return f'{self.num_1}/{self.num_2}'
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
