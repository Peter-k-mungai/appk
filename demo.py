import dash


from dash import  dcc, html

from flask import Flask


server = Flask(__name__)
app = dash.Dash(__name__, server=server)


app.layout = html.Div()


app.run_server(debug=True)