import click

from gamesinfo.olympic2020 import game_list_show, show_info


@click.command()
@click.option("-m", "--mid")
@click.option("-l", "--list", is_flag=True, default=False)
@click.option("-d", "--date")
@click.option("-f", "--finish", is_flag=True, default=False)
def cli(mid, list, date, finish):
    if mid is not None:
        show_info(mid)
    if list:
        game_list_show(date=date)
    if finish:
        game_list_show(date=date, is_finish=finish)
