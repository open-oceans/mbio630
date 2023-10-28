import requests

cookies = {
    '__atuvc': '0%7C14%2C0%7C15%2C0%7C16%2C0%7C17%2C2%7C18',
    '__atrfs': 'ab/|pos/|tot/|rsi/644e630200000000|cfc/|hash/0|rsiq/|fuid/76cc236c|rxi/|rsc/|gen/1|csi/|dr/',
    '_pk_ref.57.a333': '%5B%22%22%2C%22%22%2C1692107614%2C%22https%3A%2F%2Fwww.nature.com%2F%22%5D',
    '_pk_id.57.a333': '22dbd28e16ced8b9.1677307436.10.1692107614.1692066860.',
    '5569e5a730cade8ff2b54f1e815f3670': 'f9d271ac9b68d71cd5509013725d4800',
    'session': '796aad47137f11d8_653c81cc._mASNo8UXtZJy3MUT0G30Fm3tRs',
    'csrftoken': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTY5ODQ2NDIwNCwiZXhwIjoxNjk4NTUwNjA0fQ.ImZQUVBZaUhYMW54ZnBaaFJLcTc4Q1RyVFJkTmNLU2FIIg.hbjqFVvBLRwbuTNftDhuOqIRKg_GGFpofKhrFBzYiMPScEqsGr9uHFzzhiqWu3wI0ZELXx1UUme_fmBWx77KiQ',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Content-Type': 'application/json',
    # 'Cookie': '__atuvc=0%7C14%2C0%7C15%2C0%7C16%2C0%7C17%2C2%7C18; __atrfs=ab/|pos/|tot/|rsi/644e630200000000|cfc/|hash/0|rsiq/|fuid/76cc236c|rxi/|rsc/|gen/1|csi/|dr/; _pk_ref.57.a333=%5B%22%22%2C%22%22%2C1692107614%2C%22https%3A%2F%2Fwww.nature.com%2F%22%5D; _pk_id.57.a333=22dbd28e16ced8b9.1677307436.10.1692107614.1692066860.; 5569e5a730cade8ff2b54f1e815f3670=f9d271ac9b68d71cd5509013725d4800; session=796aad47137f11d8_653c81cc._mASNo8UXtZJy3MUT0G30Fm3tRs; csrftoken=eyJhbGciOiJIUzUxMiIsImlhdCI6MTY5ODQ2NDIwNCwiZXhwIjoxNjk4NTUwNjA0fQ.ImZQUVBZaUhYMW54ZnBaaFJLcTc4Q1RyVFJkTmNLU2FIIg.hbjqFVvBLRwbuTNftDhuOqIRKg_GGFpofKhrFBzYiMPScEqsGr9uHFzzhiqWu3wI0ZELXx1UUme_fmBWx77KiQ',
    'Origin': 'https://zenodo.org',
    'Referer': 'https://zenodo.org/account/settings/github/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-CSRFToken': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTY5ODQ2NDIwNCwiZXhwIjoxNjk4NTUwNjA0fQ.ImZQUVBZaUhYMW54ZnBaaFJLcTc4Q1RyVFJkTmNLU2FIIg.hbjqFVvBLRwbuTNftDhuOqIRKg_GGFpofKhrFBzYiMPScEqsGr9uHFzzhiqWu3wI0ZELXx1UUme_fmBWx77KiQ',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.post('https://zenodo.org/api/user/github/repositories/sync', cookies=cookies, headers=headers,timeout=None)
print(response.status_code)
