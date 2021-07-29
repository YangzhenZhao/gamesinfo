import click

from gamesinfo.olympic2020 import show_info


# 130000:3283  15:00开始
# 130000:212  15:25开始
@click.command()
@click.option("-m", "--mid")
def cli(mid):
    if mid is not None:
        show_info(mid)
