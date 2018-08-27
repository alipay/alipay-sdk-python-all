#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicPayeeBindDeleteModel(object):

    def __init__(self):
        self._login_id = None
        self._pid = None

    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicPayeeBindDeleteModel()
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'pid' in d:
            o.pid = d['pid']
        return o


