#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundRuleDetail(object):

    def __init__(self):
        self._absolute_date = None
        self._deduct_base_type = None
        self._deduct_percent = None
        self._relative_date_type = None
        self._relative_minute = None

    @property
    def absolute_date(self):
        return self._absolute_date

    @absolute_date.setter
    def absolute_date(self, value):
        self._absolute_date = value
    @property
    def deduct_base_type(self):
        return self._deduct_base_type

    @deduct_base_type.setter
    def deduct_base_type(self, value):
        self._deduct_base_type = value
    @property
    def deduct_percent(self):
        return self._deduct_percent

    @deduct_percent.setter
    def deduct_percent(self, value):
        self._deduct_percent = value
    @property
    def relative_date_type(self):
        return self._relative_date_type

    @relative_date_type.setter
    def relative_date_type(self, value):
        self._relative_date_type = value
    @property
    def relative_minute(self):
        return self._relative_minute

    @relative_minute.setter
    def relative_minute(self, value):
        self._relative_minute = value


    def to_alipay_dict(self):
        params = dict()
        if self.absolute_date:
            if hasattr(self.absolute_date, 'to_alipay_dict'):
                params['absolute_date'] = self.absolute_date.to_alipay_dict()
            else:
                params['absolute_date'] = self.absolute_date
        if self.deduct_base_type:
            if hasattr(self.deduct_base_type, 'to_alipay_dict'):
                params['deduct_base_type'] = self.deduct_base_type.to_alipay_dict()
            else:
                params['deduct_base_type'] = self.deduct_base_type
        if self.deduct_percent:
            if hasattr(self.deduct_percent, 'to_alipay_dict'):
                params['deduct_percent'] = self.deduct_percent.to_alipay_dict()
            else:
                params['deduct_percent'] = self.deduct_percent
        if self.relative_date_type:
            if hasattr(self.relative_date_type, 'to_alipay_dict'):
                params['relative_date_type'] = self.relative_date_type.to_alipay_dict()
            else:
                params['relative_date_type'] = self.relative_date_type
        if self.relative_minute:
            if hasattr(self.relative_minute, 'to_alipay_dict'):
                params['relative_minute'] = self.relative_minute.to_alipay_dict()
            else:
                params['relative_minute'] = self.relative_minute
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundRuleDetail()
        if 'absolute_date' in d:
            o.absolute_date = d['absolute_date']
        if 'deduct_base_type' in d:
            o.deduct_base_type = d['deduct_base_type']
        if 'deduct_percent' in d:
            o.deduct_percent = d['deduct_percent']
        if 'relative_date_type' in d:
            o.relative_date_type = d['relative_date_type']
        if 'relative_minute' in d:
            o.relative_minute = d['relative_minute']
        return o


