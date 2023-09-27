#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrhealthKdysPersoninfoQueryModel(object):

    def __init__(self):
        self._data_key = None
        self._no_login_code = None

    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def no_login_code(self):
        return self._no_login_code

    @no_login_code.setter
    def no_login_code(self, value):
        self._no_login_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.no_login_code:
            if hasattr(self.no_login_code, 'to_alipay_dict'):
                params['no_login_code'] = self.no_login_code.to_alipay_dict()
            else:
                params['no_login_code'] = self.no_login_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrhealthKdysPersoninfoQueryModel()
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'no_login_code' in d:
            o.no_login_code = d['no_login_code']
        return o


