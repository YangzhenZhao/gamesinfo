import click

from gamesinfo.olympic2020 import show_info


@click.command()
@click.option("-m", "--mid")
def cli(mid):
    if mid is not None:
        show_info(mid)
