#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcrowdUseResp(object):

    def __init__(self):
        self._method_id = None
        self._ret_val = None

    @property
    def method_id(self):
        return self._method_id

    @method_id.setter
    def method_id(self, value):
        self._method_id = value
    @property
    def ret_val(self):
        return self._ret_val

    @ret_val.setter
    def ret_val(self, value):
        self._ret_val = value


    def to_alipay_dict(self):
        params = dict()
        if self.method_id:
            if hasattr(self.method_id, 'to_alipay_dict'):
                params['method_id'] = self.method_id.to_alipay_dict()
            else:
                params['method_id'] = self.method_id
        if self.ret_val:
            if hasattr(self.ret_val, 'to_alipay_dict'):
                params['ret_val'] = self.ret_val.to_alipay_dict()
            else:
                params['ret_val'] = self.ret_val
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcrowdUseResp()
        if 'method_id' in d:
            o.method_id = d['method_id']
        if 'ret_val' in d:
            o.ret_val = d['ret_val']
        return o


