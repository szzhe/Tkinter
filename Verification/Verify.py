#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Verify:

    def __init__(self, stid:str, name:str, sex:str, mobile:str, email:str):
        self.stid = stid
        self.name = name
        self.sex = sex
        self.mobile = mobile
        self.email = email

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

class Verify_cls:
    stid = ""
    name = ""
    sex = ""
    mobile = ""
    email = ""

    def __init__(self, stid, name, sex, mobile, email):
        Verify_cls.stid = stid
        Verify_cls.name = name
        Verify_cls.sex = sex
        Verify_cls.mobile = mobile
        Verify_cls.email = email

    @classmethod
    def check_stid(cls):
        pattern = re.compile(R"^95\d{4}$")
        match_result = pattern.match(cls.stid)
        if match_result is None:
            return False
        else:
            return True

    @classmethod
    def check_name(cls):
        if len(cls.name.strip()) >= 2 and len(cls.name.strip()) <= 10:
            for index in range(len(cls.name.strip())):
                if cls.name[index] <= "\u4E00" or cls.name[index] >= "\u9FA5":
                    return False
                if index == len(cls.name.strip())-1:
                    return True
        else:
            return False

    @classmethod
    def check_sex(cls):
        if cls.sex.strip() in ["男", "女"]:
            return True
        else:
            return False

    @classmethod
    def check_mobile(cls):
        pattern = re.compile(R"^[1][35789]\d{9}$")
        match_result = pattern.match(cls.mobile)
        if match_result is None:
            return False
        else:
            return True

    @classmethod
    def check_email(cls):
        pattern = re.compile(R"^\w{1,}[@]\w{1,}[.]\w{1,}$")
        match_result = pattern.match(cls.email)
        if match_result is None:
            return False
        else:
            return True

    @classmethod
    def check_all(cls):
        if not cls.check_stid():
            return 1
        elif not cls.check_name():
            return 2
        elif not cls.check_sex():
            return 3
        elif not cls.check_mobile():
            return 4
        elif not cls.check_email():
            return 5
        else:
            return 0

class Verify_static:

    @staticmethod
    def check_stid(stid):
        pattern = re.compile(R"^95\d{4}$")
        match_result = pattern.match(stid)
        if match_result is None:
            return False
        else:
            return True

    @staticmethod
    def check_name(name):
        if len(name.strip()) >= 2 and len(name.strip()) <= 10:
            for index in range(len(name.strip())):
                if name[index] <= "\u4E00" or name[index] >= "\u9FA5":
                    return False
                if index == len(name.strip())-1:
                    return True
        else:
            return False

    @staticmethod
    def check_sex(sex):
        if sex.strip() in ["男", "女"]:
            return True
        else:
            return False

    @staticmethod
    def check_mobile(mobile):
        pattern = re.compile(R"^[1][35789]\d{9}$")
        match_result = pattern.match(mobile)
        if match_result is None:
            return False
        else:
            return True

    @staticmethod
    def check_email(email):
        pattern = re.compile(R"^\w{1,}[@]\w{1,}[.]\w{1,}$")
        match_result = pattern.match(email)
        if match_result is None:
            return False
        else:
            return True

if __name__ == "__main__":
    this_verify = Verify()
