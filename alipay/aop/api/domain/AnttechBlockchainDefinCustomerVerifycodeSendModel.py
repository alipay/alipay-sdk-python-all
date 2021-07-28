#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinCustomerVerifycodeSendModel(object):

    def __init__(self):
        self._action = None
        self._biz_product = None
        self._destination = None
        self._template_code = None
        self._type = None

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
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


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
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinCustomerVerifycodeSendModel()
        if 'action' in d:
            o.action = d['action']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'destination' in d:
            o.destination = d['destination']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'type' in d:
            o.type = d['type']
        return o


