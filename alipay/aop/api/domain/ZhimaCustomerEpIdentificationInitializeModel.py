#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerEpIdentificationInitializeModel(object):

    def __init__(self):
        self._certify_mode = None
        self._identity_param = None
        self._merchant_url = None
        self._product_code = None
        self._scene_code = None
        self._transaction_id = None

    @property
    def certify_mode(self):
        return self._certify_mode

    @certify_mode.setter
    def certify_mode(self, value):
        self._certify_mode = value
    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        self._identity_param = value
    @property
    def merchant_url(self):
        return self._merchant_url

    @merchant_url.setter
    def merchant_url(self, value):
        self._merchant_url = value
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
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_mode:
            if hasattr(self.certify_mode, 'to_alipay_dict'):
                params['certify_mode'] = self.certify_mode.to_alipay_dict()
            else:
                params['certify_mode'] = self.certify_mode
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        if self.merchant_url:
            if hasattr(self.merchant_url, 'to_alipay_dict'):
                params['merchant_url'] = self.merchant_url.to_alipay_dict()
            else:
                params['merchant_url'] = self.merchant_url
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
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerEpIdentificationInitializeModel()
        if 'certify_mode' in d:
            o.certify_mode = d['certify_mode']
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        if 'merchant_url' in d:
            o.merchant_url = d['merchant_url']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


