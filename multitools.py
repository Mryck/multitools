import click
from tools.speedtest import run_speedtest
from tools.metno import get_weather



@click.group()
def cli():
    pass


cli.add_command(run_speedtest, "speedtest")
cli.add_command(get_weather, "weather")


if __name__ == "__main__":
    cli()
