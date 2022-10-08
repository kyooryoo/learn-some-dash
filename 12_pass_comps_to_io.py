from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

my_input = dcc.Input(value='initial value', type='text')

app.layout = html.Div([
    html.H1("Using components for input/output without providing IDs"),
    html.P("Check source code for the two ways of creating components."),
    html.Div([
        "Input: ",
        # my_input is defined before getting used
        my_input
    ]),
    html.Br(),
    # my_output is defined and getting used at the same time
    my_output := html.Div()
])


@callback(
    Output(my_output, component_property='children'),
    Input(my_input, component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
