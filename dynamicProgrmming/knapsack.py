# -*- using:utf-8 -*-
"""
Use dynamic programming to calculate knapsack problem
Solution test = 44
Solution 1 = 2493893
Solution 2 =
"""

import sys

def ReadData(fileName):
    print('\n - READ DATA -')
    print('   from '+fileName)
    file = open(fileName)

    index = 0
    capacity = 0
    numItem = 0
    items = {}
    for line in file:
        if index == 0:
            capacity = int(line.split()[0])
            numItem = int(line.split()[1])
        else:
            value = int(line.split()[0])
            weight = int(line.split()[1])
            items[index] = [value,weight]
        sys.stdout.write('\r   Read Line '+str(index))
        sys.stdout.flush()
        index += 1
    file.close()
    print('')
    assert numItem == len(items), 'Item size not machted...'
    return items, capacity


#############################################################

class Knapsack:
    def __init__(self, capacity, items):
        print('\n - Initialize Knapsack problem -')
        self.__capacity = capacity
        self.__items = items
        self.__valueMat = None
        self.__choiceMat = None
        self.__pickedItems = None
        self.__maxWeight = None
        print(' - FINISH -')

    def packing(self, debug=False):
        """
        forward: choose the item into pack with maximum values
        """
        print('\n - PACKING -')
        # initialize the matrix       
        valueMat = []       # record the value in the pack
        choiceMat = []     # record the choice of items in the pack
        for i in range(len(self.__items)+1):
            valueMat.append([0]*(self.__capacity+1))
            choiceMat.append([0]*(self.__capacity+1))
            sys.stdout.write('\r   Initialize '+str(i)+'/'+str(len(self.__items)))
            sys.stdout.flush()
        print('')
        print('   Matrix initialized')
        
        for i in range(1,(len(self.__items)+1)):
            for currentCap in range(self.__capacity+1):
                wi = self.__items[i][1]
                vi = self.__items[i][0]
                if currentCap < wi:
                    valueMat[i][currentCap] = valueMat[i-1][currentCap]
                else:
                    chooseCurrent = valueMat[i-1][currentCap-wi]+vi
                    notChooseCurrent = valueMat[i-1][currentCap]
                    if chooseCurrent > notChooseCurrent:
                        valueMat[i][currentCap] = chooseCurrent
                        choiceMat[i][currentCap] = 1
                    else:
                        valueMat[i][currentCap] = notChooseCurrent
                sys.stdout.write('\r   Processed Item '+str(i)+' W='+str(currentCap))
                sys.stdout.flush()
        print('')
        
        if debug:
            print('\n - VALUE MATRIX -')
            for line in valueMat:
                print(line)

            print('\n - CHOICE MATRIX -')
            for line in choiceMat:
                print(line)

        self.__valueMat = valueMat
        self.__choiceMat = choiceMat
        print(' - FINISH -')

    def picking(self, debug = False):
        """
        backward: trace back the choice matrix to find which items are chosen
        """
        print('\n - PICKING -')
        itemIndex = len(self.__items)
        currentCap = self.__capacity
        pickedItems = []
        if debug:
            print('\n - Picking items -')
        while itemIndex >= 1 and currentCap > 0:
            if debug:
                print('  Checking Item ' + str(itemIndex) + ' with remaining capacity ' + str(currentCap))
            if self.__choiceMat[itemIndex][currentCap] == 1:
                if debug:
                    print('  Picked\n')
                pickedItems.append(itemIndex)
                currentCap -= self.__items[itemIndex][1]
                itemIndex -= 1
            else:
                if debug:
                    print('  Not picked\n')
                itemIndex -= 1
            if debug:
                input('')

        self.__pickedItems = pickedItems
        print(' - FINISH -')

    
    def pickedItems(self):
        return self.__pickedItems

    def showResult(self,fullList = False):
        print('\n - SOLUTION - ')
        sumWeight = 0
        for itemIndex in self.__pickedItems:
            sumWeight += self.__items[itemIndex][1]
            if fullList:
                print('   Item '+str(itemIndex)+ \
                    ' (V='+str(self.__items[itemIndex][0])+ \
                    ',W='+str(self.__items[itemIndex][1])+')')
        if fullList:
            print('\n')
        self.__maxWeight = sumWeight
        print('   Weight = ' + str(self.__maxWeight)+' <= '+str(self.__capacity))
        print('   Maximum value = ' + str(self.__valueMat[-1][-1]))
        print('')

#############################################################

if __name__ == '__main__':
    items, capacity = ReadData('knapsack2.txt')

    pack = Knapsack(capacity, items)
    pack.packing()
    pack.picking()
    pack.showResult()

