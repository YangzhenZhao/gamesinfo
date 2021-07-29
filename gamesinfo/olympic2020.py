import json

import requests
from prettytable import PrettyTable

from gamesinfo.const import CUSTOM_HEADER
import time


def show_info(mid):
    """
    url示例: "https://app.sports.qq.com/TokyoOly/statDetail?mid=130000:3271"
    """
    last_version = ""
    while True:
        text = requests.get(
            f"https://app.sports.qq.com/TokyoOly/statDetail?mid={mid}",
            headers=CUSTOM_HEADER,
        ).text
        info = json.loads(text)
        version = info["version"]
        if version == last_version:
            time.sleep(30)
        last_version = version
        if info["code"] != 0:
            print("暂无数据!")
            break
        match_info = info["data"]['matchInfo']
        print(match_info['matchDesc'])
        print(f"比赛状态: {match_info['period']}")
        print(f"预计开始时间: {match_info['startTime']}")
        print(f"预计结束时间: {match_info['endTime']}")
        game_info = info["data"]["stats"][0]["rows"]

        table = PrettyTable()
        for i, columns in enumerate(game_info):
            row_info = [item["html"] for item in columns]
            if i == 0:
                table.field_names = row_info
            else:
                table.add_row(row_info)
        print(table.get_string())

        if match_info['period'] == "已结束":
            break
        time.sleep(30)


if __name__ == "__main__":
    show_info("130000:3271")
