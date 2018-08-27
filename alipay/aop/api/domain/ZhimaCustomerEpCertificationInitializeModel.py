#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerEpCertificationInitializeModel(object):

    def __init__(self):
        self._biz_code = None
        self._ext_biz_param = None
        self._identity_param = None
        self._merchant_config = None
        self._product_code = None
        self._transaction_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def ext_biz_param(self):
        return self._ext_biz_param

    @ext_biz_param.setter
    def ext_biz_param(self, value):
        self._ext_biz_param = value
    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        self._identity_param = value
    @property
    def merchant_config(self):
        return self._merchant_config

    @merchant_config.setter
    def merchant_config(self, value):
        self._merchant_config = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.ext_biz_param:
            if hasattr(self.ext_biz_param, 'to_alipay_dict'):
                params['ext_biz_param'] = self.ext_biz_param.to_alipay_dict()
            else:
                params['ext_biz_param'] = self.ext_biz_param
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        if self.merchant_config:
            if hasattr(self.merchant_config, 'to_alipay_dict'):
                params['merchant_config'] = self.merchant_config.to_alipay_dict()
            else:
                params['merchant_config'] = self.merchant_config
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
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
        o = ZhimaCustomerEpCertificationInitializeModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'ext_biz_param' in d:
            o.ext_biz_param = d['ext_biz_param']
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        if 'merchant_config' in d:
            o.merchant_config = d['merchant_config']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


