graphrepresentation.py
========================================

![Graphrepresentation](https://drive.google.com/uc?export=view&id=1TeQr9qhkSF2e0-GjjaK6OD4ohQHT5Bin)

File python dapat dilihat di [*Python file*](https://github.com/n0tavaliduser/Kecerdasan-Buatan/blob/main/Assignment-1/graphrepresentation.py)

Graf adalah struktur data populer yang diaplikasikan dalam pemrograman komputer. Graf referesentasi tidak sangat dibutuhkan jika kita memanfaatkan penyimpanan external, namun beberapa permasalahan komputasi yang membutuhkan referesentasi internal maka graf tidak dapat dihindari. 



Undirected Graph & Directed Graph
========================================

![](https://drive.google.com/uc?export=view&id=1zfU2rdxkpReowWY2GTChVZzlb0sb01s_
)

Graph (G) berisikan node/vertex (V) dan edge (E) maka G = {V, E}

Untuk membuat graph representation dengan Python dibutuhkan library tambahan (optional) yaitu.

* [numpy](https://numpy.org/)
* [tabulate](https://pypi.org/project/tabulate/)

Cara menginstall library dengan command prompt:

pastikan direktori sudah pada tempat dimana python diinstall, sebagai contoh C:\Python27>
```
pip install numpy
```

kemudian tabulate

```
pip install tabulate
```

Penggunaan pada kode python
========================================

```python
import numpy as np
from tabulate import tabulate
```

Masih panjang anjenk...

buat class object graphrepresentation

```python
class graphrepresentation(object):

    def __init__(self):
        self.nama = [] # bentuk data ["vertex ke-1", ..., "vertex ke-x"]
        self.relation = [] # bentuk data [["vertex ke-1, [{relation}]], [..., [{relation}], ["vertex ke-x", {relation}]]
```

Method setter nama

```python
    def setNama(self, nama):
        self.nama.append(nama)
        self.relation.append([])

        for i in range(len(self.nama)):
            while len(self.relation[i]) < len(self.nama):
                self.relation[i].append(0)
```

Method setter relasi

```python
    def setRelation(self, nama, teman):
        for i in range(len(self.nama)):
            for j in range(len(self.relation[i])):
                if self.nama[i] == nama and j == self.nama.index(teman):
                    self.relation[i][j] += 1
```

Method getter nama dan relasi

```python
    def getNama(self):
        return(self.nama)

    def getRelation(self):
        return(self.relation)
```