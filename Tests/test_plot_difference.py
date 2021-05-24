import numpy as np

from Tests.plot_difference import plot_relative_difference


size = 30

### 1d ###
predata1d_x1 = np.random.normal(loc=0, scale=0.3, size=size) + 0.2
predata1d_x2 = np.random.normal(loc=0, scale=0.3, size=size) + 0.2
data1d_x1 = np.zeros(size)
data1d_x2 = np.zeros(size)

predata1d_x1 = np.square(predata1d_x1)
predata1d_x2 = np.square(predata1d_x2)
np.clip(a=predata1d_x1, a_min=0., a_max=1., out=data1d_x1)
np.clip(a=predata1d_x2, a_min=0., a_max=1., out=data1d_x2)
data1d_x1 = data1d_x1*100
data1d_x2 = data1d_x2*100

fig = plot_relative_difference(
    data1=data1d_x1,
    data2=data1d_x2,
    plt_figure_num="testfig",
    theme="dark_background"
)

fig.show()

### 2d ###
predata2d_x1 = [np.random.normal(
    loc=0, scale=0.3, size=size) + 0.2 for i in range(size)]
predata2d_x2 = [np.random.normal(
    loc=0, scale=0.3, size=size) + 0.2 for i in range(size)]
data2d_x1 = np.zeros((size, size))
data2d_x2 = np.zeros((size, size))

predata2d_x1 = np.square(predata2d_x1)
predata2d_x2 = np.square(predata2d_x2)
np.clip(a=predata2d_x1, a_min=0., a_max=1., out=data2d_x1)
np.clip(a=predata2d_x2, a_min=0., a_max=1., out=data2d_x2)
data2d_x1 = data2d_x1*100
data2d_x2 = data2d_x2*100

fig = plot_relative_difference(
    data1=data2d_x1,
    data2=data2d_x2,
    plt_figure_num="testfig",
    theme="dark_background"
)

fig.show()


input("Press Enter to exit...")
input("Press Enter to exit...")
input("Press Enter to exit...")
input("Press Enter to exit...")
