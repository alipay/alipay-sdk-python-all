#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthenticationTokenSaveModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_obj = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_obj(self):
        return self._biz_obj

    @biz_obj.setter
    def biz_obj(self, value):
        self._biz_obj = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_obj:
            if hasattr(self.biz_obj, 'to_alipay_dict'):
                params['biz_obj'] = self.biz_obj.to_alipay_dict()
            else:
                params['biz_obj'] = self.biz_obj
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthenticationTokenSaveModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_obj' in d:
            o.biz_obj = d['biz_obj']
        return o


