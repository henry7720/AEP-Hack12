import pandas
import plotly.express as plotly

data_file = pandas.read_csv('output.csv')

figure = plotly.histogram(data_file, x="High Energy", category_orders=dict(high_energy=["true", "false"]))
figure.write_html("output.html")