"""
This is an example to show how to build cross-GUI applications using
matplotlib event handling to interact with objects on the canvas

"""
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment
import matplotlib.pyplot as plt
from numpy.random import rand


class customPointPlacer:
	"""
	Key-bindings
	  'i' insert a point at the current position of the cursor,
	  'r' insert a point uniformly random in a unit square around the cursor,
	  hold down 'i' or 'r' to place points continuosly.
	"""
	def __init__(self, fig, ax, xs, ys):
		self.fig = fig;
		self.ax = ax;
		self.points, = self.ax.plot(xs, ys, 'o')
		self.xs = xs;
		self.ys = ys;

	def key_press_callback(self, event):
		'whenever a key is pressed'
		if not event.inaxes: return
		elif event.key=='i':
			self.xs.append(event.xdata);
			self.ys.append(event.ydata);
			self.points.set_xdata(self.xs);
			self.points.set_ydata(self.ys);
			self.fig.canvas.draw();
			self.fig.canvas.flush_events();
		elif event.key=='r':
			self.xs.append( (event.xdata+rand(1)-0.5)[0] );
			self.ys.append( (event.ydata+rand(1)-0.5)[0] );
			self.points.set_xdata(self.xs);
			self.points.set_ydata(self.ys);
			self.fig.canvas.draw();
			self.fig.canvas.flush_events();
