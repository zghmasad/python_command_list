import numpy

# Import matplotlib colour map
from pythonw.matplotlib import cm as colourmap
# Required for £D Projections
# Provide access to numpy functions


def line_graph():
    # Set up the data
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [0, 2, 6, 14, 30, 43, 75]
    # Set the axes headings
    pyplot.ylabel('Speed', fontsize=12)
    pyplot.xlabel('Time', fontsize=12)
    # Set the title
    pyplot.title("Speed v Time")
    # Plot and display the graph
    # Using blue circles for markers ('bo')
    # and a solid line ('-')
    pyplot.plot(x, y, 'bo-')
    '''
    b,g,r,c,m,y,k,w
    blue, green, red, cyan, magenta, yellow, black, white

    ‘.’ point marker
    ‘,’ pixel marker
    ‘o’ circle marker
    ‘v’ triangle_down marker
    ‘^’ triangle_up marker
    ‘ < ’ triangle_left marker
    ‘ > ’ triangle_right marker
    ‘s’ square marker
    ‘p’ pentagon marker
    ‘*’ star marker
    ‘h’ hexagon1 marker
    ‘ + ’ plus marker
    ‘x’ x marker
    ‘D’ diamond marker
    ‘-’ solid line style
    ‘–’ dashed line style
    ‘-.’ dash-dot line style
    ‘:’ dotted line style
    '''
    pyplot.show()


