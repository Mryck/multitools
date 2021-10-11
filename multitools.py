import click
from tools.speedtest import run_speedtest


@click.group()
def cli():
    pass


cli.add_command(run_speedtest, "speedtest")

if __name__ == "__main__":
    cli()
