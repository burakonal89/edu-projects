# -*- coding: utf-8 -*-
__author__ = "burakonal"
import pandas as pd
import re

# pd.set_option("display.max_colwidth", 100000)

def pre_process(file_):
    df = pd.DataFrame(columns=["date", "time", "name", "message"])
    info_pattern = re.compile(r'(\d\d/\d\d/\d\d\d\d),\s(\d\d:\d\d:\d\d):\s')
    iter_ = 0
    with open(file_, "r") as f_read, open("data.csv", "w") as f_write:
        for line in f_read:
            line = line.strip()
            info = info_pattern.match(line)
            if info:
                date = info.group(1)
                time = info.group(2)
                body = line[21:]
                if ":" not in body:
                    name = "info_message"
                    message = body.strip()
                else:
                    name, message = body.split(":", 1)
                    name = name.strip()
                    message = message.strip()
                # print iter_, message
                text = date+" "+time+"\t"+name+"\t"+message+"\n"
                f_write.write(text)
                # df.loc[iter_] = [date, time, name, message]
                # print [date, time, name, message]
            #     previous_date = date
            #     previous_time = time
            #     previous_name = name
            #     previous_message = message
            # else:
            #     df.message[(df.date == previous_date) &
            #                (df.time == previous_time) &
            #                (df.name == previous_name)] = previous_message + " " + line
    #         iter_ += 1
    #         if iter_ == 10:
    #             break
    #
    # return df


df = pre_process("_chat.txt")
# df = pd.read_csv("data.csv", sep="\t", names=["date", "time", "name", "message"])
# print df.loc[4]
# print df.loc[8]
