#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeMerchantCreditQueryModel(object):

    def __init__(self):
        self._credit_scene = None
        self._merchant_credit_source = None
        self._merchant_user_id = None

    @property
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def merchant_credit_source(self):
        return self._merchant_credit_source

    @merchant_credit_source.setter
    def merchant_credit_source(self, value):
        self._merchant_credit_source = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_scene:
            if hasattr(self.credit_scene, 'to_alipay_dict'):
                params['credit_scene'] = self.credit_scene.to_alipay_dict()
            else:
                params['credit_scene'] = self.credit_scene
        if self.merchant_credit_source:
            if hasattr(self.merchant_credit_source, 'to_alipay_dict'):
                params['merchant_credit_source'] = self.merchant_credit_source.to_alipay_dict()
            else:
                params['merchant_credit_source'] = self.merchant_credit_source
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
        o = AlipayTradeMerchantCreditQueryModel()
        if 'credit_scene' in d:
            o.credit_scene = d['credit_scene']
        if 'merchant_credit_source' in d:
            o.merchant_credit_source = d['merchant_credit_source']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        return o


