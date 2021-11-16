#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractPeople(object):

    def __init__(self):
        self._login_name = None
        self._nick_name = None
        self._real_name = None
        self._type_is_login_name = None
        self._work_no = None

    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def type_is_login_name(self):
        return self._type_is_login_name

    @type_is_login_name.setter
    def type_is_login_name(self, value):
        self._type_is_login_name = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_name:
            if hasattr(self.login_name, 'to_alipay_dict'):
                params['login_name'] = self.login_name.to_alipay_dict()
            else:
                params['login_name'] = self.login_name
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.type_is_login_name:
            if hasattr(self.type_is_login_name, 'to_alipay_dict'):
                params['type_is_login_name'] = self.type_is_login_name.to_alipay_dict()
            else:
                params['type_is_login_name'] = self.type_is_login_name
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractPeople()
        if 'login_name' in d:
            o.login_name = d['login_name']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'type_is_login_name' in d:
            o.type_is_login_name = d['type_is_login_name']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


