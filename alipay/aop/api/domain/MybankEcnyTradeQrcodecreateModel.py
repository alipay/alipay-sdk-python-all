#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyTradeQrcodecreateModel(object):

    def __init__(self):
        self._amount = None
        self._attach_params = None
        self._extend_params = None
        self._merchant_id = None
        self._scene = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def attach_params(self):
        return self._attach_params

    @attach_params.setter
    def attach_params(self, value):
        self._attach_params = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.attach_params:
            if hasattr(self.attach_params, 'to_alipay_dict'):
                params['attach_params'] = self.attach_params.to_alipay_dict()
            else:
                params['attach_params'] = self.attach_params
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyTradeQrcodecreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'attach_params' in d:
            o.attach_params = d['attach_params']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'scene' in d:
            o.scene = d['scene']
        return o


