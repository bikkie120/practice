# 主なコマンド】
# p(print) 引数に指定した変数の値を出力する。
# a(args) 現在の関数で使用している引数一覧を出力する。
# l(list) 現在のソースコードの前後の行を表示する。
# c(continue) 次のbreakpoint()まで処理を進める。
# s(step) 現在の行を実行し、次の行に進む。次の行が関数の場合、関数内に入って停止する。次の行が関数でない場合は、現在の関数の次の行で停止する。
# n(next) 現在の行を実行し、次の行に進む。次の行が関数の場合でも関数内には入らない。
# r(return) 現在の関数が返るまで実行する。
# j(jump) 次に実行する行を指定できる。ただし、for文の中などは入れないなどの制限あり。
# q(quit)デバッグを終了する。

def main():
    stock_price1 = 1000
    stock_price2 = 2000
    stock_price3 = 3000
    breakpoint()

    average = (stock_price1 + stock_price2 + stock_price3) / 3
    print(f"平均株価:{average}円")


if __name__ == '__main__':
    main()
