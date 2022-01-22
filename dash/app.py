# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plot_lines
import time
import plotly.io as pio
from keywords import term_dict
from sewage import amphetamine_series, methamphetamine_series, MDMA_series, cocaine_series

# pio.templates.default = "none"


app = dash.Dash(__name__)

amphetamine_df = pd.DataFrame({'count': amphetamine_series.values, 'type': 'Amphetamine in sewage'}, index = amphetamine_series.index)
methamphetamine_df = pd.DataFrame({'count': methamphetamine_series.values, 'type': 'Methamphetamine in sewage'}, index = methamphetamine_series.index)
MDMA_df = pd.DataFrame({'count': MDMA_series.values, 'type': 'MDMA in sewage'}, index = MDMA_series.index)
cocaine_df = pd.DataFrame({'count': cocaine_series.values, 'type': 'Cocaine in sewage'}, index = cocaine_series.index)

extra_terms = []
local_term_dict = term_dict.copy()
relevant_cases = []


options = []
def get_options():
    global options
    for key in local_term_dict:
        globals()[key + "_mentions_results"] = []
        globals()[key + "_cases_results"] = []
        curr = {'label': key, 'value': key}
        if curr not in options:
            options.append(curr)
    return options
get_options()

app.layout = html.Div(children=[
    html.H1(children='Data Systems Project group F6'),

    html.Div(children='''
        Uncovering modus operandi.
    '''),

    dcc.Graph(
        id='sliding-graph'
    ),
    dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output")
        ),
    html.Div(children='''
        Rolling mean slider
    '''),
    dcc.Slider(
        id='rolling-mean-slider',
        min=1,
        max=25,
        value=6,
        step=1,
        marks={
        1: '1',
        5: '5',
        10: '10',
        15: '15',
        25: '25'
    },
    ),
    dcc.RadioItems(
        id='mentions_case_selector',
    options=[
        {'label': 'Mentions', 'value': 'mentions'},
        {'label': 'Cases', 'value': 'cases'}
    ],
    value='mentions'),
    html.Div(children='''
        Court mentions
    '''),
    dcc.Checklist(
        id="line-selector",
        options=get_options(),
        value=[]
    ),
    html.Div(children='''
        Sewage data
    '''),
    dcc.Checklist(
        id="sewage-selector",
        options=[{'label': 'Amphetamines', 'value': 'amphetamines'},
        {'label': 'Methamphetamines', 'value': 'methamphetamines'},
        {'label': 'MDMA', 'value': 'MDMA'},
        {'label': 'Cocaine', 'value': 'cocaine'}],
        value=[]
    ),
    html.Div(children='''
        Extra terms:
    '''),
    dcc.Input(
        id="input", type="text", placeholder="", debounce=True),
    html.Div(id="output"),
    dcc.Checklist(
        id="extra-terms-selector",
        options=[],
        value=[]
    ),
    html.Button('Delete extra terms', id='delete-extra-items', n_clicks_timestamp = 0),
    html.Div(children='''
        Find cases by mentions:
    '''),
    dcc.Input(
        id="specific-case-input", type="text", placeholder="", debounce=True),
        dcc.Input(
        id="specific-case-amount-input", type="number", placeholder="20", debounce=True),
    html.Div(
        children=[
            html.Ul(id='specific-case-output', children=[html.Li(i) for i in relevant_cases])
        ],
    )
])

@app.callback(
    Output('sliding-graph', 'figure'),
    Input('rolling-mean-slider', 'value'),
    Input('line-selector', 'value'),
    Input('sewage-selector', 'value'),
    Input('mentions_case_selector', 'value'),
    Input('extra-terms-selector', 'value'))
