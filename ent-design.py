import numpy as np
import matplotlib.pyplot as plt
import math
#Homogenous Network of Sensor Nodes


#Notes from Miguel A Labrador
#Geometric Random Graph, G = (V,E,r)
#r => open ball and only nodes within the open ball are neighbours 
#Initiate graph network;
class SensorNode:
     def __init__(self, coords, trans_radius, E_init, nodes):
          self.coords = coords  
          self.x, self.y = coords[0], coords[1] #Coords is a tuple for immobile nodes
          self.E_0 = E_init
          #self.deg = deg
          self.trans_radius = trans_radius
          self.tag = None
          self.nodes = nodes          #Neighbours is most likely a tuple of tuples or list of tuples etc etc.
          self.neighbours = self.getNeighbours(self, trans_radius, coords, nodes)
          self.costs = self.nodeCost(self,coords, neighbours)
     def energyModel(self, dist, nodes, E_0, n_bits = 1, E_circ = 50, E_amp = 100):         #E_circ is the energy used by the Electronic circuit to send 1-bit, it is a constant
          #Compute residual energy
          E_tx = n_bits*E_circ + E_amp*n_bits*(dist**2)                                #We assume E_tx = E_tx for homogenous network measured in nJ
          E_res = E_0 - E_tx
          return E_res
      
     def getNeighbours(self, trans_radius, coords, nodes):
         self.neighbours = []
     	  for node in nodes:
     	       dist = math.sqrt((self.x - node[0])**2 + (self.y - node[1])**2)
     	       if dist <= trans_radius:
     	          self.neighbours.append(node)
     	  return self.neighbours
     def nodeCost(self, coords, neighbours):
     #Useful for computing the cost between node and neighbours
          self.costs = [] 
          for node in self.neighbours:
               node_cost = 1 				#Obtain formula and compute the cost for each node
               self.costs.append(node_cost)
          return self.costs
     def metric(self, neighbours, E_res, coords):
          #Compute metric of node for every neighbour node
          self.metrics = []
          for node in neighbours:
               metric_cost = pass #Get the real matrics formula and compute the metrics of a node
               self.metrics.append(metric_cost)
          return self.metrics
node1 = SensorNode((10,5),100,[(10,20),(40,10),(10,13),(5,2),(7,10)])
node2 = SensorNode((7,5),9,[(89,0),(10,17),(15,13),(25,12),(70,1)])
node3 = SensorNode((13,5),18,[(10,20),(15,10),(77,45),(6,2),(2,8)])

class Link(SensorNode):

     def __init__(self, neighbours,E_res,coords):
          self.costs = []
          self.metrics = []
          for node in neighbours:
          	self.metrics = node.metric(neighbours, E_res, coords)
          
     def linkCost(node, neighbours):     
     	  for i in range(len(self.metrics)):
               self.costs.append(node.nodeCost(coord1) + self.metrics[i])
          return self.costs
          #Since link cost is a constant, no need to define a model for changing the cost
     #def linkCost(coord1,coord2):
          
     #def costModel(x,y):

     #threshold distance, r cost from energy model
     #Model link for each node
class SinkNode():
	def __init__(self):
		self.E = 100000 #Very large amount of energy --- Sink
		self.coord = 
		self.
class Network(Link, SensorNode):
     def __init__(self,E_th = 10):
          self.E_th = E_th
          self.graph = [node1,node2,node3]
     def main(self,E_th,graph):
          for node in graph:
               node.tag = 'NN'
               if node.energyModel(node.neighbours,node.E_0)<= E_th or node.energyModel(node.neighbours,node.E_0) == 0: 
                    node.tag = 'NCH' #Note eligible for cluster head election
               elif node.energyModel(node.neighbours,node.E_0) == 0:
                    node.tag = 'DN'
               else:
                    continue
               return node.tag







#Adapted from https://github.com/python-engineer/MLfromscratch/blob/master/mlfromscratch/kmeans.py
#Algorithm 1 --- KMeans Clustering
class KMeans:
    def __init__(self, K=5, max_iters=100, plot_steps=False):
        self.K = K
        self.max_iters = max_iters
        self.plot_steps = plot_steps

        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.K)]
        # the centers (mean feature vector) for each cluster
        self.centroids = []

    def predict(self, X):
        self.X = X
        self.n_samples, self.n_features = X.shape
        
        # initialize 
        #random_sample_idxs = SensorNode()
        random_sample_idxs = np.random.choice(self.n_samples, self.K, replace=False)
        self.centroids = [self.X[idx] for idx in random_sample_idxs]

        # Optimize clusters
        for _ in range(self.max_iters):
            # Assign samples to closest centroids (create clusters)
            self.clusters = self._create_clusters(self.centroids)
            
            if self.plot_steps:
                self.plot()

            # Calculate new centroids from the clusters
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)
            
            # check if clusters have changed
            if self._is_converged(centroids_old, self.centroids):
                break

            if self.plot_steps:
                self.plot()

        # Classify samples as the index of their clusters
        return self._get_cluster_labels(self.clusters)


    def _get_cluster_labels(self, clusters):
        # each sample will get the label of the cluster it was assigned to
        labels = np.empty(self.n_samples)

        for cluster_idx, cluster in enumerate(clusters):
            for sample_index in cluster:
                labels[sample_index] = cluster_idx
        return labels

    def _create_clusters(self, centroids):
        # Assign the samples to the closest centroids to create clusters
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self._closest_centroid(sample, centroids)
            clusters[centroid_idx].append(idx)
        return clusters

    def _closest_centroid(self, sample, centroids):
        # distance of the current sample to each centroid
        distances = [self.euclidean_distance(sample, point) for point in centroids]
        closest_index = np.argmin(distances)
        return closest_index

    def _get_centroids(self, clusters):
        # assign mean value of clusters to centroids
        centroids = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroids[cluster_idx] = cluster_mean
        return centroids

    def _is_converged(self, centroids_old, centroids):
        # distances between each old and new centroids, fol all centroids
        distances = [self.euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)]
        return sum(distances) == 0
    def euclidean_distance(self,x1,x2):
        return np.sqrt(np.sum((x1-x2)**2))
    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker="x", color="black", linewidth=2)

        plt.show()



#Perform topology discovery i.e r the node to node distance, initial energy of nodes E0, cost of transmission between nodes E_cost;
#Set constrains such as threshold transmission distance r_th and threshold cost, E_th of Nodes, if E_cost > E_th, set entry = 0;
#Calculate desired network lifetime t_d
#Initiate adjacency matrix with E_cost as entries --- Note: we may need to include r in case several nodes die and E_cost becomes a bad reference;
#Set model for energy decrease
#Set model for cost re-calculation
#Create model for Flagging dead sensor nodes and preventing
#Set parameters and model for cluster formation and switching in rounds: Threshold residual energy of nodes E_th,


#Algorithm 1 -- Base Case
#Perform Spectral clustering using adjacency matrix
#Initiate Cluster formation rounds
#Create a real-time display of node behaviour for NN --> CN (coined by me) --> DN
#Choose cluster heads
#Update adjacency matrix and re-calculate the eigen vector space
#End rounds once all nodes are dead
#Analyze network lifetime
#Analyze and optimize energy use


#Algorithm 2
#Perform stronly connected components and form clusters from it
#Here: clusters are formed based on distance from each node
#Adjacency matrix entries will be computed based on relative distance of other nodes before clusters are formed from the strongly connected components
#Initiate rounds and after the degree of a certain number of nodes reduce to a certain value (percentage value of nodes in component), perform a different component analysis and form different clusters
#
