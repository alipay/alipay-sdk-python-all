#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankcustAccountQueryModel(object):

    def __init__(self):
        self._logon_id = None
        self._phone_id = None

    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def phone_id(self):
        return self._phone_id

    @phone_id.setter
    def phone_id(self, value):
        self._phone_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.phone_id:
            if hasattr(self.phone_id, 'to_alipay_dict'):
                params['phone_id'] = self.phone_id.to_alipay_dict()
            else:
                params['phone_id'] = self.phone_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserDtbankcustAccountQueryModel()
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'phone_id' in d:
            o.phone_id = d['phone_id']
        return o


