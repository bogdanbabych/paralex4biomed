'''
Created on 5 Jul 2019

@author: bogdan
'''


import os, sys, re
import mdReadLexHTML

class clHtml2tsv(object):
    '''
    reads a directory with html files, and joins them into one list, then prints out a tsv
    '''


    def __init__(self, SDirInput):
        '''
        takes an input directory, processes files, returns a single list of terms + URLs
        '''
        self.LTUrlNTermsAll = []
        for root, dirs, files in os.walk(SDirInput):
            i = 0
            for SFile in files:
                i+= 1
                SPathFile = os.path.join(root,SFile)
                if re.search('\.html', SFile):
                    sys.stderr.write('%(i)d: %(SPathFile)s\n' % locals())
                    FInput = open(SPathFile, 'rU')
                    OReadLexHTML = mdReadLexHTML.clReadLexHTML(FInput)
                    self.LTUrlNTermsAll.extend(OReadLexHTML.getData())
                    
    def getData(self):
        return self.LTUrlNTermsAll
    
    def printData(self):
        for SUrl, STerm in self.LTUrlNTermsAll:
            sys.stdout.write('%(STerm)s\thttps://www.medilexicon.com%(SUrl)s\n' % locals())


        
        
if __name__ == '__main__':
    SDirInput = sys.argv[1]
    OHtml2tsv = clHtml2tsv(SDirInput)
    OHtml2tsv.printData()
    
