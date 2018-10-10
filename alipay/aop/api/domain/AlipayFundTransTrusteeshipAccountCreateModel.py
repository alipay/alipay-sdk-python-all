#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransTrusteeshipAccountCreateModel(object):

    def __init__(self):
        self._account_product_code = None
        self._merchant_user_id = None
        self._merchant_user_type = None

    @property
    def account_product_code(self):
        return self._account_product_code

    @account_product_code.setter
    def account_product_code(self, value):
        self._account_product_code = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def merchant_user_type(self):
        return self._merchant_user_type

    @merchant_user_type.setter
    def merchant_user_type(self, value):
        self._merchant_user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_product_code:
            if hasattr(self.account_product_code, 'to_alipay_dict'):
                params['account_product_code'] = self.account_product_code.to_alipay_dict()
            else:
                params['account_product_code'] = self.account_product_code
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.merchant_user_type:
            if hasattr(self.merchant_user_type, 'to_alipay_dict'):
                params['merchant_user_type'] = self.merchant_user_type.to_alipay_dict()
            else:
                params['merchant_user_type'] = self.merchant_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransTrusteeshipAccountCreateModel()
        if 'account_product_code' in d:
            o.account_product_code = d['account_product_code']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'merchant_user_type' in d:
            o.merchant_user_type = d['merchant_user_type']
        return o


