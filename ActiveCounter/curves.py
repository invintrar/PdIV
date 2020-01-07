"""
Created on Thu Nov 28 18:31:27 2019

@author: Gustavo
"""

import matplotlib

matplotlib.use('webagg')

import numpy as np
from scipy.special import binom

import matplotlib.pyplot as plt

from matplotlib.lines import Line2D

from  scipy.interpolate import interp1d
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment


class BezierBuilder(object):
    """Bézier curve interactive builder.

    """
    def __init__(self, control_polygon, ax_bernstein):
        """Constructor.

        Receives the initial control polygon of the curve.

        """
        self.control_polygon = control_polygon
        self.xp = list(control_polygon.get_xdata())
        self.yp = list(control_polygon.get_ydata())
        self.canvas = control_polygon.figure.canvas
        self.ax_main = control_polygon.axes
        self.ax_bernstein = ax_bernstein

        # Event handler for mouse clicking
        self.cid = self.canvas.mpl_connect('button_press_event', self)

        # Create Bézier curve
        line_bezier = Line2D([], [],
                             c=control_polygon.get_markeredgecolor())
        self.bezier_curve = self.ax_main.add_line(line_bezier)

    def __call__(self, event):
        # Ignore clicks outside axes
        if event.inaxes != self.control_polygon.axes:
            return

        # Add point
        self.xp.append(event.xdata)
        self.yp.append(event.ydata)
        self.control_polygon.set_data(self.xp, self.yp)

        # Rebuild Bézier curve and update canvas
        self.bezier_curve.set_data(*self._build_bezier())
        self._update_bernstein()
        self._update_bezier()

    def _build_bezier(self):
        x, y = Bezier(list(zip(self.xp, self.yp))).T
        return x, y

    def _update_bezier(self):
        self.canvas.draw()

    def _update_bernstein(self):
        N = len(self.xp) - 1
        t = np.linspace(0, 1, num=200)
        ax = self.ax_bernstein
        ax.clear()
        for kk in range(N + 1):
            ax.plot(t, Bernstein(N, kk)(t))
        ax.set_title("Bernstein basis, N = {}".format(N))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)


def Bernstein(n, k):
    """Bernstein polynomial.

    """
    coeff = binom(n, k)

    def _bpoly(x):
        return coeff * x ** k * (1 - x) ** (n - k)

    return _bpoly


def Bezier(points, num=200):
    """Build Bézier curve from points.

    """
    N = len(points)
    t = np.linspace(0, 1, num=num)
    curve = np.zeros((num, 2))
    for ii in range(N):
        curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])
    return curve

class PolygonInteractor(object):

    """
    A polygon editor.
    https://matplotlib.org/gallery/event_handling/poly_editor.html

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """

    showverts = True
    epsilon = 5  # max pixel distance to count as a vertex hit

    def __init__(self, ax, poly, visible=False):
        if poly.figure is None:
            raise RuntimeError('You must first add the polygon to a figure '
                               'or canvas before defining the interactor')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly
        self.poly.set_visible(visible)

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y, ls="",lw=5.0, c='r',
                           marker='o', markerfacecolor='r',animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # the active vert

        canvas.mpl_connect('draw_event', self.draw_callback)
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('key_press_event', self.key_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)
        canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)
        self.canvas = canvas

        x,y = self.interpolate()
        self.line2 = Line2D(x, y, animated=True)
        self.ax.add_line(self.line2)

    def interpolate(self):
        x, y = self.poly.xy[:].T
        i = np.arange(len(x))

        interp_i = np.linspace(0, i.max(), 100 * i.max())

        xi = interp1d(i, x, kind='cubic')(interp_i)  
        yi = interp1d(i, y, kind='cubic')(interp_i)

        return xi,yi

    def draw_callback(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.ax.draw_artist(self.line2)
        # do not need to blit here, this will fire before the screen is
        # updated

    def poly_changed(self, poly):
        'this method is called whenever the polygon object is called'
        # only copy the artist props to the line (except visibility)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # don't use the poly visibility state


    def get_ind_under_point(self, event):
        'get the index of the vertex under point if within epsilon tolerance'

        # display coords
        xy = np.asarray(self.poly.xy)
        xyt = self.poly.get_transform().transform(xy)
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.hypot(xt - event.x, yt - event.y)
        indseq, = np.nonzero(d == d.min())
        ind = indseq[0]

        if d[ind] >= self.epsilon:
            ind = None

        return ind

    def button_press_callback(self, event):
        'whenever a mouse button is pressed'
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        self._ind = self.get_ind_under_point(event)

    def button_release_callback(self, event):
        'whenever a mouse button is released'
        if not self.showverts:
            return
        if event.button != 1:
            return
        self._ind = None

    def key_press_callback(self, event):
        'whenever a key is pressed'
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        elif event.key == 'd':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.poly.xy = np.delete(self.poly.xy,
                                         ind, axis=0)
                self.line.set_data(zip(*self.poly.xy))
        elif event.key == 'i':
            xys = self.poly.get_transform().transform(self.poly.xy)
            p = event.x, event.y  # display coords
            for i in range(len(xys) - 1):
                s0 = xys[i]
                s1 = xys[i + 1]
                d = dist_point_to_segment(p, s0, s1)
                if d <= self.epsilon:
                    self.poly.xy = np.insert(
                        self.poly.xy, i+1,
                        [event.xdata, event.ydata],
                        axis=0)
                    self.line.set_data(zip(*self.poly.xy))
                    break
        if self.line.stale:
            self.canvas.draw_idle()

    def motion_notify_callback(self, event):
        'on mouse movement'
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        x, y = event.xdata, event.ydata

        self.poly.xy[self._ind] = x, y
        if self._ind == 0:
            self.poly.xy[-1] = x, y
        elif self._ind == len(self.poly.xy) - 1:
            self.poly.xy[0] = x, y
        self.line.set_data(zip(*self.poly.xy))

        x,y = self.interpolate()
        self.line2.set_data(x,y)

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.ax.draw_artist(self.line2)
        self.canvas.blit(self.ax.bbox)
