result_list = []

def eight_stairs(total, line, prev):
    # 終了条件
    if total == 8:
        result_list.append(line)
        return
    if total > 8:
        return

    # 1を選ぶ
    eight_stairs(total + 1, line + [1], 1)

    # 2を選ぶ（連続禁止）
    if prev != 2:
        eight_stairs(total + 2, line + [2], 2)

# 実行
eight_stairs(0, [], 0)

# 結果
for r in result_list:
    print(r)

print("列の数は", len(result_list), "です。")