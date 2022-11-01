#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundZcardprodMerchantSignModel(object):

    def __init__(self):
        self._account_name = None
        self._biz_scene_code = None
        self._biz_scene_id = None
        self._business_params = None
        self._product_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
    @property
    def biz_scene_id(self):
        return self._biz_scene_id

    @biz_scene_id.setter
    def biz_scene_id(self, value):
        self._biz_scene_id = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.biz_scene_code:
            if hasattr(self.biz_scene_code, 'to_alipay_dict'):
                params['biz_scene_code'] = self.biz_scene_code.to_alipay_dict()
            else:
                params['biz_scene_code'] = self.biz_scene_code
        if self.biz_scene_id:
            if hasattr(self.biz_scene_id, 'to_alipay_dict'):
                params['biz_scene_id'] = self.biz_scene_id.to_alipay_dict()
            else:
                params['biz_scene_id'] = self.biz_scene_id
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
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
        o = AlipayFundZcardprodMerchantSignModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'biz_scene_code' in d:
            o.biz_scene_code = d['biz_scene_code']
        if 'biz_scene_id' in d:
            o.biz_scene_id = d['biz_scene_id']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


