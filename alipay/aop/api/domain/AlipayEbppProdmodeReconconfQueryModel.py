#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppProdmodeReconconfQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._chargeoff_code = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def chargeoff_code(self):
        return self._chargeoff_code

    @chargeoff_code.setter
    def chargeoff_code(self, value):
        self._chargeoff_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.chargeoff_code:
            if hasattr(self.chargeoff_code, 'to_alipay_dict'):
                params['chargeoff_code'] = self.chargeoff_code.to_alipay_dict()
            else:
                params['chargeoff_code'] = self.chargeoff_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppProdmodeReconconfQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'chargeoff_code' in d:
            o.chargeoff_code = d['chargeoff_code']
        return o


