# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                  dcc.Dropdown(id='site-dropdown',
                                        options=[
                                            {'label': 'All Sites', 'value': 'ALL'},
                                            {'label': 'CCAFS LC-40', 'value': 'site1'},
                                            {'label': 'CCAFS SLC-40', 'value': 'site2'},
                                            {'label': 'KSC LC-39A', 'value': 'site3'},
                                            {'label': 'VAFB SLC-4E', 'value': 'site4'},
                                        ],
                                        value='ALL',
                                        placeholder="place holder here",
                                        searchable=True
                                        ),
                                   html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                        min=0, max=10000, step=1000,
                                        marks={0: '0', 500: '500', 1000: '1000',
                                        2500: '2500', 5000: '5000', 7500: '7500'},
                                        value=[min_payload, max_payload]),


                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output

@app.callback([
              Output(component_id='success-pie-chart', component_property='figure'),
              Output(component_id='success-payload-scatter-chart', component_property='figure')
              ],
              [
              Input(component_id='site-dropdown', component_property='value'), 
              Input(component_id="payload-slider", component_property="value")
              ]
                )

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

def get_pie_chart(entered_site, payload_slider_input):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        # pie figure
        fig_pie = px.pie(filtered_df, values='class', 
        names='Launch Site', 
        title='Total Success Launch by site')

        # scatter figure
        fig_scatter = px.scatter(spacex_df, x="Payload Mass (kg)", y="class", color="Booster Version Category")
        
        # return figures    
        return [fig_pie, fig_scatter]

    elif entered_site == 'site1': #CCAFS LC-40
         # pie figure
         filter_pd = spacex_df.loc[spacex_df['Launch Site'] == 'CCAFS LC-40']
         filter_pd = filter_pd[['Launch Site', 'class']]
         filter_pd = filter_pd.groupby('class', axis=0).count()
         filter_pd = filter_pd.reset_index()
         fig_pie = px.pie(filter_pd, values='Launch Site', 
         names='class', 
         title='Pie Chart for Launch Site CCAFS LC-40')

         # scatter figure
         filter_scatter = spacex_df.loc[(spacex_df['Launch Site'] == 'CCAFS LC-40')
                            & (spacex_df['Payload Mass (kg)'] >= payload_slider_input[0])
                            & (spacex_df['Payload Mass (kg)'] <= payload_slider_input[1])]
         fig_scatter = px.scatter(filter_scatter, x="Payload Mass (kg)", y="class", color="Booster Version Category")
        
         # return figures   
         return [fig_pie, fig_scatter]

    elif entered_site == 'site2': #CCAFS SLC-40
         # pie figure
         filter_pd = spacex_df.loc[spacex_df['Launch Site'] == 'CCAFS SLC-40']
         filter_pd = filter_pd[['Launch Site', 'class']]
         filter_pd = filter_pd.groupby('class', axis=0).count()
         filter_pd = filter_pd.reset_index()
         fig_pie = px.pie(filter_pd, values='Launch Site', 
         names='class', 
         title='Pie Chart for Launch Site CCAFS SLC-40')

         # scatter figure
         filter_scatter = spacex_df.loc[(spacex_df['Launch Site'] == 'CCAFS SLC-40')
                            & (spacex_df['Payload Mass (kg)'] >= payload_slider_input[0])
                            & (spacex_df['Payload Mass (kg)'] <= payload_slider_input[1])]
         fig_scatter = px.scatter(filter_scatter, x="Payload Mass (kg)", y="class", color="Booster Version Category")
        
         # return figures   
         return [fig_pie, fig_scatter]

    elif entered_site == 'site3': #KSC LC-39A
         # pie figure
         filter_pd = spacex_df.loc[spacex_df['Launch Site'] == 'KSC LC-39A']
         filter_pd = filter_pd[['Launch Site', 'class']]
         filter_pd = filter_pd.groupby('class', axis=0).count()
         filter_pd = filter_pd.reset_index()
         fig_pie = px.pie(filter_pd, values='Launch Site', 
         names='class', 
         title='Pie Chart for Launch Site KSC LC-39A')

         # scatter figure
         filter_scatter = spacex_df.loc[(spacex_df['Launch Site'] == 'KSC LC-39A')
                            & (spacex_df['Payload Mass (kg)'] >= payload_slider_input[0])
                            & (spacex_df['Payload Mass (kg)'] <= payload_slider_input[1])]
         fig_scatter = px.scatter(filter_scatter, x="Payload Mass (kg)", y="class", color="Booster Version Category")
        
         # return figures   
         return [fig_pie, fig_scatter] 

    elif entered_site == 'site4': #VAFB SLC-4E
          # pie figure
         filter_pd = spacex_df.loc[spacex_df['Launch Site'] == 'VAFB SLC-4E']
         filter_pd = filter_pd[['Launch Site', 'class']]
         filter_pd = filter_pd.groupby('class', axis=0).count()
         filter_pd = filter_pd.reset_index()
         fig_pie = px.pie(filter_pd, values='Launch Site', 
         names='class', 
         title='Pie Chart for Launch Site VAFB SLC-4E')

         # scatter figure
         filter_scatter = spacex_df.loc[(spacex_df['Launch Site'] == 'VAFB SLC-4E')
                            & (spacex_df['Payload Mass (kg)'] >= payload_slider_input[0])
                            & (spacex_df['Payload Mass (kg)'] <= payload_slider_input[1])]
         fig_scatter = px.scatter(filter_scatter, x="Payload Mass (kg)", y="class", color="Booster Version Category")
        
         # return figures   
         return [fig_pie, fig_scatter]
 



# Run the app
if __name__ == '__main__':
    app.run_server()
