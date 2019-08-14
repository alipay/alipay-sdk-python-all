#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAppinfoQueryModel(object):

    def __init__(self):
        self._logon_id = None
        self._open_app_type = None

    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def open_app_type(self):
        return self._open_app_type

    @open_app_type.setter
    def open_app_type(self, value):
        self._open_app_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.open_app_type:
            if hasattr(self.open_app_type, 'to_alipay_dict'):
                params['open_app_type'] = self.open_app_type.to_alipay_dict()
            else:
                params['open_app_type'] = self.open_app_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAppinfoQueryModel()
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'open_app_type' in d:
            o.open_app_type = d['open_app_type']
        return o


