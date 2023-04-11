import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk



x_values = [1,2,3,4,5]
y_values = [1,4,6,7,9]

fig = plt.Figure()
ax = fig.add_subplot(111)
ax.plot(x_values, y_values, 'ro')
ax.plot(x_values, y_values)
ax.set_title('Graph')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

root = tk.Tk()
root.title('Graph')
root.iconbitmap('Polynomial_of_degree_three.svg.ico')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a label below the graph
eks = 'X - | '

#Сюда мы запишем значения оси-Y
igrik = 'Y - | '

for eksik in range(len(x_values)):

    #Значения оси-X
    eks+=f'{x_values[eksik]} | '

for ipchik in range(len(y_values)):

    #Значения оси-Y
    igrik+=f'{y_values[ipchik]} | '

label = tk.Label(root, text="Table of graph : ")
label.pack()
label = tk.Label(root, text=f"{eks}\n{igrik}")
label.pack(pady=40)

tk.mainloop()
