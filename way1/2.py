import requests


class A(object):
    def __init__(self):
        self.session = requests.session()
        self.username = ""

    def get_new_session(self):
        pass

    def run(self):
        u = "https://raw.githubusercontent.com/peterpuf/pyet/master/way1/1.py"
        r = requests.get(u)
        print(r.text)


if __name__ == '__main__':
    A().run()

    # 更新时间比较长，一般1-2分钟左右才会更新到raw上
