#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeAdvanceConsultModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._industry_product_code = None
        self._sub_merchant_id = None
        self._sub_merchant_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def industry_product_code(self):
        return self._industry_product_code

    @industry_product_code.setter
    def industry_product_code(self, value):
        self._industry_product_code = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def sub_merchant_type(self):
        return self._sub_merchant_type

    @sub_merchant_type.setter
    def sub_merchant_type(self, value):
        self._sub_merchant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.industry_product_code:
            if hasattr(self.industry_product_code, 'to_alipay_dict'):
                params['industry_product_code'] = self.industry_product_code.to_alipay_dict()
            else:
                params['industry_product_code'] = self.industry_product_code
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.sub_merchant_type:
            if hasattr(self.sub_merchant_type, 'to_alipay_dict'):
                params['sub_merchant_type'] = self.sub_merchant_type.to_alipay_dict()
            else:
                params['sub_merchant_type'] = self.sub_merchant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAdvanceConsultModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'industry_product_code' in d:
            o.industry_product_code = d['industry_product_code']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'sub_merchant_type' in d:
            o.sub_merchant_type = d['sub_merchant_type']
        return o


