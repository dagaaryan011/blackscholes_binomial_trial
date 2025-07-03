# S       = Current stock price
# K       = Strike price , deal price at which stock can be bought in future
# T       = Time to expiry (in years)
# r       = Risk-free interest rate (annual)
# σ       = Volatility
# n       = Number of steps (time intervals in the tree)
# Δt      = T / n = Time per step

# u       = e^(σ * sqrt(Δt))         → Upward movement factor ->how much the stock price can go up in one time interval
# d       = 1 / u                    → Downward movement factor -> how much the stock price can fall in one time interval
# p       = (e^(r * Δt) - d) / (u - d)  → Risk-neutral probability -> future ki kamai , aaj ki kitni hogi 
# e^(-r*T) = Discount factor

# At each end node:
#   Call payoff = max(0, S_end - K)
#   Put payoff  = max(0, K - S_end)


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
    else:  
        values = [max(0, K - price) for price in prices]

    # Backward induction
    for i in range(steps - 1, -1, -1):
        values = [exp(-r * dt) * (p * values[j + 1] + (1 - p) * values[j]) for j in range(i + 1)]

    return values[0]
