#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataSendBusinessResult(object):

    def __init__(self):
        self._biz_code = None
        self._biz_msg = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_msg:
            if hasattr(self.biz_msg, 'to_alipay_dict'):
                params['biz_msg'] = self.biz_msg.to_alipay_dict()
            else:
                params['biz_msg'] = self.biz_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataSendBusinessResult()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_msg' in d:
            o.biz_msg = d['biz_msg']
        return o


