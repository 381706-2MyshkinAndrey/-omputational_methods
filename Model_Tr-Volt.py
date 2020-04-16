import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

#Model Lotky-Volterra
def Fx_der(x, y, a, c):
    value = float((a - c * y) * x)
    return value

def Fy_der(x, y, b, d):
    value = float((-b + d * x) * y)
    return value

#Runge Kutta 4th order
def Runge_Kutt_4th(x0,y0,n,h):
    x.append(x0)
    y.append(y0)
    H = 0.
    i = 0
    yt = 0
    xt = 0
    while(H < n):
        k1_y = h * Fy_der(x[i], y[i], b, d)
        
        kx = x[i] + h / 2
        y1 = y[i] + k1_y / 2
        k2_y = h * Fy_der(kx, y1, b, d)
        
        y1 = y[i] + k2_y / 2
        k3_y = h * Fy_der(kx, y1, b, d)
        
        kx = kx + h / 2
        y1 = y[i] + k3_y
        k4_y = h * Fy_der(kx, y1, b, d)
        
        yt = y[i] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        y.append(yt)

        k1_x = h * Fx_der(x[i], y[i], a, c)
        
        kx = x[i] + h / 2
        y1 = y[i] + k1_x / 2
        k2_x = h * Fx_der(kx, y1, a, c)
        
        y1 = y[i] + k2_x / 2
        k3_x = h * Fx_der(kx, y1, a, c)
        
        kx = kx + h / 2
        y1 = y[i] + k3_x
        k4_x = h * Fx_der(kx, y1, a, c)
        
        xt = x[i] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        x.append(xt)
        H+=h
        i+=1

#draw graph_axes
def addGraphPhase(graph_axes, x, y):   
     graph_axes.plot(x, y)
     plt.draw()

if __name__ == '__main__':
    x = list()
    y = list()
    plt.style.use('seaborn-ticks')
    plt.rcParams['figure.facecolor'] = '#d3c1d6'
    plt.rcParams['axes.facecolor'] = '#f0f0f0'

    #Event handler for the Add button (Method start)
    def onButtonAddClicked(event):
        global graph_axes, x, y
        global a, c  #F(x)
        global b, d  #F(y)
        global x0, y0, n, h
        # x - популяция жертв, y - популяция хищников
        # a - рождаемость жертв с - убийство жертв
        # b - воспроизводство хищников 
        # d - убыль жищников
        Runge_Kutt_4th(x0,y0,n,h)
        addGraphPhase(graph_axes, x, y)
        x = []
        y = []

    #Event handler for the Clear button
    def onButtonClearClicked(event):
        global graph_axes 
        graph_axes.clear()
        graph_axes.grid()
        plt.draw()

    #Event handler for entering text
    def submitA(text):
        global a
        try:
            a = float(text)
        except ValueError:        
            print("Вы пытаетесь ввести не число")
            
    def submitC(text):
        global c
        try:
            c = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitH(text):
        global h
        try:
            h = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitX0(text):
        global x0
        try:
            x0 = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitY0(text):
        global y0
        try:
            y0 = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitN(text):
        global n
        try:
            n = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitB(text):
        global b
        try:
            b = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
                        
    def submitD(text):
        global d
        try:
            d = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    #Create graph
    fig, graph_axes = plt.subplots()
    graph_axes.grid()
    graph_axes.set_title('Model Trays - Volterra')
    fig.subplots_adjust(left=0.06, right=0.80, top=0.95, bottom=0.23)

    #Create add button
    axes_button_add = plt.axes([0.55, 0.01, 0.4, 0.075])
    button_add = Button(axes_button_add, 'Добавить новый график', hovercolor = '#f0f0f0')
    button_add.on_clicked(onButtonAddClicked)

    #Create clear buttin
    axes_button_clear = plt.axes([0.05, 0.01, 0.4, 0.075])
    button_clear = Button(axes_button_clear, 'Очистить график',hovercolor = '#f0f0f0')
    button_clear.on_clicked(onButtonClearClicked)

    #Create textbox
    axbox = plt.axes([0.88, 0.90, 0.10, 0.075])
    x0_box = TextBox(axbox, 'Задача \n Коши \n x0 =', initial="0.1", hovercolor = '#d9d9d9')
    x0 = 0.1
    x0_box.on_submit(submitX0)

    axbox = plt.axes([0.88, 0.80, 0.10, 0.075])
    y0_box = TextBox(axbox, 'y0 =', initial= "0.1", hovercolor = '#d9d9d9')
    y0 = 0.1
    y0_box.on_submit(submitY0)
    
    axbox = plt.axes([0.88, 0.50, 0.10, 0.075])
    n_box = TextBox(axbox, ' n =', initial="100", hovercolor = '#d9d9d9')
    n = 100.0
    n_box.on_submit(submitN)
    
    axbox = plt.axes([0.88, 0.65, 0.10, 0.075])
    h_box = TextBox(axbox, 'Шаг h =', initial="0.01", hovercolor = '#d9d9d9')
    h = 0.01
    h_box.on_submit(submitH)

    axbox = plt.axes([0.24, 0.10, 0.13, 0.075])
    a_box = TextBox(axbox, 'Коэффициенты  a =', initial= "0.1", hovercolor = '#d9d9d9')
    a = 0.1
    a_box.on_submit(submitA)

    axbox = plt.axes([0.43, 0.10, 0.13, 0.075])
    b_box = TextBox(axbox, 'b =', initial= "0.1", hovercolor = '#d9d9d9')
    b = 0.1
    b_box.on_submit(submitB)

    axbox = plt.axes([0.62, 0.10, 0.13, 0.075])
    c_box = TextBox(axbox, 'c =', initial= "0.5", hovercolor = '#d9d9d9')
    c = 0.5
    c_box.on_submit(submitC)

    axbox = plt.axes([0.82, 0.10, 0.13, 0.075])
    d_box = TextBox(axbox, 'd =', initial= "1", hovercolor = '#d9d9d9')
    d = 1
    d_box.on_submit(submitD)

    plt.show()