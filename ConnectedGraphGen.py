import numpy as np
import networkx as nx
import random as rand


def ConnectedNetwork(G, position_x, position_y, probability, number_of_iterations, record_step=None):
    # Function to create connected networks, as described in CITATION HERE.
    # INPUTS:
    # G : Network of interested (connected by any means)

    # position_x : list of x coordinates
    # position_y : list of corresponding y coordinates
    # number_of_iterations : number of iterations required in the Metropolis-Hastings process
    # probability : function that has the relationship between distance and probability ( e.g. p= 0.1*exp(-4*d) in the Waxman)
    # record_step : integer, intervals at which recording is desired. E.g. record_step = 100, records average degree every 100 iterations

    # OUTPUTS:
    # G : connected network
    #
    # Note: this code saves the average degree if record_stepis not None

    n = len(G)

    if record_step:
        z_end = np.empty([int(number_of_iterations / record_step)])


    for it in range(number_of_iterations):

        # pick random numbers (nodes) and make sure they are different
        i = int(np.floor(rand.random() * n))
        j = int(np.floor(rand.random() * n))
        while i == j:
            j = int(np.floor(rand.random() * n))


        d = np.sqrt((position_x[i] - position_x[j]) ** 2 + (position_y[i] - position_y[j]) ** 2) # find distance between i and j
        print i, j, d
        p = probability(d)  # find the probability of link in original graph (input)

        if G.has_edge(i, j):
            G.remove_edge(i, j)  # remove the the edge

            if nx.is_connected(G):  # only accept change if new is connected

                alpha = min(1, (1 - p) / p)

                if rand.random() > alpha:
                    G.add_edge(i, j)  # if we do not accept the new network then go back to the previous
                #else:
                    #print 'remove'
            else:
                G.add_edge(i, j)

        else:                               # if edge doesn't exist
            alpha = min(1, p / (1 - p))
            if rand.random() < alpha:   # decide whether to accept the new network and add the edge
                G.add_edge(i, j)        # add edge if we accept
                #print 'add'



        if record_step:  # if recording save the average degree
            if it % record_step == 0:
                z_end[int(it / record_step)] = np.mean(G.degree().values())


    if record_step:
        np.save('filename_z_.npy', z_end)

    return G

