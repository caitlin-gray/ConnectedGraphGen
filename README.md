# ConnectedGraphGen
Code to generate connected random networks by MCMC methods.

Python code for generation of connected random graphs, specifically Spatially Embedded Random Networks (SERNs), such as the Waxman random graph.  The algorithm uses MCMC methods to sample from the distribution of interested conditioned on connectivity. See [1]

### Contents
The scripts are:
	ConnectedGraphGen.py:  Source python function for connected graph algorithm.
	CreateWaxman.py: Example of generating connected Waxman networks using the 					parameterisation in [2]

[1] C. Gray, L. Mitchell, M. Roughan, "Generating Connected Networks", Journal of Complex Networks, , cnz011, https://doi.org/10.1093/comnet/cnz011

[2]  M. Roughan, J. Tuke, and E. Parsonage, “Estimating the parameters of the Waxman random graph,” (2015), arXiv preprint: 1506.07974.  
