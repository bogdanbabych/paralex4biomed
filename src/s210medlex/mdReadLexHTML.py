'''
Created on 5 Jul 2019

@author: bogdan
'''


import os, sys, re


class clReadLexHTML(object):
    '''
    reading html file with the medical lexicon
    to be used in a workflow operating on a directory
    '''


    def __init__(self, SInput):
        '''
        Constructor
        '''
        self.LTerms = []
        for SLine in SInput:
            m = re.search('<h3 class="item_text "><a href=(.+?)>(.+?)</a></h3>', SLine)
            
            # search for:
            # <h3 class="item_text "><a href=/dictionary/83398>alaryngeal speech</a></h3>
            if m:
                # SUrl, STerm = m.groups()
                # sys.stdout.write('%(STerm)s\t%(SUrl)s\n' % locals())
                self.LTerms.append(m.groups())
                
    def getData(self):
        return self.LTerms
        
        
if __name__ == '__main__':
    FInput = open(sys.argv[1], 'rU')
    OReadLexHTML = clReadLexHTML(FInput)
    for SUrl, STerm in OReadLexHTML.LTerms:
        sys.stdout.write('%(STerm)s\thttps://www.medilexicon.com%(SUrl)s\n' % locals())
        # sys.stdout.write('https://www.medilexicon.com%(SUrl)s\n' % locals())
        
        '''
        if called will be used for each file in the directory
        '''
        

    

        