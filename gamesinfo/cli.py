import click

from gamesinfo.olympic2020 import game_list_show, show_info


@click.command()
@click.option("-m", "--mid")
@click.option("-l", "--list", is_flag=True)
def cli(mid, list):
    if mid is not None:
        show_info(mid)
    if list is not None:
        game_list_show()
