import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def temperature_graph(history, dark_mode=False):

    bg = "#1a1a2e" if dark_mode else "#ffffff"
    fg = "#ffffff" if dark_mode else "#111111"
    grid_color = "#333355" if dark_mode else "#e0e0e0"
    line_color = "#ff6b6b" if dark_mode else "#e63946"

    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    ax.plot(
        range(len(history)),
        history,
        color=line_color,
        marker="o",
        markersize=6,
        linewidth=2.5,
        markerfacecolor=line_color,
    )

    ax.fill_between(range(len(history)), history, min(history) - 1,
                    color=line_color, alpha=0.1)

    ax.set_title("Live Temperature Monitoring", color=fg, fontsize=14, pad=12)
    ax.set_ylabel("Temperature (°C)", color=fg)
    ax.set_xlabel("Readings", color=fg)
    ax.tick_params(colors=fg)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.0f°C"))

    for spine in ax.spines.values():
        spine.set_edgecolor(grid_color)

    ax.grid(True, color=grid_color, linestyle="--", linewidth=0.7)

    fig.tight_layout()
    return fig


def humidity_graph(history, dark_mode=False):

    bg = "#1a1a2e" if dark_mode else "#ffffff"
    fg = "#ffffff" if dark_mode else "#111111"
    grid_color = "#333355" if dark_mode else "#e0e0e0"
    line_color = "#4cc9f0" if dark_mode else "#0077b6"

    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    ax.plot(
        range(len(history)),
        history,
        color=line_color,
        marker="o",
        markersize=6,
        linewidth=2.5,
        markerfacecolor=line_color,
    )

    ax.fill_between(range(len(history)), history, min(history) - 1,
                    color=line_color, alpha=0.1)

    ax.set_title("Live Humidity Monitoring", color=fg, fontsize=14, pad=12)
    ax.set_ylabel("Humidity (%)", color=fg)
    ax.set_xlabel("Readings", color=fg)
    ax.tick_params(colors=fg)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.0f%%"))

    for spine in ax.spines.values():
        spine.set_edgecolor(grid_color)

    ax.grid(True, color=grid_color, linestyle="--", linewidth=0.7)

    fig.tight_layout()
    return fig