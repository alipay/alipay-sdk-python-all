#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPackage(object):

    def __init__(self):
        self._commodity_code = None
        self._commodity_name = None
        self._effective_period_num = None
        self._effective_period_type = None
        self._spec_code = None
        self._spec_name = None

    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def effective_period_num(self):
        return self._effective_period_num

    @effective_period_num.setter
    def effective_period_num(self, value):
        self._effective_period_num = value
    @property
    def effective_period_type(self):
        return self._effective_period_type

    @effective_period_type.setter
    def effective_period_type(self, value):
        self._effective_period_type = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.effective_period_num:
            if hasattr(self.effective_period_num, 'to_alipay_dict'):
                params['effective_period_num'] = self.effective_period_num.to_alipay_dict()
            else:
                params['effective_period_num'] = self.effective_period_num
        if self.effective_period_type:
            if hasattr(self.effective_period_type, 'to_alipay_dict'):
                params['effective_period_type'] = self.effective_period_type.to_alipay_dict()
            else:
                params['effective_period_type'] = self.effective_period_type
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPackage()
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'effective_period_num' in d:
            o.effective_period_num = d['effective_period_num']
        if 'effective_period_type' in d:
            o.effective_period_type = d['effective_period_type']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        return o


