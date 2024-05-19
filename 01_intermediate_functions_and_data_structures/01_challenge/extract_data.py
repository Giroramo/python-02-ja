import re

def extract_data(text):
    # 正規表現パターン: コロンで区切られたデータ名とその値をキャプチャ
    pattern = r'\w+:[^\s,.;]+'
    # 正規表現に一致する部分をすべて抽出
    matches = re.findall(pattern, text)
    return matches

def better_extract_data(text):
    # 正規表現パターン: データ名とその値をキャプチャ
    pattern = r'(\w+):([^\s,.;]+)'
    # 正規表現に一致する部分をすべて抽出
    matches = re.findall(pattern, text)
    return matches