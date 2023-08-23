#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PucInstCode(object):

    def __init__(self):
        self._biz_type = None
        self._inst_code = None
        self._inst_name = None
        self._sub_biz_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PucInstCode()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


