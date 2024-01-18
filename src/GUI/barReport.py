import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
class BarGramm(FigureCanvas):
    def __init__(self):
        super(BarGramm, self).__init__()
        self.figure = Figure()
        self.axes = self.figure.gca()
    def graph(self, objectA, index, values):
        self.axes.clear()
        self.axes.bar(index, values)
        self.axes.set_title("Расходы/Прибыль")
        self.figure.subplots_adjust(left=0.2, top=0.85)
        self.canvas = FigureCanvas(self.figure)
        objectA.updateCanvas(self.canvas)