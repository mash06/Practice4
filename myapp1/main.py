import csv


def readfromfile(pair):
        res = open("files/file.csv")
        onstring = res.read().split("\n")[:-1]
        dictionary = dict()

        for item in onstring:
            key = item.split(" ")[0]
            value = item.split(" ")[1:]
            dictionary[key] = value
        return dictionary[pair]

