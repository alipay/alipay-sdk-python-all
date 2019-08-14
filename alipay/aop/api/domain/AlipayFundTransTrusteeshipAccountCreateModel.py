#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransTrusteeshipAccountCreateModel(object):

    def __init__(self):
        self._account_product_code = None
        self._account_scene_code = None
        self._alipay_user_id = None
        self._merchant_user_id = None
        self._merchant_user_type = None

    @property
    def account_product_code(self):
        return self._account_product_code

    @account_product_code.setter
    def account_product_code(self, value):
        self._account_product_code = value
    @property
    def account_scene_code(self):
        return self._account_scene_code

    @account_scene_code.setter
    def account_scene_code(self, value):
        self._account_scene_code = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
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
        if self.account_scene_code:
            if hasattr(self.account_scene_code, 'to_alipay_dict'):
                params['account_scene_code'] = self.account_scene_code.to_alipay_dict()
            else:
                params['account_scene_code'] = self.account_scene_code
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
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
        if 'account_scene_code' in d:
            o.account_scene_code = d['account_scene_code']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'merchant_user_type' in d:
            o.merchant_user_type = d['merchant_user_type']
        return o


