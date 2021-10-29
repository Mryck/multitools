import click
from metno_locationforecast import Place, Forecast


@click.command(name="weather")
@click.option("--lat", required=True, type=float)
@click.option("--long", required=True, type=float)
@click.option("--alt", default=1, type=float)
def get_weather(lat, long, alt):
    USER_AGENT = "metno_locationforecast/2.0 https://github.com/Mryck/multitools"
    place = Place("MyPlace", lat, long, alt)
    place_forecast = Forecast(place, USER_AGENT)
    place_forecast.update()
    click.echo(place_forecast.data.intervals[0])

