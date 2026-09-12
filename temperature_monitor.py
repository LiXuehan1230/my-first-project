"""使用模拟数据演示简单的温度监测。"""


# 预先准备一组模拟温度数据，单位为摄氏度（℃）。
temperatures = [25, 28, 31, 29, 35]

# 依次读取列表中的每一个温度。
for temperature in temperatures:
    # 显示当前正在监测的温度。
    print(f"当前温度：{temperature}℃")

    # 判断当前温度是否超过 30℃，并显示对应状态。
    if temperature > 30:
        print("高温报警")
    else:
        print("温度正常")

