from skimage import measure
#from plotly.tools import FigureFactory as FF
import plotly.figure_factory as FF
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as plt


def make_mesh(image, threshold=-300, step_size=1):

    print("Transposing surface")
    p = image.transpose(2, 1, 0)

    print("Calculating surface")
    verts, faces, norm, val = measure.marching_cubes_lewiner(
        p, step_size=1, allow_degenerate=True)
    return verts, faces


def plotly_3d(verts, faces):
    x, y, z = zip(*verts)

    print("Drawing")

    # Make the colormap single color since the axes are positional not intensity.
    # colormap=['rgb(255,105,180)','rgb(255,255,51)','rgb(0,191,255)']
    colormap = ['rgb(183, 110, 121)', 'rgb(183, 110, 121)']

    fig = FF.create_trisurf(x=x,
                            y=y,
                            z=z,
                            plot_edges=False,
                            show_colorbar=False,
                            colormap=colormap,
                            simplices=faces,
                            backgroundcolor='rgb(204, 204, 204)',
                            title="Visualización Interactiva del Pulmón")
    iplot(fig)


def plt_3d(verts, faces):
    print("Drawing")
    x, y, z = zip(*verts)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], linewidths=0.05, alpha=1)
    face_color = [1, 1, 0.9]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, max(x))
    ax.set_ylim(0, max(y))
    ax.set_zlim(0, max(z))
    ax.set_facecolor((0.7, 0.7, 0.7))
    plt.show()
