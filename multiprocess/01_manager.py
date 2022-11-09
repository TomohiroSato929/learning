from multiprocessing import Process
from time import sleep
from os import getpid, getppid


def f1(name):
    """ 引数を渡せる """
    print("Hello {} pid={} ppid={}   sleep 3 sec".format(name, getpid(), getppid()))
    sleep(5)
    print("Good morning", name)


def f2(*args, **kwargs):
    """可変長引数、辞書型の引数を渡せる"""
    print("args=", args, " kwargs=",kwargs)
    print("Hello", kwargs["name"], " pid", getpid(), getppid())
    print("Sleeping... {}s".format(kwargs["tlen"]))
    sleep(kwargs["tlen"])
    print("Good morning", kwargs["name"])


if __name__ == "__main__":
    # サブプロセスを作成します
    print(__name__, " pid", getpid())
    p1 = Process(target=f1, args=("Bob",))
    p2 = Process(target=f2, args=("Bob",), kwargs={"name": "Alice", "tlen":10})
    # サブプロセスを開始します
    p1.start()
    p2.start()
    print("Processes started.")
    # サブプロセスが終了するまで待ちます。
    p1.join()
    p2.join()
    print("Processes joined.")