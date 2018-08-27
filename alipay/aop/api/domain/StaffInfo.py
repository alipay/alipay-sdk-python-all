#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StaffInfo(object):

    def __init__(self):
        self._logon_id = None
        self._user_id = None

    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StaffInfo()
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


