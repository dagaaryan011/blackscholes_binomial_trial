

def plgraph(S, K, option_price):
    stock_prices = np.linspace(0, 2*S, 100)
    payoff = np.maximum(stock_prices - K, 0) - option_price

    fig, ax = plt.subplots()

    # Set background colors
    fig.patch.set_facecolor("#000000")  # Outer figure background
    ax.set_facecolor('#000000')         # Inside plot area background

    # Plot green for profit
    ax.plot(stock_prices[payoff >= 0], payoff[payoff >= 0], color='green')

    # Plot red for loss
    ax.plot(stock_prices[payoff < 0], payoff[payoff < 0], color='red')

    # Reference lines
    ax.axhline(0, color='white', linewidth=0.5)
    ax.axvline(K, color='blue', linestyle='--')

    # ✅ Set white axes and labels
    ax.tick_params(axis='both', colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')

    # ✅ Dynamic y-axis limits
    margin = 0.1
    y_min = payoff.min()
    y_max = payoff.max()
    y_range = y_max - y_min
    ax.set_ylim(y_min - margin * y_range, y_max + margin * y_range)

    # Remove title/labels if not needed
    ax.set_xlabel("Stock Price at Expiry", color='white')
    ax.set_ylabel("Profit / Loss", color='white')

    st.pyplot(fig)

 plgraph(S, C, price)
plgraph(S, C, price)
 plgraph(S2, K2, price2)
plgraph(S2, K2, price2)