# Here I want to define a universal function for Binomial Tree that takes some inputs
import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import norm

def BinomialTree(nodes, S, K, T, sigma, rate, div, style, type):

    """This function compute the price of an option using the Binomial Tree Model. The inputs required are the\
        usual ones, note that "style" and "type" require string values. For "style" choose between "american" and "european"\
        while for "style" insert "call" or "put"."""
    
    delta_time = T/nodes
    u = np.exp(sigma*np.sqrt(delta_time))
    d = 1/u
    q_rn = (1/(u-d))*(np.exp((rate-div)*delta_time)-d)
    qq = 1-q_rn
    dis = np.exp(-rate*delta_time)
    row = nodes+1
    col = nodes+1
    lattice = np.zeros((row, col))
    payoff = np.zeros((row, col))
    price = np.zeros((row, col))
    lattice[0, 0] = S

    if style == "european" and type == "call":
        
        for i in range(1, row, 1):
            for j in range(1, col, 1):
                lattice[0, j] = S*(u**j)
                lattice[i, j] = lattice[i-1, j-1]*d

        for i in range(0, row, 1):
            for j in range(0, col, 1):
                if lattice[i, j] == 0:
                    payoff[i, j] = 0
                else:
                    payoff[i, j] = np.maximum(lattice[i, j]-K, 0)

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if lattice[i, j] == 0:
                    price[i, j] = 0
                else:
                    if j == col-1:
                        price[i, j] = payoff[i, j]
                    else:
                        price[i, j] = dis*(q_rn*price[i, j+1]+qq*price[i+1, j+1])
            
    elif style == "european" and type == "put":
        
        for i in range(1, row, 1):
            for j in range(1, col, 1):
                lattice[0, j] = S*(u**j)
                lattice[i, j] = lattice[i-1, j-1]*d

        for i in range(0, row, 1):
            for j in range(0, col, 1):
                if lattice[i, j] == 0:
                    payoff[i, j] = 0
                else:
                    payoff[i, j] = np.maximum(K-lattice[i, j], 0)

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if lattice[i, j] == 0:
                    price[i, j] = 0
                else:
                    if j == col-1:
                        price[i, j] = payoff[i, j]
                    else:
                        price[i, j] = dis*(q_rn*price[i, j+1]+qq*price[i+1, j+1])

    elif style == "american" and type == "call":

        for i in range(1, row, 1):
            for j in range(1, col, 1):
                lattice[0, j] = S*(u**j)
                lattice[i, j] = lattice[i-1, j-1]*d

        for i in range(0, row, 1):
            for j in range(0, col, 1):
                if lattice[i, j] == 0:
                    payoff[i, j] = 0
                else:
                    payoff[i, j] = np.maximum(lattice[i, j]-K, 0)

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if lattice[i, j] == 0:
                    price[i, j] = 0
                else:
                    if j == col-1:
                        price[i, j] = payoff[i, j]
                    else:
                        price[i, j] = max(payoff[i, j], dis*(q_rn*price[i, j+1]+qq*price[i+1, j+1]))

    elif style == "american" and type == "put":

        for i in range(1, row, 1):
            for j in range(1, col, 1):
                lattice[0, j] = S*(u**j)
                lattice[i, j] = lattice[i-1, j-1]*d

        for i in range(0, row, 1):
            for j in range(0, col, 1):
                if lattice[i, j] == 0:
                    payoff[i, j] = 0
                else:
                    payoff[i, j] = np.maximum(K-lattice[i, j], 0)

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if lattice[i, j] == 0:
                    price[i, j] = 0
                else:
                    if j == col-1:
                        price[i, j] = payoff[i, j]
                    else:
                        price[i, j] = max(payoff[i, j], dis*(q_rn*price[i, j+1]+qq*price[i+1, j+1]))
                    
    Option_Price = price[0,0]
    
    return Option_Price


def BlackScholes(S, K, T, sigma, rate, div, style, type):

    """This function implements the Black-Scholes Model for european options. Inputs required are the usual ones\
       For "style" choose exclusively "european" while for "style" insert "call" or "put". Note that these are string arguments."""

    d1 = (np.log(S/K)+(rate-div+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*(np.sqrt(T)))

    if style == "european" and type == "call":
        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)
        c0 = (S*np.exp(-div*T)*N_d1)-(K*np.exp(-rate*T)*N_d2)
        # The formulas for the greeks are derived in the pdf report file
        D = np.exp(-div*T)*N_d1
        V = K*np.exp(-rate*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi))
        R = T*K*np.exp(-rate*T)*N_d2/100
        TH = ((div*S*np.exp(-div*T)*N_d1) - (rate*K*np.exp(-rate*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-rate*T)*np.exp((-d2**2)/2))))/365
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-div*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi)

    elif style == "european" and type == "put":
        N_d1 = norm.cdf(-d1)
        N_d2 = norm.cdf(-d2)
        c0 = (K*np.exp(-rate*T)*N_d2)-(S*np.exp(-div*T)*N_d1)
        D = -np.exp(-div*T)*N_d1
        V = K*np.exp(-rate*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi))
        R = -T*K*np.exp(-rate*T)*N_d2/100
        TH = (-(div*S*np.exp(-div*T)*N_d1) + (rate*K*np.exp(-rate*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-rate*T)*np.exp((-d2**2)/2))))/365
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-div*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi)
    
    Option_Price = c0

    return Option_Price



