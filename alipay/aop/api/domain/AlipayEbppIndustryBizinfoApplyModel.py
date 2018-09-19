#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryBizinfoApplyModel(object):

    def __init__(self):
        self._ability_code = None
        self._bill_key = None
        self._biz_inst = None
        self._biz_type = None
        self._out_apply_no = None
        self._request_context = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
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
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def request_context(self):
        return self._request_context

    @request_context.setter
    def request_context(self, value):
        self._request_context = value


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
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
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
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
        o = AlipayEbppIndustryBizinfoApplyModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_inst' in d:
            o.biz_inst = d['biz_inst']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'request_context' in d:
            o.request_context = d['request_context']
        return o


