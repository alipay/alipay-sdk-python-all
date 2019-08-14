#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAccountQueryModel(object):

    def __init__(self):
        self._account_product_code = None
        self._account_scene_code = None
        self._account_type = None
        self._alipay_user_id = None
        self._ext_info = None
        self._merchant_user_id = None

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
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value


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
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAccountQueryModel()
        if 'account_product_code' in d:
            o.account_product_code = d['account_product_code']
        if 'account_scene_code' in d:
            o.account_scene_code = d['account_scene_code']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        return o


