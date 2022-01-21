import plotly.figure_factory as pf
import pandas as p
import csv

data = p.read_csv("data.csv")

plot = pf.create_distplot( [data["Avg Rating"].tolist()] , ["Average Rating"]  )

plot.show()
