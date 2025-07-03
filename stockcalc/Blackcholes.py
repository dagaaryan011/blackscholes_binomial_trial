# S  = Current stock price (spot price)
# K  = Strike price (agreed future price in option contract)
# T  = Time to maturity (in years)
# r  = Risk-free interest rate (annual, as a decimal),guaranteed amount of interest that can be earned without any risk of losing your money.
# v  = Volatility (standard deviation of stock returns)
# N(d) = Cumulative probability from standard normal distribution
# e  =  2.718

# d1 = [ ln(S/K) + (r + σ²/2) * T ] / (σ * sqrt(T))
# d2 = d1 - σ * sqrt(T)

# Call Price = S * N(d1) - K * e^(-r*T) * N(d2)
# Put Price  = K * e^(-r*T) * N(-d2) - S * N(-d1)


from math import log, sqrt, exp
from scipy.stats import norm

def calculate_option_price(S, K, T, r, v, option_type='call'):
    d1 = (log(S / K) + (r + 0.5 * v** 2) * T) / (v * sqrt(T))
    d2 = d1 - v * sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'.")

    return price
