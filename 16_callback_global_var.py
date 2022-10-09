import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)

df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
	dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@app.callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
#     # 以下使用全局变量的代码会运行中失败
#     global df
# 	df = df[df['score'] == value]
# 	return len(df)

    # 创建一个新的本地局部变量
	filtered_df = df[df['score'] == value]
	return len(filtered_df)

if __name__ == '__main__':
    app.run_server(debug=True)