def update_figure(rolling_mean_value, line_selector, sewage_selector, mentions_case_selector, extra_terms):
    df = pd.DataFrame(columns = ['count', 'type'])
    for var in line_selector:
        if mentions_case_selector == 'mentions':
            if not (len(globals()[var + "_mentions_results"]) > 0):
                globals()[var + "_mentions_results"] = plot_lines.get_line(term_dict[var], 'mentions')
            globals()["monthly_" + var + "_mentions_results"] = globals()[var + "_mentions_results"].rolling(window=rolling_mean_value).mean()
            globals()["monthly_" + var + "_mentions_results"]['type'] = var
            df = df.append(globals()["monthly_" + var + "_mentions_results"])
        elif mentions_case_selector == 'cases':
            if not (len(globals()[var + "_cases_results"]) > 0):
                globals()[var + "_cases_results"] = plot_lines.get_line(term_dict[var], 'cases')
            globals()["monthly_" + var + "_cases_results"] = globals()[var + "_cases_results"].rolling(window=rolling_mean_value).mean()
            globals()["monthly_" + var + "_cases_results"]['type'] = var
            df = df.append(globals()["monthly_" + var + "_cases_results"])

    if 'amphetamines' in sewage_selector:
        df = df.append(amphetamine_df)
    if 'methamphetamines' in sewage_selector:
        df = df.append(methamphetamine_df)
    if 'MDMA' in sewage_selector:
        df = df.append(MDMA_df)
    if 'cocaine' in sewage_selector:
        df = df.append(cocaine_df)
    
    for var in extra_terms:
        print(extra_terms)
        print(var)
        globals()[var + "_mentions_results"] = []
        globals()[var + "_cases_results"] = []
        if mentions_case_selector == 'mentions':
            if not (len(globals()[var + "_mentions_results"]) > 0):
                globals()[var + "_mentions_results"] = plot_lines.get_line([var], 'mentions')
            globals()["monthly_" + var + "_mentions_results"] = globals()[var + "_mentions_results"].rolling(window=rolling_mean_value).mean()
            globals()["monthly_" + var + "_mentions_results"]['type'] = var
            df = df.append(globals()["monthly_" + var + "_mentions_results"])
        elif mentions_case_selector == 'cases':
            if not (len(globals()[var + "_cases_results"]) > 0):
                globals()[var + "_cases_results"] = plot_lines.get_line([var], 'cases')
            globals()["monthly_" + var + "_cases_results"] = globals()[var + "_cases_results"].rolling(window=rolling_mean_value).mean()
            globals()["monthly_" + var + "_cases_results"]['type'] = var
            df = df.append(globals()["monthly_" + var + "_cases_results"])


    df['date'] = df.index
    fig = px.line(df, x="date", y="count", title='Monthly mentions', color='type')
    fig.update_layout(transition_duration=500)

    return fig

# @app.callback(Output("loading-output", "children"), Input("line-selector", "value"))
# def input_triggers_spinner(value):
#     time.sleep(1)
#     return value

@app.callback(
    Output("extra-terms-selector", "options"),
    Input("input", "value"),
    Input("delete-extra-items", "n_clicks_timestamp")
)
def update_output(input, n_clicks_timestamp):
    delete_terms_button_timestamp = time.time()
    curr_time = str(int(time.time()))
    click_time = str(n_clicks_timestamp)[:-3]
    new_list = []

    if input is not None:
        extra_terms.append(input)
    for term in extra_terms:
        curr = {'label': term, 'value': term}
        new_list.append(curr)
    if curr_time == click_time:
        print("Delete list")
        new_list = []
       
    # delete_terms_button_timestamp = n_clicks_timestamp
    return new_list

@app.callback(
    Output("specific-case-output", "children"),
    Input("specific-case-input", "value"),
     Input("specific-case-amount-input", "value")
)
def update_case_check(input, amount):
    cases = input
    complete = []
    print(input , amount)
    if len(input) > 0:
        result = plot_lines.get_case_that_exceed_count([input], amount)
        counts = result[0]
        cases = result[1]
        dates = result[2]
        for i in range(len(counts)):
            link = html.A(cases[i])
            link.href = 'https://uitspraken.rechtspraak.nl/inziendocument?id=' + cases[i]
            link.target = '_blank'
            curr = html.Div([
                html.P(str(counts[i]) + " mentions in " + dates[i]),
                link
            ])
            curr_el = html.Li(curr)
            complete.append(curr_el)
        if len(complete) > 0:
            relevant_cases = complete
        else:
            relevant_cases = []
    return relevant_cases

if __name__ == '__main__':
    app.run_server(debug=True)