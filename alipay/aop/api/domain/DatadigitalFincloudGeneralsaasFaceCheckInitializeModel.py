#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasFaceCheckInitializeModel(object):

    def __init__(self):
        self._biz_code = None
        self._outer_order_no = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def outer_order_no(self):
        return self._outer_order_no

    @outer_order_no.setter
    def outer_order_no(self, value):
        self._outer_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.outer_order_no:
            if hasattr(self.outer_order_no, 'to_alipay_dict'):
                params['outer_order_no'] = self.outer_order_no.to_alipay_dict()
            else:
                params['outer_order_no'] = self.outer_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasFaceCheckInitializeModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'outer_order_no' in d:
            o.outer_order_no = d['outer_order_no']
        return o


