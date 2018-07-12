#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import re

class Verification(Tk):

    def __init__(self, stid:str, name:str, sex:str, mobile:str, email:str):
        self.stid = stid
        self.name = name
        self.sex = sex
        self.mobile = mobile
        self.email = email

        self.check_stid()
        self.check_name()
        self.check_sex()
        self.check_mobile()
        self.check_email()

        self.check_all()

    def check_stid(self):
        pattern = re.compile(R"^95\d{4}$")
        match_result = pattern.match(self.stid)
        if match_result is None:
            return False
        else:
            return True

    def check_name(self):
        if len(self.name.strip()) >= 2 and len(self.name.strip()) <= 10:
            for index in range(len(self.name.strip())):
                if self.name[index] <= "\u4E00" or self.name[index] >= "\u9FA5":
                    return False
                if index == len(self.name.strip())-1:
                    return True
        else:
            return False

    def check_sex(self):
        if self.sex.strip() in ["男", "女"]:
            return True
        else:
            return False

    def check_mobile(self):
        pattern = re.compile(R"^[1][35789]\d{9}$")
        match_result = pattern.match(self.mobile)
        if match_result is None:
            return False
        else:
            return True

    def check_email(self):
        pattern = re.compile(R"^\w{1,}[@]\w{1,}[.]\w{1,}$")
        match_result = pattern.match(self.email)
        if match_result is None:
            return False
        else:
            return True

    def check_all(self):
        if not self.check_stid():
            return 1
        elif not self.check_name():
            return 2
        elif not self.check_sex():
            return 3
        elif not self.check_mobile():
            return 4
        elif not self.check_email():
            return 5
        else:
            return 0

if __name__ == "__main__":
    this_verification = Verification()
