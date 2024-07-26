def mystery_function(lst):
    result = lst.copy()  # 元のリストをコピーして変更を行う
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  # 偶数の要素をチェック
            result[i] = lst[i] ** 2  # 偶数の要素を二乗
    return result
