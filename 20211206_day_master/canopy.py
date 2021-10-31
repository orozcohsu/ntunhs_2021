import numpy as np
import math

class Canopy:
    #類別初始化
    dataset = []
    t1 = 0
    t2 = 0

    #建構子
    def __init__(self, dataset, t1, t2):
        self.dataset = dataset
        self.t1 = t1
        self.t2 = t2

    #計算歐式距離
    def euclidean_distance(self, point1, point2):
        return math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

    def get_index(self):
        return np.random.randint(len(self.dataset))

    #計算中心點
    def find_cluster_by_canopy(self):
        canopy_cluster = []
        while(len(self.dataset) != 0):
            center_set = []
            delete_set = []
            index = self.get_index()
            center_point = self.dataset[index]
            self.dataset = np.delete(self.dataset, index, 0)
            for i in range(len(self.dataset)):
                point = self.dataset[i]
                #調用計算
                distance = self.euclidean_distance(point, center_point)
                if distance < self.t1:
                    center_set.append(point)
                if distance < self.t2:
                    delete_set.append(i)
            self.dataset = np.delete(self.dataset, delete_set, 0)
            canopy_cluster.append((center_point, center_set))
            canopy_cluster = [cluster for cluster in canopy_cluster if len(cluster[1]) > 1]
        return canopy_cluster