def scatter_graph():
    # Create data
    riding = ((17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
              (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4))
    swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
                (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
    sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
               (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))
    # Plot the data
    pyplot.scatter(x=riding[0], y=riding[1], c='red', marker='o',
                   label='riding')
    pyplot.scatter(x=swimming[0], y=swimming[1], c='green',
                   marker='^', label='swimming')
    pyplot.scatter(x=sailing[0], y=sailing[1], c='blue',
                   marker='*', label='sailing')
    # Configure graph
    pyplot.xlabel('Age')
    pyplot.ylabel('Hours')
    pyplot.title('Activities Scatter Graph')
    pyplot.legend()
    pyplot.show()
    # Display the chart

def scatter_line_graph():
    x = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
    y = (120, 115, 100, 112, 80, 85, 69, 65)
    # Generate the scatter plot
    pyplot.scatter(x, y)
    # Generate the trend line
    z = numpy.polyfit(x, y, 1)
    p = numpy.poly1d(z)
    pyplot.plot(x, p(x), 'r')
    # Display the figure
    pyplot.show()

def pie_graph():
    labels = ('Python', 'Java', 'Scala', 'C#')
    sizes = [45, 30, 15, 10]
    pyplot.pie(sizes,
               labels=labels,
               autopct='%1.f%%',
               counterclock=False,
               startangle=90)
    pyplot.show()

def pie_graph2():
    labels = ('Python', 'Java', 'Scala', 'C#')
    sizes = [45, 30, 15, 10]
    # only "explode" the 1st slice (i.e. 'Python')
    explode = (0.1, 0, 0, 0)
    pyplot.pie(sizes,
               explode=explode,
               labels=labels,
               autopct='%1.f%%',
               shadow=True,
               counterclock=False,
               startangle=90)
    pyplot.show()


def bar_graph():
    # Set up the data
    labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
    index = (1, 2, 3, 4, 5)  # provides locations on x axis
    sizes = [45, 10, 15, 30, 22]
    # Set up the bar chart
    pyplot.bar(index, sizes, tick_label=labels)
    # Configure the layout
    pyplot.ylabel('Usage')
    pyplot.xlabel('Programming Languages')
    # Display the chart
    pyplot.show()

def bar_horizontal_graph():
    # Set up the data
    labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
    index = (1, 2, 3, 4, 5)  # provides locations on x axis
    sizes = [45, 10, 15, 30, 22]
    # Set up the bar chart
    pyplot.barh(index, sizes, tick_label=labels)
    # Configure the layout
    pyplot.ylabel('Usage')
    pyplot.xlabel('Programming Languages')
    # Display the chart
    pyplot.show()

def bar_colored_graph():
    # Set up the data
    labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
    index = (1, 2, 3, 4, 5)  # provides locations on x axis
    sizes = [45, 10, 15, 30, 22]
    # Set up the bar chart
    pyplot.bar(index, sizes, tick_label=labels, color=('red',
                                                          'green', 'blue', 'yellow', 'orange'))
    # Configure the layout
    pyplot.ylabel('Usage')
    pyplot.xlabel('Programming Languages')
    # Display the chart
    pyplot.show()

def bar_stacked_graph():
    # Set up the data
    labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
    index = (1, 2, 3, 4, 5)
    web_usage = [20, 2, 5, 10, 14]
    data_science_usage = [15, 8, 5, 15, 2]
    games_usage = [10, 1, 5, 5, 4]
    # Set up the bar chart
    pyplot.bar(index, web_usage, tick_label=labels, label='web')
    pyplot.bar(index, data_science_usage, tick_label=labels,
               label='data science', bottom=web_usage)
    web_and_games_usage = [web_usage[i] + data_science_usage[i]
                           for i in range(0, len(web_usage))]
    pyplot.bar(index, games_usage, tick_label=labels,
               label='games', bottom=web_and_games_usage)
    # Configure the layout
    pyplot.ylabel('Usage')
    pyplot.xlabel('Programming Languages')
    pyplot.legend()
    # Display the chart
    pyplot.show()

def bar_grouped_graph():
    BAR_WIDTH = 0.35
    # set up grouped bar charts
    teama_results = (60, 75, 56, 62, 58)
    teamb_results = (55, 68, 80, 73, 55)
    # Set up the index for each bar
    index_teama = (1, 2, 3, 4, 5)
    index_teamb = [i + BAR_WIDTH for i in index_teama]
    # Determine the mid point for the ticks
    ticks = [i + BAR_WIDTH / 2 for i in index_teama]
    tick_labels = ('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5')
    # Plot the bar charts
    pyplot.bar(index_teama, teama_results, BAR_WIDTH, color='b',
               label='Team A')
    pyplot.bar(index_teamb, teamb_results, BAR_WIDTH, color='g',
               label='Team B')
    # Set up the graph
    pyplot.xlabel('Labs')
    pyplot.ylabel('Scores')
    pyplot.title('Scores by Lab')
    pyplot.xticks(ticks, tick_labels)
    pyplot.legend()
    # Display the graph
    pyplot.show()

def subplots():
    t = range(0, 20)
    s = range(30, 10, -1)
    # Set up the grid of subplots to be 2 by 2
    grid_size = '22'
    # Initialize a Figure
    figure = pyplot.figure()
    # Add first subplot
    position = grid_size + '1'
    print('Adding first subplot to position', position)
    axis1 = figure.add_subplot(position)
    axis1.set(title='subplot(2,2,1)')
    axis1.plot(t, s)
    # Add second subplot
    position = grid_size + '2'
    print('Adding second subplot to position', position)
    axis2 = figure.add_subplot(position)
    axis2.set(title='subplot(2,2,2)')
    axis2.plot(t, s, 'r-')
    # Add third subplot
    position = grid_size + '3'
    print('Adding third subplot to position', position)
    axis3 = figure.add_subplot(position)
    axis3.set(title='subplot(2,2,3)')
    axis3.plot(t, s, 'g-')
    # Add fourth subplot
    position = grid_size + '4'
    print('Adding fourth subplot to position', position)
    axis4 = figure.add_subplot(position)
    axis4.set(title='subplot(2,2,4)')
    axis4.plot(t, s, 'y-')
    # Display the chart
    pyplot.show()

def treeD_graph():
    # Make the data to be displayed
    x_values = numpy.arange(-6, 6, 0.3)
    y_values = numpy.arange(-6, 6, 0.3)
    # Generate coordinate matrices from coordinate vectors
    x_values, y_values = numpy.meshgrid(x_values, y_values)
    # Generate Z values as sin of x plus y values
    z_values = numpy.sin(x_values + y_values)
    # Obtain the figure object
    figure = pyplot.figure()
    # Get the axes object for the 3D graph
    axes = figure.gca(projection='3d')
    # Plot the surface.
    surf = axes.plot_surface(x_values,
                             y_values,
                             z_values,
                             cmap=colourmap.coolwarm)
    # Add a color bar which maps values to colors.
    figure.colorbar(surf)
    # Add labels to the graph
    pyplot.title("3D Graph")
    axes.set_ylabel('y values', fontsize=8)
    axes.set_xlabel('x values', fontsize=8)
    axes.set_zlabel('z values', fontsize=8)
    # Display the graph
    pyplot.show()

#line_graph()
#scatter_graph()
#scatter_line_graph()
#pie_graph()
#pie_graph2()
#bar_graph()
#bar_horizontal_graph()
#bar_colored_graph()
#bar_stacked_graph()
#bar_grouped_graph()
#subplots()
treeD_graph()