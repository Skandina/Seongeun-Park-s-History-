#!/usr/bin/env python3

import os
import sys
import signal

class Killing(object):

    def __init__(self):
        self.proc_ins = os.popen('ps aux').read().splitlines()
        self.process_name = sys.argv[1]
        self.id = sys.argv[1]

    def killbyname(self):

        for process in self.proc_ins:
            elements = process.split()
            pid = elements[1]
            name = elements[10]
            if self.process_name in name:
                print("[{}]{}(User) {}%(CPU) %{}(Mem) {}(Started) {}(Elapsed)".format(pid, elements[0], elements[2], elements[3], elements[8], elements[9], name))
            if self.id in pid:
                os.kill(int(self.id),signal.SIGTERM)
                print("Kills one process identified by {}".format(self.id))


