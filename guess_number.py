import random


def play_game():
    """进行一局猜数字游戏。"""
    answer = random.randint(1, 100)
    attempts = 0

    print("我已经想好了一个 1 到 100 之间的整数，请猜猜看！")
    while True:
        try:
            guess = int(input("请输入你的猜测："))
        except ValueError:
            print("请输入有效的整数。")
            continue

        attempts += 1
        if guess > answer:
            print("太大了")
        elif guess < answer:
            print("太小了")
        else:
            print("🚩 恭喜你，插上红旗！")
            print(f"你一共猜了 {attempts} 次。")
            break


def main():
    while True:
        play_game()
        again = input("还要再玩一局吗？输入 y 继续：").strip().lower()
        if again != "y":
            print("谢谢游玩，再见！")
            break


if __name__ == "__main__":
    main()
