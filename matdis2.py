class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # Nomor dari vertices
        self.graph = []  # array default untuk menyimpan graph
 
    # fungsi untuk menambah edge ke graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # Fungsi untuk menemukan set dari element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # Fungsi untuk menggabungkan 2 set
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Perankingan Set
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # jika rank sama, maka gabungkan set
        # dan tingkatkan ranknya
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # fungsi utama kruskal
        # algorithm
    def KruskalMST(self):
 
        result = []  # untuk menyimpan hasilnya
         
        # indeks variabel untuk edges yang sudah di sort
        i = 0
         
        # indeks variabel untuk "result"
        e = 0
 
        # Step 1:  Sorting semua edges berdasarkan nilai weightnya  
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # membuat v subset
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        while e < self.V - 1:
 
            # Step 2: Ambil edge yang paling kecil dan otomatis meng increment i
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # jika edge yang dibaca tidak membuat cycle maka add edge ke result dan union set dari u dan v 
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # jika tidak maka tidak perlu di add ke result
 
        minimumCost = 0
        print ("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)

 
masuk = int(input("Masukkan jumlah Edge : "))
g = Graph(masuk)
print("Ketik Vertex Yang Terhubung : ")
for i in range(masuk):
    print("Edge ke-", i+1)
    u = int(input("Masukkan Vertex 1 : "))
    v = int(input("Masukkan Vertex 2 : "))
    w = int(input("Masukkan Bobot : "))
    g.addEdge(u, v, w)

g.KruskalMST()

