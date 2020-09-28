#!/usr/bin/env python3

#Homogenous Network of Sensor Nodes

#Initiate graph;
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

