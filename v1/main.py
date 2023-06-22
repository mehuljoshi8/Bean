'''
Author: Mehul Joshi
Version: 1.0
'''

import sqlite3
import datetime
import os
import matplotlib.pyplot as plt

def init_tables() -> None:
    conn = sqlite3.connect("bean.db")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE ssid2date (
                    id INTEGER PRIMARY KEY,
                    dateTime TIMESTAMP NOT NULL UNIQUE);''')
    curr.execute('''CREATE TABLE ssid2mid (
                    ssid INTEGER NOT NULL,
                    LC TEXT,
                    LW TEXT,
                    M TEXT,
                    RW TEXT,
                    RC TEXT,
                    FOREIGN KEY (ssid) REFERENCES ssid2date(id));''')
    curr.execute('''CREATE TABLE ssid2threes (
                    ssid INTEGER NOT NULL,
                    LC TEXT,
                    LW TEXT,
                    M TEXT,
                    RW TEXT,
                    RC TEXT,
                    FOREIGN KEY (ssid) REFERENCES ssid2date(id));''')
    conn.commit()

def log(table: str, date: datetime) -> None:
    conn = sqlite3.connect("bean.db")
    curr = conn.cursor()
    date = datetime.date.today() if date == None else date
    curr.execute("SELECT * FROM ssid2date WHERE datetime=?", (date,))
    rows = curr.fetchall()
    if len(rows) == 0:
        curr.execute("INSERT INTO ssid2date VALUES (NULL, ?)", (date,))
        curr.execute("SELECT * FROM ssid2date WHERE datetime=?", (date,))
        rows = curr.fetchall()
    ssid = rows[0][0]
    print("ssid = ", ssid)
    LC = input("LC: ")
    LW = input("LW: ")
    M = input("M: ")
    RW = input("RW: ")
    RC = input("RC: ")
    insert_query = "INSERT INTO {} VALUES ({}, '{}', '{}', '{}', '{}', '{}')".format(table, ssid, LC, LW, M, RW, RC)
    curr.execute(insert_query)
    conn.commit()
    curr.close()
    conn.close()

# plots the data for a specific table (mid or threes) and a specific location (LC, LW...)
def plot(table: str) -> None:
    conn = sqlite3.connect("bean.db")
    curr = conn.cursor()
    xs = []
    ys = [[], [], [], [], []]
    totals = []

    curr.execute("SELECT * FROM ssid2date")
    ssid2dates = curr.fetchall()
    ssid2dates = sorted(ssid2dates, key=lambda x: x[1])
    for e in ssid2dates:
        xs.append(e[1])
    print(ssid2dates)
    curr.execute("SELECT * FROM {}".format(table))
    rows = curr.fetchall()
    print(rows)

    for e in ssid2dates:
        total_made, total_missed = 0, 0
        for i in range(1, 6):
            n, d = rows[e[0] - 1][i].split("/")
            total_made += int(n)
            total_missed += int(d)
            ys[i - 1].append(round(int(n) / int(d), 3))
        totals.append(round(total_made / total_missed, 3))
    
    labels = ["left corner", "left wing", "middle", "right wing", "right corner", "total made/attempted"]
    for i in range(0, 5):
        plt.plot(xs, ys[i], 'o', ls="-")
    
    plt.plot(xs, totals, 'o', ls="-")

    plt.title(table)
    plt.legend(labels)
    plt.xlabel("dates")
    plt.ylabel("percentage")
    plt.grid(True)
    plt.show()

def route_input(stdin: str) -> None:
    tokens = stdin.split(" ")
    if stdin == "quit" or stdin == "exit":
        print("Cleaning up Bean!")
        conn = sqlite3.connect("bean.db")
        curr = conn.cursor()
        conn.commit()
        curr.close()
        conn.close()
        print("See you soon :)")
        os._exit(0)
    elif tokens[0] == "log":
        table = "ssid2" + tokens[1]
        date = datetime.datetime.strptime(tokens[2], '%m/%d/%Y').date() if len(tokens) == 3 else None
        log(table, date)
    elif tokens[0] == "plot":
        print("plotting data")
        plot("ssid2" + tokens[1])

def main() -> None:
    print("Welcome to Bean!")
    ascii_art = open("./ascii_art/dunk.txt")
    for l in ascii_art:
        print(l, end='')
    print()

    if not os.path.isfile("./bean.db"):
        init_tables()
    
    while True:
        stdin = input("> ")
        print(stdin)
        route_input(stdin)

if __name__ == "__main__":
    main()
