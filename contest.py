from bs4 import BeautifulSoup
from requests import get
import os
import sys

def get_html(url):
    return get(url).content

def get_problems(contest_id):
    url = "https://codeforces.com/contest/" + str(contest_id)
    res = []
    soup = BeautifulSoup(get_html(url), "html.parser")
    table = soup.select("table.problems")[0]
    trs = table.select("tr")[1:]
    for tr in trs:
        td = tr.find("td")
        a = td.find("a")
        res.append(a.text.strip().lower())
    return res

def make_folders(problems, contest_id):
    if os.path.exists(str(contest_id)):
        os.system("rm -r {}".format(str(contest_id)))
    for name in problems:
        os.system("mkdir -p {}/{}".format(str(contest_id), name))
    from os.path import expanduser
    home = expanduser("~")
    for name in problems:
        with open("{}/cpp/tpl.cpp".format(home), "r") as tpl:
            with open("{}/{}/{}.cpp".format(str(contest_id), name, name), "w") as f:
                f.write(tpl.read())

def main():
    contest_id = sys.argv[1]
    problems = get_problems(contest_id)
    make_folders(problems, contest_id)


if __name__ == "__main__":
    main()


