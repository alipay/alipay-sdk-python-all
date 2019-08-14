#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradePrecreateConfirmPrecreateCodeInfo(object):

    def __init__(self):
        self._precreate_code = None
        self._precreate_code_create_time = None
        self._precreate_code_type = None

    @property
    def precreate_code(self):
        return self._precreate_code

    @precreate_code.setter
    def precreate_code(self, value):
        self._precreate_code = value
    @property
    def precreate_code_create_time(self):
        return self._precreate_code_create_time

    @precreate_code_create_time.setter
    def precreate_code_create_time(self, value):
        self._precreate_code_create_time = value
    @property
    def precreate_code_type(self):
        return self._precreate_code_type

    @precreate_code_type.setter
    def precreate_code_type(self, value):
        self._precreate_code_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.precreate_code:
            if hasattr(self.precreate_code, 'to_alipay_dict'):
                params['precreate_code'] = self.precreate_code.to_alipay_dict()
            else:
                params['precreate_code'] = self.precreate_code
        if self.precreate_code_create_time:
            if hasattr(self.precreate_code_create_time, 'to_alipay_dict'):
                params['precreate_code_create_time'] = self.precreate_code_create_time.to_alipay_dict()
            else:
                params['precreate_code_create_time'] = self.precreate_code_create_time
        if self.precreate_code_type:
            if hasattr(self.precreate_code_type, 'to_alipay_dict'):
                params['precreate_code_type'] = self.precreate_code_type.to_alipay_dict()
            else:
                params['precreate_code_type'] = self.precreate_code_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradePrecreateConfirmPrecreateCodeInfo()
        if 'precreate_code' in d:
            o.precreate_code = d['precreate_code']
        if 'precreate_code_create_time' in d:
            o.precreate_code_create_time = d['precreate_code_create_time']
        if 'precreate_code_type' in d:
            o.precreate_code_type = d['precreate_code_type']
        return o


