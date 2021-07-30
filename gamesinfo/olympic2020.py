import json
import time
from datetime import datetime

import requests
from prettytable import PrettyTable

from gamesinfo.const import CUSTOM_HEADER


def game_list_show(date=None, is_finish=False):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    url = (
        "https://app.sports.qq.com/match/list"
        f"?columnId=130002&dateNum=1&flag=2&date={date}"
    )
    text = requests.get(url, headers=CUSTOM_HEADER).text
    info = json.loads(text)
    if info["code"] != 0:
        print("暂无数据!")
        return
    match_list = info["data"]["matches"][date]["list"]
    table = PrettyTable()
    table.field_names = ["开始时间", "赛事", "ID"]
    for match in match_list:
        if "matchInfo" not in match:
            continue
        match_info = match["matchInfo"]
        if not is_finish:
            is_show = match_info["livePeriod"] != "2"
        else:
            is_show = match_info["livePeriod"] == "2"
        if not is_show:
            continue
        match_name = match_info["matchDesc"]
        match_id = match_info["mid"]
        match_id = match_id[match_id.find(":") + 1 :]
        start_time = match_info["startTime"]
        start_time = start_time[start_time.find(" ") + 1 :]
        table.add_row([start_time, match_name, match_id])
    print(table.get_string())


def show_info(mid):
    """
    url示例: "https://app.sports.qq.com/TokyoOly/statDetail?mid=130000:3271"
    """
    last_version = ""
    while True:
        text = requests.get(
            f"https://app.sports.qq.com/TokyoOly/statDetail?mid=130000:{mid}",
            headers=CUSTOM_HEADER,
        ).text
        info = json.loads(text)
        version = info["version"]
        if version == last_version:
            time.sleep(10)
        last_version = version
        if info["code"] != 0:
            print("暂无数据!")
            break
        match_info = info["data"]["matchInfo"]
        print(match_info["matchDesc"])
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

        if match_info["period"] == "已结束":
            break
        if match_info["period"] == "比赛前":
            time.sleep(90)
        else:
            time.sleep(25)
