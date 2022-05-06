#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossRelatedCompanyConsultModel(object):

    def __init__(self):
        self._biz_time_in_mills = None
        self._is_whole_month_valid = None
        self._type = None
        self._value = None

    @property
    def biz_time_in_mills(self):
        return self._biz_time_in_mills

    @biz_time_in_mills.setter
    def biz_time_in_mills(self, value):
        self._biz_time_in_mills = value
    @property
    def is_whole_month_valid(self):
        return self._is_whole_month_valid

    @is_whole_month_valid.setter
    def is_whole_month_valid(self, value):
        self._is_whole_month_valid = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time_in_mills:
            if hasattr(self.biz_time_in_mills, 'to_alipay_dict'):
                params['biz_time_in_mills'] = self.biz_time_in_mills.to_alipay_dict()
            else:
                params['biz_time_in_mills'] = self.biz_time_in_mills
        if self.is_whole_month_valid:
            if hasattr(self.is_whole_month_valid, 'to_alipay_dict'):
                params['is_whole_month_valid'] = self.is_whole_month_valid.to_alipay_dict()
            else:
                params['is_whole_month_valid'] = self.is_whole_month_valid
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossRelatedCompanyConsultModel()
        if 'biz_time_in_mills' in d:
            o.biz_time_in_mills = d['biz_time_in_mills']
        if 'is_whole_month_valid' in d:
            o.is_whole_month_valid = d['is_whole_month_valid']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


