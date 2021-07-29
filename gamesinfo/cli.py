import click

from gamesinfo.olympic2020 import show_info


# 130000:3271  14:00开始
# 130000:3283  15:00开始
# 130000:212  15:25开始
@click.command()
def cli():
    show_info("130000:3271")
