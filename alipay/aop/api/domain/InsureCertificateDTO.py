#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsureCertificateDTO(object):

    def __init__(self):
        self._pre_order_id = None
        self._product_code = None
        self._quote_id = None
        self._recommend_flow_id = None

    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value
    @property
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsureCertificateDTO()
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        return o


