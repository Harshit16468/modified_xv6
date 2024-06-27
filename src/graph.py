import matplotlib.pyplot as plt

# Dictionary to store data for each PID
pid_data = {}

# Read data from the file
with open('new.txt', 'r') as file:
    for line in file:
        pid, priority, ticks,l = map(int, line.strip().split())
        if pid not in pid_data:
            pid_data[pid] = {'priority': [], 'ticks': []}
        pid_data[pid]['priority'].append(priority)
        pid_data[pid]['ticks'].append(ticks)

# Plot the data for each PID
for pid, data in pid_data.items():
    plt.plot( data['ticks'], data['priority'],label=f'PID {pid}')

# Customize the plot
plt.xlabel('Ticks')
plt.ylabel('Priority')
plt.legend()
plt.title('Priority vs. Ticks for each PID')
plt.grid(True)

# Show the plot
plt.savefig("graph.png")
plt.close()
