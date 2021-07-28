#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinCustomerVerifycodeVerifyModel(object):

    def __init__(self):
        self._action = None
        self._biz_product = None
        self._destination = None
        self._verify_code = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.verify_code:
            if hasattr(self.verify_code, 'to_alipay_dict'):
                params['verify_code'] = self.verify_code.to_alipay_dict()
            else:
                params['verify_code'] = self.verify_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinCustomerVerifycodeVerifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'destination' in d:
            o.destination = d['destination']
        if 'verify_code' in d:
            o.verify_code = d['verify_code']
        return o


