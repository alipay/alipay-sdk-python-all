#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryBizinfoQueryModel(object):

    def __init__(self):
        self._biz_inst = None
        self._biz_type = None
        self._data_code = None
        self._request_context = None

    @property
    def biz_inst(self):
        return self._biz_inst

    @biz_inst.setter
    def biz_inst(self, value):
        self._biz_inst = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def data_code(self):
        return self._data_code

    @data_code.setter
    def data_code(self, value):
        self._data_code = value
    @property
    def request_context(self):
        return self._request_context

    @request_context.setter
    def request_context(self, value):
        self._request_context = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_inst:
            if hasattr(self.biz_inst, 'to_alipay_dict'):
                params['biz_inst'] = self.biz_inst.to_alipay_dict()
            else:
                params['biz_inst'] = self.biz_inst
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.data_code:
            if hasattr(self.data_code, 'to_alipay_dict'):
                params['data_code'] = self.data_code.to_alipay_dict()
            else:
                params['data_code'] = self.data_code
        if self.request_context:
            if hasattr(self.request_context, 'to_alipay_dict'):
                params['request_context'] = self.request_context.to_alipay_dict()
            else:
                params['request_context'] = self.request_context
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryBizinfoQueryModel()
        if 'biz_inst' in d:
            o.biz_inst = d['biz_inst']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'data_code' in d:
            o.data_code = d['data_code']
        if 'request_context' in d:
            o.request_context = d['request_context']
        return o


