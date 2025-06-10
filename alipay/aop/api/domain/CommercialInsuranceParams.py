#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommercialInsuranceParams(object):

    def __init__(self):
        self._insure_channel_code = None
        self._insure_product_name = None
        self._merchant_no = None
        self._terminal_no = None

    @property
    def insure_channel_code(self):
        return self._insure_channel_code

    @insure_channel_code.setter
    def insure_channel_code(self, value):
        self._insure_channel_code = value
    @property
    def insure_product_name(self):
        return self._insure_product_name

    @insure_product_name.setter
    def insure_product_name(self, value):
        self._insure_product_name = value
    @property
    def merchant_no(self):
        return self._merchant_no

    @merchant_no.setter
    def merchant_no(self, value):
        self._merchant_no = value
    @property
    def terminal_no(self):
        return self._terminal_no

    @terminal_no.setter
    def terminal_no(self, value):
        self._terminal_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.insure_channel_code:
            if hasattr(self.insure_channel_code, 'to_alipay_dict'):
                params['insure_channel_code'] = self.insure_channel_code.to_alipay_dict()
            else:
                params['insure_channel_code'] = self.insure_channel_code
        if self.insure_product_name:
            if hasattr(self.insure_product_name, 'to_alipay_dict'):
                params['insure_product_name'] = self.insure_product_name.to_alipay_dict()
            else:
                params['insure_product_name'] = self.insure_product_name
        if self.merchant_no:
            if hasattr(self.merchant_no, 'to_alipay_dict'):
                params['merchant_no'] = self.merchant_no.to_alipay_dict()
            else:
                params['merchant_no'] = self.merchant_no
        if self.terminal_no:
            if hasattr(self.terminal_no, 'to_alipay_dict'):
                params['terminal_no'] = self.terminal_no.to_alipay_dict()
            else:
                params['terminal_no'] = self.terminal_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommercialInsuranceParams()
        if 'insure_channel_code' in d:
            o.insure_channel_code = d['insure_channel_code']
        if 'insure_product_name' in d:
            o.insure_product_name = d['insure_product_name']
        if 'merchant_no' in d:
            o.merchant_no = d['merchant_no']
        if 'terminal_no' in d:
            o.terminal_no = d['terminal_no']
        return o


