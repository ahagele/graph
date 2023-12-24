import sys
import pickle
import numpy as np
from io import StringIO
import sys
import os

try:
    from Tkinter import Tk
    from Tkinter.filedialog import askopenfilename
    from Tkinter import messagebox
except ImportError:
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from tkinter import messagebox

class logToFile:
    def __init__(self, baseName):
        self.baseName = baseName
        self.fileIndex = 1
        self.fileName = ""
        self.lines = []

    def startLog(self):
        self.fileName = 'cal{0}.txt'.format(self.fileIndex)

    def setHeader(self, line):
        self.header = 'Timestamp, HVRef,  HD755, HD1064,  HD532,  PWus,  Seed,   Amp,  ASE'

    def addLog(self, line):
        # add to list of strings
        self.lines.append(line)

    def endLog(self):
        # ToDo
        # format the output and write to file
        # convert to table with numpy.loadtxt()
        # reverse lines
        # filter required lines
        # save to file
        self.lines.reverse()
        allData = np.loadtxt(self.lines, delimiter=',', usecols = (1,11,12,13,14,16,18,19,20), dtype='str')
        print(allData)
        outName = '{0}_{1}.csv'.format(self.baseName, self.fileIndex)
        print(f'{outName = }')
        np.savetxt(outName, allData, delimiter=',', fmt='%s', header= self.header)
        self.lines = [] # clear data
        self.fileIndex += 1 # move to next out file index

class LVMdata:
    def __init__(self, fileName,
                begBlock = "PULSE HISTORY",
                endBlock = "FAULT COUNTS",
                colNums = [1,11,12,13,14,16,18,19,20],
                header = 'Timestamp, HVRef,  HD755, HD1064,  HD532,  PWus,  Seed,   Amp,  ASE'):
        self.begBlock = begBlock
        self.endBlock = endBlock
        self.colNums = colNums
        self.header = header
        self.fileName = fileName

    def proc(self):
        print(self.fileName, self.begBlock, self.endBlock, self.colNums, self.header, sep=" ")

if __name__ == '__main__':
    print('time for action')

    scriptpath = os.path.dirname(__file__)
    output = StringIO()
    try:
        LVMpath = pickle.load(open(scriptpath + '/cfg.p', 'rb'))
    except:
        print('no pickle found')
        LVMpath = '~/Downloads'

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    LVMfile = askopenfilename(initialdir =  LVMpath, \
        title='Select LVM file', \
        filetypes = (("LVM files","*.txt"),("all files","*.*")))

    if not LVMfile:
        sys.exit()

    # print(LVMfile)
    LVMpath, dummy = os.path.split(LVMfile)
    LVMbase, dummy = os.path.splitext(LVMfile)
    # print(LVMbase)
    pickle.dump(LVMpath, open(scriptpath + '/cfg.p', 'wb'))
    lvm = LVMdata(LVMfile)
    lvm.proc()
    sys.exit() # .??.

    with open(LVMfile) as infile:
        log = logToFile(LVMbase)
        subBlock = False
        copy = False
        for line in infile:
            if line.strip() == "PULSE HISTORY":
                copy = True
                # ToDo get col headers 2 lines down
                next(infile) # dummy, ignore
                log.setHeader(next(infile))
                continue
            elif line.strip() == "FAULT COUNTS":
                copy = False
                continue
            elif copy:
                if line.find('C,') > 0 and subBlock == False:
                    # start of block
                    subBlock = True
                    log.startLog()
                if line.find('C') < 0 and subBlock == True:
                    #end of block
                    subBlock = False
                    log.endLog()

                if subBlock == True:
                    log.addLog(line)

