#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclingScrappedTaxCalcItem(object):

    def __init__(self):
        self._reduction_ratio = None
        self._tax_item_code = None
        self._tax_item_name = None
        self._tax_project_code = None
        self._tax_project_name = None
        self._tax_rate = None

    @property
    def reduction_ratio(self):
        return self._reduction_ratio

    @reduction_ratio.setter
    def reduction_ratio(self, value):
        self._reduction_ratio = value
    @property
    def tax_item_code(self):
        return self._tax_item_code

    @tax_item_code.setter
    def tax_item_code(self, value):
        self._tax_item_code = value
    @property
    def tax_item_name(self):
        return self._tax_item_name

    @tax_item_name.setter
    def tax_item_name(self, value):
        self._tax_item_name = value
    @property
    def tax_project_code(self):
        return self._tax_project_code

    @tax_project_code.setter
    def tax_project_code(self, value):
        self._tax_project_code = value
    @property
    def tax_project_name(self):
        return self._tax_project_name

    @tax_project_name.setter
    def tax_project_name(self, value):
        self._tax_project_name = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.reduction_ratio:
            if hasattr(self.reduction_ratio, 'to_alipay_dict'):
                params['reduction_ratio'] = self.reduction_ratio.to_alipay_dict()
            else:
                params['reduction_ratio'] = self.reduction_ratio
        if self.tax_item_code:
            if hasattr(self.tax_item_code, 'to_alipay_dict'):
                params['tax_item_code'] = self.tax_item_code.to_alipay_dict()
            else:
                params['tax_item_code'] = self.tax_item_code
        if self.tax_item_name:
            if hasattr(self.tax_item_name, 'to_alipay_dict'):
                params['tax_item_name'] = self.tax_item_name.to_alipay_dict()
            else:
                params['tax_item_name'] = self.tax_item_name
        if self.tax_project_code:
            if hasattr(self.tax_project_code, 'to_alipay_dict'):
                params['tax_project_code'] = self.tax_project_code.to_alipay_dict()
            else:
                params['tax_project_code'] = self.tax_project_code
        if self.tax_project_name:
            if hasattr(self.tax_project_name, 'to_alipay_dict'):
                params['tax_project_name'] = self.tax_project_name.to_alipay_dict()
            else:
                params['tax_project_name'] = self.tax_project_name
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecyclingScrappedTaxCalcItem()
        if 'reduction_ratio' in d:
            o.reduction_ratio = d['reduction_ratio']
        if 'tax_item_code' in d:
            o.tax_item_code = d['tax_item_code']
        if 'tax_item_name' in d:
            o.tax_item_name = d['tax_item_name']
        if 'tax_project_code' in d:
            o.tax_project_code = d['tax_project_code']
        if 'tax_project_name' in d:
            o.tax_project_name = d['tax_project_name']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


