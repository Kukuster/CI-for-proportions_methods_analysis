from typing import Literal, Tuple, Union
from collections import defaultdict

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

from CI_methods_analyser.data_functions import float_to_str


def normalize_data(data: np.ndarray) -> np.ndarray:
    return (data - np.min(data))/(np.max(data) - np.min(data))


def normalize_data1_and_data2(data1: np.ndarray, data2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    x_min = np.min([np.min(data1), np.min(data2)])
    x_max = np.max([np.max(data1), np.max(data2)])

    return ( (data1 - x_min)/(x_max - x_min),
             (data2 - x_min)/(x_max - x_min) )


def relative_diff(data1: np.ndarray, data2: np.ndarray) -> np.ndarray:
    """diff is symmetric with respect to `data1` and `data2`"""
    data1, data2 = np.array(np.longdouble(np.array(data1))), np.array(np.longdouble(np.array(data2)))
    # data1, data2 = normalize_data1_and_data2(data1, data2)

    with np.errstate(divide='ignore', invalid='ignore'):
        """
        This formula always works, except when x1 = 1 and x2 = 1 => gives nan
        And for the right reason. This 2-variate function has infinite amount of limit values,
        depending on from what side to approach this point (x1, x2) = (1, 1)

        One important property that this function has:
        f(0.9, 0.99) = f(0.92, 0.992) = f(0.95, 0.995) = f(0.99, 0.999) = f(0.999, 0.9999) = 0.(81)
        You get the idea?
        f(0.0, 0.1) = f(0.9, 0.91)  = f(0.99, 0.991)  = 0.05263158
        f(0.5, 0.8) = f(0.95, 0.98) = f(0.995, 0.998) = 0.42857143
        f(0.1, 0.9) = f(0.91, 0.99) = f(0.991, 0.999) = 0.8

        Add any number of '9's after zero,
        This is how it's "relative" difference.

        check out this function:
          f(x, y) = |x-y|/(2-(x+y))

        It is indeterminate at the point (1,1)
        """
        diff = abs(data1-data2)/(2 - (data1+data2))  # a value from 0 to 1
        diff = np.array(diff)
    np.clip(a=diff, a_min=0., a_max=1., out=diff) # just make sure values are from 0 to 1
    diff = np.nan_to_num(diff, nan=0)  # decided to set f(1,1) = 0
    return np.round(diff, 8)


def plot_relative_difference(
    data1: np.ndarray,
    data2: np.ndarray,
    plt_figure_num: Union[str, int],
    theme: Literal["dark_background", "default"] = "dark_background",
    title: str = "Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}",
):
    if data1.shape != data2.shape:
        raise ValueError("data1 and data2 have to have the same shape")

    shape = data1.shape

    data1, data2 = normalize_data1_and_data2(np.longdouble(data1), np.longdouble(data2))
    diff = relative_diff(data1, data2)

    plt.style.use(theme)

    # for 1d arrays
    if len(shape) == 1:

        print(f"mean relative difference (data shape {list(shape)}) = {float_to_str(np.mean(diff), 5)}")

        fig = plt.figure(plt_figure_num)

        points = [
            {"point": 0.0005, "color": "blue"},
            {"point": 0.005,  "color": "green"},
            {"point": 0.025,  "color": "yellow"},
            {"point": 0.5,    "color": "red"},
        ]

        plt.yscale("log", base=10)
        plt.plot([i for i in range (0,len(diff))], diff,
                 color='white' if theme == "dark_background" else 'black',
                 marker=',', linestyle='solid', zorder=5)
        for point in points:
            plt.axhline(point["point"], color=point["color"],   linestyle=":", zorder=0)

        x1, x2, y1, y2 = plt.axis()
        plt.axis((x1, x2, 1e-5, 1))


        title = title.format(**defaultdict(str, 
            dim = len(shape),
            shape = f"{shape[0]}",
            avg = float_to_str(np.mean(diff), 5),
            max = float_to_str(np.max(diff), 5),
        ))
        plt.title(title, fontsize="large", fontweight="bold")
        plt.xlabel("data points")
        plt.ylabel("relative difference")

        size = fig.get_size_inches()
        fig.set_size_inches(size[0], size[1]*1.25)

        return fig


    # for 2d arrays
    elif len(shape) == 2:

        print(f"mean relative difference (data shape {list(shape)}) = {float_to_str(np.mean(diff), 5)}")

        nodes = [0, 0.001, 0.01, 0.05, 1]
        colors = ["black", "blue", "green", "yellow", "red"]
        cmap = LinearSegmentedColormap.from_list("", list(zip(nodes, colors)))
        cmap.set_under("black")

        # plt.matshow(data)
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(str(plt_figure_num))

        top = 1
        im = ax.imshow(diff, cmap=cmap, norm=Normalize(0, top, True))

        title = title.format(**defaultdict(str, 
            dim = len(shape),
            shape = f"{shape[0]}, {shape[1]}",
            avg = float_to_str(np.mean(diff), 5),
            max = float_to_str(np.max(diff), 5),
        ))
        ax.set_title(title)
        fig.colorbar(im, extend="max")

        size = fig.get_size_inches()
        fig.set_size_inches(size[0]*1.25, size[1]*1.25)

        return fig

    else:
        raise ValueError("this function is not supported for data of shape other than 1d or 2d")

