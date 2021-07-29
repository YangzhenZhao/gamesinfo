import json

import requests
from prettytable import PrettyTable

from gamesinfo.const import CUSTOM_HEADER


def show_info(mid):
    """
    url示例: "https://app.sports.qq.com/TokyoOly/statDetail?mid=130000:3271"
    """
    text = requests.get(
        f"https://app.sports.qq.com/TokyoOly/statDetail?mid={mid}",
        headers=CUSTOM_HEADER,
    ).text
    info = json.loads(text)
    if info["code"] != 0:
        print("暂无数据!")
        return
    # version = info["version"]
    info_l = info["data"]["stats"]
    game_info = info_l[0]["rows"]

    table = PrettyTable()
    for i, columns in enumerate(game_info):
        row_info = [item["html"] for item in columns]
        if i == 0:
            table.field_names = row_info
        else:
            table.add_row(row_info)
    print(table.get_string())


if __name__ == "__main__":
    show_info("130000:3271")
