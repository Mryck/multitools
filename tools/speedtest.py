import click
import speedtest


@click.command(name="speetest")
def run_speedtest():
    servers = []
    threads = None
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    click.echo(f"⬇️  Download")
    s.download(threads=threads)
    click.echo(f"⬆️  Upload")
    s.upload(threads=threads)

    click.echo(f"📝 Ping {s.results.ping}")
    click.echo(f"📝 Download {round(s.results.download/1000000)} Mbits/sec")
    click.echo(f"📝 Upload {round(s.results.upload/1000000)} Mbits/sec")
