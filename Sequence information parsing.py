#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3 
# Name: Zarghaam Abbas
# Group Members: Andrew Matsiev, Rogelio Chavez, Samuel Hirsch, Anand Verna 


'''
This Program will Parse and display the FASTQ formated input string

For Example if this is Input:
@EAS139:136:FC706VJ:2:2104:15343:197393

Output:
Instrument = EAS139
Run ID = 136
Flow Cell ID = FC706VJ
Flow Cell Lane = 2
Tile Number = 2104
X-coord = 15343
Y-coord = 197393
'''

class FastqString (str):
    ''' This is a string Class whose object is created to Parse the given FASTQ foramtted line'''
    def parse(self):
        ''' This is the Function where the line is parsed and printed'''
        #we will split the string on bases of : and store in a list
        parseList=self.split(':')
        #This first element of the list will be @Instrument therefore we will remove @ and store in the list
        parseList[0]=parseList[0].replace('@','')
        #we will return the list, that do not have @ and is seprated on bases of :
        return parseList
        
        
        
def main():
    ''' This Function create an object of FastString class and call parse function to Parse the FASATQ formatted line'''
    #Taking input of the FASTQ formatted line
    fastq=input('FASTQ LINE:')
    #creating the object
    thisSeq=FastqString(fastq)
    #The parse will return a list of all the component i.e instrument at 0th position, therefore, WE will stroe all in different variables
    intrument,runId,flowId,flowLane,tile,xCord,yCord=thisSeq.parse()
    #WE will print the above Variable here
    print('Instrument = {}\nRun ID = {}'.format(intrument,runId))
    print('Flow Cell ID = {}\nFlow Cell Lane = {}'.format(flowId,flowLane))
    print('Tile Number= {}'.format(tile))
    print('X-coord = {}\nY-coord = {}'.format(xCord,yCord))

main()

