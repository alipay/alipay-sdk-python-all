#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoginRecordDTO(object):

    def __init__(self):
        self._exit_time = None
        self._login_time = None
        self._passport_id = None

    @property
    def exit_time(self):
        return self._exit_time

    @exit_time.setter
    def exit_time(self, value):
        self._exit_time = value
    @property
    def login_time(self):
        return self._login_time

    @login_time.setter
    def login_time(self, value):
        self._login_time = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exit_time:
            if hasattr(self.exit_time, 'to_alipay_dict'):
                params['exit_time'] = self.exit_time.to_alipay_dict()
            else:
                params['exit_time'] = self.exit_time
        if self.login_time:
            if hasattr(self.login_time, 'to_alipay_dict'):
                params['login_time'] = self.login_time.to_alipay_dict()
            else:
                params['login_time'] = self.login_time
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoginRecordDTO()
        if 'exit_time' in d:
            o.exit_time = d['exit_time']
        if 'login_time' in d:
            o.login_time = d['login_time']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        return o


