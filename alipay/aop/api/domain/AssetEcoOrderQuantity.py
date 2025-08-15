#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetEcoOrderQuantity(object):

    def __init__(self):
        self._eco_code = None
        self._eco_name = None
        self._eco_nfc_order_count = None
        self._eco_order_count = None
        self._sales_model = None
        self._statistical_date = None

    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def eco_name(self):
        return self._eco_name

    @eco_name.setter
    def eco_name(self, value):
        self._eco_name = value
    @property
    def eco_nfc_order_count(self):
        return self._eco_nfc_order_count

    @eco_nfc_order_count.setter
    def eco_nfc_order_count(self, value):
        self._eco_nfc_order_count = value
    @property
    def eco_order_count(self):
        return self._eco_order_count

    @eco_order_count.setter
    def eco_order_count(self, value):
        self._eco_order_count = value
    @property
    def sales_model(self):
        return self._sales_model

    @sales_model.setter
    def sales_model(self, value):
        self._sales_model = value
    @property
    def statistical_date(self):
        return self._statistical_date

    @statistical_date.setter
    def statistical_date(self, value):
        self._statistical_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.eco_name:
            if hasattr(self.eco_name, 'to_alipay_dict'):
                params['eco_name'] = self.eco_name.to_alipay_dict()
            else:
                params['eco_name'] = self.eco_name
        if self.eco_nfc_order_count:
            if hasattr(self.eco_nfc_order_count, 'to_alipay_dict'):
                params['eco_nfc_order_count'] = self.eco_nfc_order_count.to_alipay_dict()
            else:
                params['eco_nfc_order_count'] = self.eco_nfc_order_count
        if self.eco_order_count:
            if hasattr(self.eco_order_count, 'to_alipay_dict'):
                params['eco_order_count'] = self.eco_order_count.to_alipay_dict()
            else:
                params['eco_order_count'] = self.eco_order_count
        if self.sales_model:
            if hasattr(self.sales_model, 'to_alipay_dict'):
                params['sales_model'] = self.sales_model.to_alipay_dict()
            else:
                params['sales_model'] = self.sales_model
        if self.statistical_date:
            if hasattr(self.statistical_date, 'to_alipay_dict'):
                params['statistical_date'] = self.statistical_date.to_alipay_dict()
            else:
                params['statistical_date'] = self.statistical_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetEcoOrderQuantity()
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'eco_name' in d:
            o.eco_name = d['eco_name']
        if 'eco_nfc_order_count' in d:
            o.eco_nfc_order_count = d['eco_nfc_order_count']
        if 'eco_order_count' in d:
            o.eco_order_count = d['eco_order_count']
        if 'sales_model' in d:
            o.sales_model = d['sales_model']
        if 'statistical_date' in d:
            o.statistical_date = d['statistical_date']
        return o


