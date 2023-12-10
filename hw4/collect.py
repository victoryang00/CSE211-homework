import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 22,
        "axes.labelsize": 22,
        "axes.titlesize": 22,
        "xtick.labelsize": 22,
        "ytick.labelsize": 22,
        "legend.fontsize": 22,
    }
)

# Creating a clustered bar chart for the provided data

# Data for the clustered bar chart
default_configs = ["M3Max Metal", "M3Max CPU", "Alderlake CPU", "4090 CUDA"]
default_throughput = [3711.20, 473.08, 280.73, 12584.47]
bert_performance = [72.1661376953125, 153.1397819519043, 135.153040885925, 62.1795]
bert1_performance = [72.1661376953125, 153.1397819519043, 135.153040885925, 33.83706092834473]
import matplotlib.pyplot as plt
import numpy as np

# Assuming default_configs, default_throughput, bert_performance are defined
default_positions = np.arange(len(default_configs))
bar_width = 0.8

# Creating the first plot for TVM GEMM
fig1, ax1 = plt.subplots(figsize=(12, 10))
ax1.bar(
    default_positions,
    default_throughput,
    width=bar_width,
    label="TVM GEMM",
    color="#8ecfc9",
)

# Labels and ticks for the first plot
ax1.set_ylabel("GFLOPS")
ax1.set_xticks(default_positions)
ax1.set_xticklabels(default_configs)

# Data labels for the first plot
for pos, val in zip(default_positions, default_throughput):
    ax1.text(pos, val, f"{val}", ha="center", va="bottom")

# Grid for the first plot
ax1.grid(True)
ax1.legend()

# Creating the second plot for TVM Bert
fig2, ax2 = plt.subplots(figsize=(12, 10))
ax2.bar(
    default_positions,
    bert_performance,
    width=bar_width,
    label="TVM Bert",
    color="#ffbe7a",
)

# Labels and ticks for the second plot
ax2.set_ylabel("Latency (ms)")
ax2.set_xticks(default_positions)
ax2.set_xticklabels(default_configs)

# Data labels for the second plot
for pos, val in zip(default_positions, bert_performance):
    ax2.text(pos, val, f"{val}", ha="center", va="bottom")

# Grid for the second plot
ax2.grid(True)
ax2.legend()

# Layout adjustments and saving the figures
plt.tight_layout()
fig1.savefig("tvm_gemm.pdf")
fig2.savefig("tvm_bert.pdf")

# Display the plots
plt.show()