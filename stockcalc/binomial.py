# binomial_tree.py

from math import exp

def calculate_binomial_option_price(S, K, T, r, sigma, steps=100, option_type='call'):
    dt = T / steps
    u = exp(sigma * (dt) ** 0.5)
    d = 1 / u
    p = (exp(r * dt) - d) / (u - d)

    # Calculate asset prices at maturity
    prices = [S * (u ** j) * (d ** (steps - j)) for j in range(steps + 1)]

    # Calculate option values at maturity
    if option_type == 'call':
        values = [max(0, price - K) for price in prices]
    else:  # put
        values = [max(0, K - price) for price in prices]

    # Backward induction
    for i in range(steps - 1, -1, -1):
        values = [exp(-r * dt) * (p * values[j + 1] + (1 - p) * values[j]) for j in range(i + 1)]

    return values[0]
