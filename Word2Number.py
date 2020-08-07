#! /usr/bin/env python
# coding=utf-8
# created from Wayne, for copy or reedit plz inform me

import pandas as pd
from collections import namedtuple
import os

#name = "new_Apple"
startPosition = 80
count = 80
items = []


def delblankline(infile, outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()


def reorganize(name):
    getData = open('Crawldata/' + name, "r").read().strip(' ').replace(" ", "\n").replace("", "")
    f = open("ProcessingData/Reorganize.txt", "w")
    f.write(getData)
    f.close()


def SetDataFrame(file, dataName):
    Item = namedtuple('Wordcount', 'Word Number')
    global count
    global datalist
    dataName = dataName.strip('.txt')

    with open(file) as f:
        for line in f:
            DeleteWordBlank = line.rstrip('\n')
            judge, TextToDigit = check(DeleteWordBlank, count)
            StrToInter = str(TextToDigit)

            if(judge == True):
                count = count + 1
                items.append(Item(DeleteWordBlank, count))

            with open("Output/" + dataName + "_conv" + ".txt", "a") as q:
                q.write(StrToInter)
                q.write(",")

    df = pd.DataFrame.from_records(items, columns=['Word', 'Number'])  # print result
    print(df)


def check(DeleteWordBlank, count):
    gate = False  # no_pass
    setcount = count
    items_count = count - startPosition
    if(items_count == 0):
        gate = True
        TextToDigit = startPosition + 1
        return gate, TextToDigit  # pass
    else:
        for times in range(len(items)):
            if(DeleteWordBlank == items[times][0]):  # check whether appear or not
                # print('[{:13}]'.format(items[times][0]) + '--existence !') #optional! print for user
                TextToDigit = int(items[times][1])
                gate = False  # no_pass
                break  # if bingo, stop waste time on loop
            else:  # if item are first data, give it an new number
                gate = True  # pass
                TextToDigit = setcount + 1
        return gate, TextToDigit


if __name__ == '__main__':

    os.getcwd()
    path = 'Crawldata'
    os.listdir(path)
    datalist = []

    for i in os.listdir(path):  # setting for take data automatically
        if os.path.splitext(i)[1] == '.txt':
            datalist.append(i)
    print("All files:", datalist)

    for data in datalist:  # 迴圈跑所有txt
        print(data)
        reorganize(data)
        delblankline("ProcessingData/Reorganize.txt", "ProcessingData/RemoveBlank.txt")
        SetDataFrame("ProcessingData/RemoveBlank.txt", data)

    # for data in datalist:
