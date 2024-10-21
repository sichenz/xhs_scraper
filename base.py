import datetime
import json
import pandas as pd
from time import sleep

from playwright.sync_api import sync_playwright

from xhs import DataFetchError, XhsClient, help


def sign(uri, data=None, a1="", web_session=""):
    for _ in range(10):
        try:
            with sync_playwright() as playwright:
                stealth_js_path = "/Users/princess/Documents/work/research assistant/xhs/stealth.min.js" #1
                chromium = playwright.chromium

                # 如果一直失败可尝试设置成 False 让其打开浏览器，适当添加 sleep 可查看浏览器状态
                browser = chromium.launch(headless=True)

                browser_context = browser.new_context()
                browser_context.add_init_script(path=stealth_js_path)
                context_page = browser_context.new_page()
                context_page.goto("https://www.xiaohongshu.com")
                browser_context.add_cookies([
                    {'name': 'a1', 'value': a1, 'domain': ".xiaohongshu.com", 'path': "/"}]
                )
                context_page.reload()
                # 这个地方设置完浏览器 cookie 之后，如果这儿不 sleep 一下签名获取就失败了，如果经常失败请设置长一点试试
                sleep(1)
                encrypt_params = context_page.evaluate("([url, data]) => window._webmsxyw(url, data)", [uri, data])
                return {
                    "x-s": encrypt_params["X-s"],
                    "x-t": str(encrypt_params["X-t"])
                }
        except Exception:
            # 这儿有时会出现 window._webmsxyw is not a function 或未知跳转错误，因此加一个失败重试趴
            pass
    raise Exception("重试了这么多次还是无法签名成功，呜呜呜哭哭")

def dframe(note_data):
    parsed = []
    items = note_data.get('items', [])

    for item in items:
        # 每个 note 有个 'note_card'
        note_card = item.get('note_card', {})
        
        # note_card 里的信息
        note_id = item.get('id', '')
        display_title = note_card.get('display_title', '')
        user_info = note_card.get('user', {})
        nickname = user_info.get('nickname', '')
        liked_count = note_card.get('interact_info', {}).get('liked_count', 0)
        cover_height = note_card.get('cover', {}).get('height', 0)
        cover_width = note_card.get('cover', {}).get('width', 0)
        note_type = note_card.get('type', 'normal')

        note_dict = {
            "Note ID": note_id,
            "Title": display_title,
            "User Nickname": nickname,
            "Liked Count": liked_count,
            "Cover Height": cover_height,
            "Cover Width": cover_width,
            "Note Type": note_type
        }

        parsed.append(note_dict)

    df = pd.DataFrame(parsed)
    return df


# if __name__ == '__main__':
#     cookie = "a1=192a171c6860hl8e7u0k6i2yzjc49utpeya21nhxe30000176074; web_session=040069b2455e3ddc13a54e9027354baf5d096f; webId=4169600570b606e0cb30b645ab928cf3"

#     xhs_client = XhsClient(cookie, sign=sign)
#     print(datetime.datetime.now())

#     for _ in range(10):
#         count = 0
#         try:
#             note = xhs_client.get_note_by_keyword("NYU")
#             # data = json.dumps(note, indent=4) #做成 json string file
#             # data_dict = json.loads(note) #从 json string 变成 dict
#             # print("Note data dictionary:", data_dict) 

#             df = dframe(note)
#             df.to_csv('data.csv', index=False)
#             print(df)

#             break
#         except DataFetchError as e:
#             print(e)
#             print("失败重试一下下")

keywords = [
    "NYUSH", "Stern", "NYUSH - Stern", "NYU Stern MSQF", "NYU Stern MSMRS", 
    "NYU Stern MSOMS", "NYU Stern MSDABC", "上纽", "上纽商科硕士", 
    "上纽计量金融", "上纽市场营销", "上纽组织管理与战略", "上纽数据分析", 
    "上纽MSQF", "上纽MSMRS", "上纽MSOMS", "上纽DABC"
]

if __name__ == '__main__':
    cookie = "a1=192a171c6860hl8e7u0k6i2yzjc49utpeya21nhxe30000176074; web_session=040069b2455e3ddc13a54e9027354baf5d096f; webId=4169600570b606e0cb30b645ab928cf3"
    xhs_client = XhsClient(cookie, sign=sign)

    print(datetime.datetime.now())

    for keyword in keywords:
        count = 0
        all_notes = []

        while count < 50:
            try:
                note = xhs_client.get_note_by_keyword(keyword)
                items_fetched = note.get('items', [])
                if not items_fetched: 
                    print(f"No more notes available for '{keyword}'. Stopping early.")
                    break

                all_notes.extend(items_fetched) 
                count += len(items_fetched)
                print(f"Fetched {len(items_fetched)} notes for '{keyword}', total: {count}")

            except DataFetchError as e:
                print(e)
                print(f"Failed to fetch notes for '{keyword}', retrying...")

        if all_notes:
            df = dframe({"items": all_notes[:50]})
            file_name = f'csv/{keyword}.csv'
            df.to_csv(file_name, index=False)
            print(f"Saved notes to {file_name}")
