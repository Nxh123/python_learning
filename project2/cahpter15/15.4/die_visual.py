from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline
#创建骰子
die = Die()
results = []
#掷骰子并将结果储存在列表中
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果',
                   xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
