#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：multi_download_pic.py
@IDE     ：PyCharm 
@Author  ：何锦涛
@Date    ：2022/4/20 19:21 
"""
import pandas as pd
import multiprocessing
import subprocess

import sys
import os


input_file = sys.argv[1]
output_dir = sys.argv[2]


class MyProcessCommand(multiprocessing.Process):
    def __init__(self, queue=None):
        super(MyProcessCommand, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            url, cmsid, content = self.queue.get()

            try:
            # print(url)
                url_info_1, url_info_2 = url.split("/")[-2:]
                tag = eval(content)['字幕是否裁剪']
                output_filename = cmsid + "_" + url_info_1 + "_" + url_info_2 + ".jpg"
                # 裁剪图片储存为0，非裁剪的储存为1
                if tag == '是':
                    output_filepath = os.path.join(output_dir, '0')
                elif tag == '否':
                    output_filepath = os.path.join(output_dir, '1')
                else:
                    pass
                output_filepath = os.path.join(output_filepath, output_filename)
                command = "wget " + url + " -O " + output_filepath

                # print(command)
                status, output = subprocess.getstatusoutput(command)
            except Exception as e:
                print("Exception: ", e)
                pass

            self.queue.task_done()


def command(command_list, num_processes=multiprocessing.cpu_count()):
    with multiprocessing.Manager() as manager:
        queue = multiprocessing.JoinableQueue()
        workerList = []
        for i in range(num_processes):
            worker = MyProcessCommand(queue=queue)
            workerList.append(worker)
            worker.daemon = True
            worker.start()

        for command in command_list:
            queue.put(command)

        queue.join()

        for worker in workerList:
            worker.terminate()

    print("Command Success!")


input_data = pd.read_excel(input_file, header=0)
input_list = input_data.values.tolist()

command(input_list)

