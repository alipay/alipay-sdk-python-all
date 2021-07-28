#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceMerchantEnterstatusQueryModel(object):

    def __init__(self):
        self._m_short_name = None
        self._process_id = None
        self._product_code = None

    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceMerchantEnterstatusQueryModel()
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


