import lib
import math
import time
import numpy as np
import matplotlib.pyplot as plt

# Define the function to test
def test_function(x):
    # Более сложная тестовая функция, включающая экспоненциальные и тригонометрические операции
    return math.exp(-x) * math.sin(x) * math.cos(x) * math.log(x + 1)

def derivative_test_function(x):
    return (math.cos(x)**2 * math.log(1 + x) / math.exp(x) +
            math.cos(x) * math.sin(x) / (math.exp(x) * (1 + x)) -
            math.cos(x) * math.log(1 + x) * math.sin(x) / math.exp(x) -
            math.log(1 + x) * math.sin(x)**2 / math.exp(x))

# Generate a range of h values
h_values = np.logspace(-1, -10, 1000)

# Initialize dictionaries to store times and accuracies
times = {method: [] for method in ['forward', 'central', 'higher_order']}
accuracies = {method: [] for method in ['forward', 'central', 'higher_order']}
efficiencies = {method: [] for method in ['forward', 'central', 'higher_order']}

# Test each method
for h in h_values:
    for method_name, method in [('forward', lib.forward_difference), 
                                ('central', lib.central_difference), 
                                ('higher_order', lib.higher_order_method)]:
        
        x = math.pi / 4
        start_time = time.time()
        how_many_iter = pow(10,4)
        for _ in range(how_many_iter):
            derivative = method(test_function, x, h)
        elapsed_time = time.time() - start_time
        times[method_name].append(elapsed_time)

        # Calculate accuracy as the absolute error from the true derivative
        true_derivative = derivative_test_function(x)
        accuracy = abs(derivative - true_derivative)
        accuracies[method_name].append(accuracy)

        # Calculate efficiency as accuracy per unit time
        efficiency =  elapsed_time/accuracy if elapsed_time > 0 else float('inf')
        efficiencies[method_name].append(efficiency)

# Plotting
fig, axes = plt.subplots(3, 3, figsize=(18, 12))  # 3x3 subplots

# Plot each method's time, accuracy, and efficiency
for i, method in enumerate(['forward', 'central', 'higher_order']):
    axes[i, 0].plot(h_values, times[method], label=f'{method} time')
    axes[i, 1].plot(h_values, accuracies[method], label=f'{method} accuracy')
    axes[i, 2].plot(h_values, efficiencies[method], label=f'{method} efficiency')

    # Set scales and labels
    for j in range(3):
        axes[i, j].set_xscale('log')
        axes[i, j].set_yscale('log')
        axes[i, j].set_xlabel('h')
        axes[i, j].legend()

    axes[i, 0].set_ylabel('Time (s)')
    axes[i, 1].set_ylabel('Accuracy')
    axes[i, 2].set_ylabel('Efficiency (Time/Accuracy)')

plt.tight_layout()
plt.show()
