import plotly
import plotly.graph_objects as go
from geo import mapbox_access_token
from geo import get_country_border
from geo import get_bbox
from geo import get_airports
from geo import get_earthquakes
from geo import get_meteorites
from geo import get_ufos
from geo import get_volcanos


if __name__ == '__main__':
    mapbox_style = "mapbox://styles/neeharikak/ck3yt0g624vwr1clm0itq8t5r"

    airLats,airLons = get_airports()
    earthLats, earthLons = get_earthquakes()
    meteorLats, meteorLons = get_meteorites()
    ufoLats, ufoLons = get_ufos()
    volcanoLats, volcanoLons = get_volcanos()

    airports = [go.Scattermapbox(
        lat=airLats,
        lon = airLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='blue',
            opacity = .8,
        ),
        name='Airports'
    )]

    ufos = [go.Scattermapbox(
        lat=ufoLats,
        lon = ufoLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='green',
            opacity = .8,
        ),
        name='Ufo Sightings'
    )]

    volcanos = [go.Scattermapbox(
        lat=volcanoLats,
        lon = volcanoLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='red',
            opacity = .8,
        ),
        name='Volcanos'
    )]

    earthquakes = [go.Scattermapbox(
        lat=earthLats,
        lon = earthLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='orange',
            opacity = .8,
        ),
        name='Earthquakes'
    )]
    meteorites = [go.Scattermapbox(
        lat=meteorLats,
        lon = meteorLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='cyan',
            opacity = .8,
        ),
        name='Meteorites'
    )]
    
    layout = go.Layout(autosize=True,
    mapbox = dict(accesstoken= mapbox_access_token,
    bearing=0,
    pitch=0,
    zoom=5,
    center=dict(lat=0,lon=0),
    style=mapbox_style),
    width=1500,
    height=1080,
    title = "Armageddon")

    fig = dict(data=earthquakes+meteorites+volcanos+ufos+airports, layout=layout)
    plotly.offline.plot(fig, filename='armageddon.html')
