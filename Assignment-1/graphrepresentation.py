import numpy as np
from tabulate import tabulate

class graphrepresentation(object):

    def __init__(self):
        self.nama = []
        self.relation = []

    def setNama(self, nama):
        self.nama.append(nama)
        self.relation.append([])

        for i in range(len(self.nama)):
            while len(self.relation[i]) < len(self.nama):
                self.relation[i].append(0)
    
    def getNama(self):
        return(self.nama)

    def setRelation(self, nama, teman):
        for i in range(len(self.nama)):
            for j in range(len(self.relation[i])):
                if self.nama[i] == nama and j == self.nama.index(teman):
                    self.relation[i][j] += 1

    def getRelation(self):
        return(self.relation)