# sch

コマンドラインベースのTODOマネージャです。

実行にはバージョン3のPythonが必要です。

## インストール

    git clone git://github.com/yoshrc/sch.git

## おすすめ設定

- パスの通った場所に、sch/schへのシンボリックリンクを貼る
- .bashrcに`sch`を追加

## 使い方

登録した予定を表示

    $ sch
    *** 2014年8月3日　日曜日 ***
    予定日         NICE 用事
    2014/08/04(月) 0    飲み会 17:50集合
    2014/08/07(木) -18  アルゴリズム課題提出期限

予定の追加

    $ sch add 805 -10 映画
    予定を追加しました。
    *** 2014年8月3日　日曜日 ***
      予定日         NICE 用事
      2014/08/04(月) 0    飲み会 17:50集合
    * 2014/08/05(火) -10  映画
      2014/08/07(木) -18  アルゴリズム課題提出期限

実行済みの予定をリストから削除

    $ sch done
    実行済みの予定を番号で選択してください。
    複数選択する場合、半角スペースで区切ってください。

       予定日         NICE 用事
    0: 2014/08/04(月) 0    飲み会 17:50集合
    1: 2014/08/05(火) -10  映画
    2: 2014/08/07(木) -18  アルゴリズム課題提出期限

    > 2

    1個の予定を実行済みにしました。
    *** 2014年8月3日　日曜日 ***
      予定日         NICE 用事
      2014/08/04(月) 0    飲み会 17:50ロータリー集合
      2014/08/05(火) -10  映画
    D 2014/08/07(木) -18  アルゴリズム課題提出期限

ヘルプ

    $ sch --help
    usage: sch [-a] [-d] [-h] {add,a,done,d} ...

    コマンドラインベースTODOマネージャ

    positional arguments:
      {add,a,done,d}
        add (a)        指定された日付,優先度,用事の予定を追加します
        done (d)       実行済みの予定を選択します

    optional arguments:
      -a, --show-all   直近のものだけでなく、今後すべての予定を表示します
      -d, --show-done  実行済みの予定も表示します
      -h, --help       このヘルプメッセージを表示します
    $ sch add --help
    usage: sch add [-h] date priority todo

    positional arguments:
      date        日付（指定方法:20140803 0803 803）
      priority    NICE値（e=-18, h=-10, n=0, l=10）
      todo        用事

    optional arguments:
      -h, --help  このヘルプメッセージを表示します

## 予定の優先度（重要度）について

各予定にはNICE値と呼ばれる優先度をつけることになります。NICE値とは、Linux系OSにおいてプロセスの優先度を表す数値で、-20以上19以下の整数値を取り、数値が低いほど優先度が高くなります。schにおけるNICE値の扱いは以下のようになります。

| NICE値            | 重要度 | 通知                             |
| ----------------- | ------ | -------------------------------- |
| -20 <=NICE <= -16 | 最重要 | schを実行すると常に表示されます  |
| -15 <= NICE <= 16 | 重要   | 予定日の一ヶ月前から表示されます |
| -5 <= NICE <= 5   | 通常   | 予定日の一週間前から表示されます |
| 6 <= NICE <= 19   | 低     | 予定日の3日前から表示されます    |
