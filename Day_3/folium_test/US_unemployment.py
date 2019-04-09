import pandas as pd
import folium

ctx = '../data/'
json = ctx+'us-states.json'
csv = ctx+'US_Unemployment_Oct2012.csv'
data = pd.read_csv(csv)

m = folium.Map(location=[37, -102], zoom_start=5)
m.choropleth(
    geo_data = json,
    name = 'choropleth',
    data = data,
    colums = ['state','Unemployment'],
    key_on = 'feature.id',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    fill_opactiy = 0.5,
    legend_name='Unemployment Rate (%)'
)

folium.LayerControl().add_to(m)
m.save(ctx+'result.html')


