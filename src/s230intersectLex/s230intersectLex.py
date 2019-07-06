'''
Created on 5 Jul 2019

@author: bogdan
'''



import sys, os, re
from collections import defaultdict



class clIntersectLex(object):
    '''
    intersects fields of two dictionaries
    '''


    def __init__(self, FDict1, FDict2):
        '''
        Constructor
        '''
        
        DField1 = self.readField(FDict1, 0)
        DField2 = self.readField(FDict2, 1)
        
        self.Intersect = []
        self.Diff1 = []
        self.Diff2 = []
        for el in DField1.keys():
            if el in DField2.keys():
                self.Intersect.append(el)
            else:
                self.Diff1.append(el)
                
        for el in DField2.keys():
            if el in DField1.keys():
                continue
            else:
                self.Diff2.append(el)
                
        
        
    def readField(self, FInput, Col = 0):
        DField = defaultdict(int)
        for SFields in FInput:
            SFields = SFields.rstrip()
            try:
                LFields = re.split('\t', SFields)
                SField = LFields[Col]
                DField[SField] += 1
            except:
                continue
            
        return DField
    
    
    def printData(self):
        FOIntersect = open('s230intersectLex-intersect.txt', 'w')
        FODiff1 = open('s230intersectLex-diff1.txt', 'w')
        FODiff2 = open('s230intersectLex-diff2.txt', 'w')
        
        for el in self.Intersect:
            FOIntersect.write('%(el)s\n' % locals())

        for el in self.Diff1:
            FODiff1.write('%(el)s\n'  % locals())
        
        for el in self.Diff2:
            FODiff2.write('%(el)s\n'  % locals())
            
            
        
        


if __name__ == '__main__':
    SDict1Ling = sys.argv[1]
    SDict2Ling = sys.argv[2]
    
    FDict1 = open(SDict1Ling, 'rU')
    FDict2 = open(SDict2Ling, 'rU')
    
    
    OIntersectLex = clIntersectLex(FDict1, FDict2)
    OIntersectLex.printData()
    
    
    
        