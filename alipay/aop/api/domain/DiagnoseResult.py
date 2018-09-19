#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiagnoseResult(object):

    def __init__(self):
        self._biz_data = None
        self._diagnose_code = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def diagnose_code(self):
        return self._diagnose_code

    @diagnose_code.setter
    def diagnose_code(self, value):
        self._diagnose_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.diagnose_code:
            if hasattr(self.diagnose_code, 'to_alipay_dict'):
                params['diagnose_code'] = self.diagnose_code.to_alipay_dict()
            else:
                params['diagnose_code'] = self.diagnose_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiagnoseResult()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'diagnose_code' in d:
            o.diagnose_code = d['diagnose_code']
        return o


