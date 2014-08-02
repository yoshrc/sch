#!/usr/bin/env python3
"""
追加要求
優先度略記
"""

"""
sch - スケジュール管理プログラム
      日付が変わる前後に使うと、まずいことになる
"""

from aprparse import ArgumentParser
from schedule import ScheduleList
import sys
import os

# DATAFILENAME = os.getenv("MYTOOL") + '/sch/schedule-list'
DATAFILENAME = os.getenv("MYTOOL") + '/sch2/test'

def show(args):
    print('no command:', args)

def add(args):
    print('command add:', args)

def done(args):
    print('command done:', args)

parser = ArgumentParser(description='コマンドラインベースTODOマネージャ',
                        add_help=False)

parser.add_argument(
    '-a', '--show-all', action='store_true',
    help='直近のものだけでなく、すべての予定を表示します'
)
parser.add_argument(
    '-d', '--show-done', action='store_true',
    help='実行済みの予定も表示します'
)
parser.add_argument(
    '-h', '--help', action='help',
    help='このヘルプメッセージを表示します'
)

subparsers = parser.add_subparsers()

"""
addコマンド使用例
sch a 20110520 e 微積分の中間試験
日付は以下の形式が利用できる
yyyymmdd : 年月日を指定
mmdd     : 本日以降の直近の月日を指定
mdd      : 本日以降の直近の月日を指定
優先度は直接数値で指定する他、以下の略記が使える（未実装）
e:最優先(Extreme) h:高(High) n:通常(Normal) l:低(Low)
"""
parser_add = subparsers.add_parser(
    'add', add_help=False,
    help='指定された日付,優先度,用事の予定を追加します'
)
parser_add.add_argument(
    'date', action='store',
    help='日付（指定方法:20140803 0803 803）'
)
parser_add.add_argument(
    'priority', action='store',
    help='NICE値（e=-18, h=-10, n=0, l=10）'
)
parser_add.add_argument(
    'todo', action='store', help='用事'
)
parser_add.add_argument(
    '-h', '--help', action='help',
    help='このヘルプメッセージを表示します'
)
parser_add.set_defaults(subcommand=add)

parser_done = subparsers.add_parser(
    'done', add_help=False, help='実行済みの予定を選択します'
)
parser_done.set_defaults(subcommand=done)

if __name__ == '__main__':
    args = parser.parse_args()
    if 'subcommand' in args:
        args.subcommand(args)
    else:
        show(args)

    """
    scheduleList = ScheduleList(DATAFILENAME)

    willWrite = options.addList or options.editList or options.doneList
    willNotify = (not willWrite or
                  options.human or options.showAll or options.showDone)

    if willWrite:
        for s in options.editList:
            scheduleList.edit(s)
        for s in options.addList:
            scheduleList.add(s)
        for sid in options.doneList:
            scheduleList.done(sid)
        scheduleList.write(DATAFILENAME)    # writeの最初にソートする

    if willNotify:
        scheduleList.notify(options.human, options.showAll, options.showDone)
    """

"""
trapするより、renameのアトミック性を利用した方がいい(man rename参照)

ファイル書き込みの旧実装:
    handlers = ignoreExitSignals()
    f = open(DATAFILENAME, 'w')
    # write on f
    f.close()
    restoreExitSignalHandlers(handlers)
これだと、writeの間中シグナルを受け付けなくなる
一旦一時ファイルに書き出して、renameする方がいい
だが、inode番号が変わるため、ハードリンクがある場合は使えない

def ignoreExitSignals():
    import signal
    signals = [signal.SIGHUP, signal.SIGINT, signal.SIGQUIT, signal.SIGTERM]
    handlerDictionary = {}
    for s in signals:
        handlerDictionary[s] = signal.getsignal(s)
        signal.signal(s, SIG_IGN)
    return handlerDictionary

def restoreExitSignalHandlers(handlerDictionary):
    import signal
    for sig in handlerDictionary:
        signal.signal(sig, handlerDictionary[sig])
"""