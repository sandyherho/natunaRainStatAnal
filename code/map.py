'''
PyGMT Mapping script

Sandy Herho <herho@umd.edu>
2021/05/24
'''
import pygmt
grid = pygmt.datasets.load_earth_relief(resolution="03s", region=[105, 110, 1.2, 7.3])

x = 108.39000
y = 3.91206

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="M15c", frame="a", cmap="geo")
fig.colorbar(frame=["a1000", "x+lElevation", "y+lm"])
fig.plot(x, y, style="i0.5c", color="red")
fig.show()
