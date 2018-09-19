#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityInitializeModel(object):

    def __init__(self):
        self._account_id = None
        self._account_name = None
        self._account_type = None
        self._biz_callback_url = None
        self._biz_id = None
        self._biz_params = None
        self._product_code = None
        self._scene_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def biz_callback_url(self):
        return self._biz_callback_url

    @biz_callback_url.setter
    def biz_callback_url(self, value):
        self._biz_callback_url = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_params(self):
        return self._biz_params

    @biz_params.setter
    def biz_params(self, value):
        self._biz_params = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.biz_callback_url:
            if hasattr(self.biz_callback_url, 'to_alipay_dict'):
                params['biz_callback_url'] = self.biz_callback_url.to_alipay_dict()
            else:
                params['biz_callback_url'] = self.biz_callback_url
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_params:
            if hasattr(self.biz_params, 'to_alipay_dict'):
                params['biz_params'] = self.biz_params.to_alipay_dict()
            else:
                params['biz_params'] = self.biz_params
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskVerifyidentityInitializeModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'biz_callback_url' in d:
            o.biz_callback_url = d['biz_callback_url']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_params' in d:
            o.biz_params = d['biz_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


