##############################
# Gianmarco Mulazzani - 2021 #
##############################

## This Python script contains three functions that can be easily used to price plain vanilla options and compute greeks.
## The idea to separate functions in a different script is related to the fact that the user could use them in any other script.
## Recall that they can be imported using "from Options import BinomialTree, GreeksBinomial, BlackScholes".

# *For a theoretical discussion about these functions refer to the pdf report.* #

# Import the relevant libraries (make sure that they are installed in your computer).
import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import norm

# FIRST FUNCTION: BinomialTree --> It implements a pricing algorithm based on a binomial tree.

def BinomialTree(nodes, S, K, T, sigma, rate, div, style, type):

    """This function computes the price of an option using the Binomial Tree Model. The inputs required are the\
        usual ones, note that "style" and "type" require string values. For "style" choose between "american" and "european"\
        while for "style" insert "call" or "put"."""
    
    # Relevant parameters are defined below, based on Cox, Ross, Rubistein formulae.
    delta_time = T/nodes
    u = np.exp(sigma*np.sqrt(delta_time))
    d = 1/u
    q_rn = (1/(u-d))*(np.exp((rate-div)*delta_time)-d) # This is the risk neutral probability Q of going up. That is Q(up)=q_rn
    qq = 1-q_rn
    dis = np.exp(-rate*delta_time) # This is the discount factor 

    # These two are auxiliary variables used in the script.
    row = nodes+1
    col = nodes+1

    # Three zero matrices are initialized.
    lattice = np.zeros((row, col))
    payoff = np.zeros((row, col))
    price = np.zeros((row, col))
    lattice[0, 0] = S

    # To make the code more understandable, all four cases have been clearly specified: European Call, European Put
    # and American Call and American Put Options.
    if style == "european" and type == "call":
        
        # FIRST for LOOP: it implements the lattice dynamics of the underlying security.
        for i in range(1, row, 1):
            for j in range(1, col, 1):
                lattice[0, j] = S*(u**j)
                lattice[i, j] = lattice[i-1, j-1]*d

        # SECOND for LOOP: this computes the payoff at each node.
        for i in range(0, row, 1):
            for j in range(0, col, 1):
                if lattice[i, j] == 0:
                    payoff[i, j] = 0
                else:
                    payoff[i, j] = np.maximum(lattice[i, j]-K, 0)

        # THIRD for LOOP: the price is computed at each node using backward recursion formulae.
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

    # Outputs desired are clearly specified and computed below.
    Option_Price = price[0,0]
    D = (price[0,1]-price[1,1])/(lattice[0,1]-lattice[1,1]) # Delta 
    Delta_1_up = (price[0,2]-price[1,2])/(lattice[0,2]-lattice[1,2]) # Delta computed at t=1 in case of an upward movement.
    Delta_1_down = (price[1,2]-price[2,2])/(lattice[1,2]-lattice[2,2]) # Delta computed at t=1 in case of a downward movement.
    G = (Delta_1_up-Delta_1_down)/(lattice[0,1]-lattice[1,1]) # Gamma
    TH = (price[1,2]-price[0,0])/(2*delta_time*365) # Theta

    # The function is instructed to return a tuple containing the results that can be easily retrieved by the user.    
    return {'Option_Price':Option_Price, 'Delta':D, 'Theta':TH, 'Gamma':G}

# SECOND FUNCTION: GreeksBinomial --> This function computes Rho and Vega using the Binomial Tree Model. The separation from the previous formula is
# needed since BinomialTree function must be used in order to perform the calculations.

def GreeksBinomial(nodes, S, K, T, sigma, rate, div, style, type):

    """This function is used to compute Rho and Vega using the Binomial Tree. The function is strictly connected to the other function of\
        this library which is called BinomialTree."""

    # Note that central difference estimators are implemented below.

    result_delta_sigma_up = BinomialTree(nodes, S, K, T, sigma+0.01, rate, div, style, type)
    result_delta_sigma_down = BinomialTree(nodes, S, K, T, sigma-0.01, rate, div, style, type)

    V = (result_delta_sigma_up['Option_Price']-result_delta_sigma_down['Option_Price'])/(0.02*100) # Vega

    result_delta_rate_up = BinomialTree(nodes, S, K, T, sigma, rate+0.01, div, style, type)
    result_delta_rate_down = BinomialTree(nodes, S, K, T, sigma, rate-0.01, div, style, type)

    R = (result_delta_rate_up['Option_Price']-result_delta_rate_down['Option_Price'])/(0.02*100) # Rho

    # The function is instructed to return a tuple containing the results that can be easily retrieved by the user.
    return {'Vega':V, 'Rho':R}

# THIRD FUNCTION: BlackScholes --> This function implements the standard Black-Scholes model and computes the related greeks.
# Two separate cases are considered: European Call and European Put Options.

def BlackScholes(S, K, T, sigma, rate, div, style, type):

    """This function implements the Black-Scholes Model for european options. Inputs required are the usual ones\
       For "style" choose exclusively "european" while for "style" insert "call" or "put". Note that these are string arguments."""

    # Define a priori the two parameters that enter the formulas below: d_1 and d_2.
    d1 = (np.log(S/K)+(rate-div+(sigma**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*(np.sqrt(T)))

    if style == "european" and type == "call":

        N_d1 = norm.cdf(d1)
        N_d2 = norm.cdf(d2)
        price = (S*np.exp(-div*T)*N_d1)-(K*np.exp(-rate*T)*N_d2)
        D = np.exp(-div*T)*N_d1 # Delta
        V = K*np.exp(-rate*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi)) # Vega
        R = T*K*np.exp(-rate*T)*N_d2/100 # Rho
        TH = ((div*S*np.exp(-div*T)*N_d1) - (rate*K*np.exp(-rate*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-rate*T)*np.exp((-d2**2)/2))))/365 # Theta
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-div*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi) # Gamma

    elif style == "european" and type == "put":

        N_d1 = norm.cdf(-d1)
        N_d2 = norm.cdf(-d2)
        price = (K*np.exp(-rate*T)*N_d2)-(S*np.exp(-div*T)*N_d1)
        D = -np.exp(-div*T)*N_d1 # Delta
        V = K*np.exp(-rate*T)*np.sqrt(T)*np.exp((-d2**2)/2)/(100*np.sqrt(2*np.pi)) # Vega
        R = -T*K*np.exp(-rate*T)*N_d2/100 # Rho
        TH = (-(div*S*np.exp(-div*T)*N_d1) + (rate*K*np.exp(-rate*T)*N_d2) - (((sigma/np.sqrt(T*8*np.pi))*K*np.exp(-rate*T)*np.exp((-d2**2)/2))))/365 # Theta
        G = (1/(sigma*S*np.sqrt(T)))*np.exp(-div*T)*np.exp((-d1**2)/2)/np.sqrt(2*np.pi) # Gamma
    
    # The function is instructed to return a tuple containing the results that can be easily retrieved by the user.
    return {'Option_Price':price, 'Delta':D, 'Vega':V, 'Rho':R, 'Theta':TH, 'Gamma':G}



