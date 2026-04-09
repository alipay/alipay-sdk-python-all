#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheThird import RainyComplexTypesTheThird


class AlipaySecurityDataOpenidtestcaseRainytestQueryModel(object):

    def __init__(self):
        self._demo = None
        self._demo_price = None
        self._open_id = None
        self._openid_complex = None
        self._user_id = None

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, value):
        self._demo = value
    @property
    def demo_price(self):
        return self._demo_price

    @demo_price.setter
    def demo_price(self, value):
        self._demo_price = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def openid_complex(self):
        return self._openid_complex

    @openid_complex.setter
    def openid_complex(self, value):
        if isinstance(value, RainyComplexTypesTheThird):
            self._openid_complex = value
        else:
            self._openid_complex = RainyComplexTypesTheThird.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo:
            if hasattr(self.demo, 'to_alipay_dict'):
                params['demo'] = self.demo.to_alipay_dict()
            else:
                params['demo'] = self.demo
        if self.demo_price:
            if hasattr(self.demo_price, 'to_alipay_dict'):
                params['demo_price'] = self.demo_price.to_alipay_dict()
            else:
                params['demo_price'] = self.demo_price
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.openid_complex:
            if hasattr(self.openid_complex, 'to_alipay_dict'):
                params['openid_complex'] = self.openid_complex.to_alipay_dict()
            else:
                params['openid_complex'] = self.openid_complex
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataOpenidtestcaseRainytestQueryModel()
        if 'demo' in d:
            o.demo = d['demo']
        if 'demo_price' in d:
            o.demo_price = d['demo_price']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'openid_complex' in d:
            o.openid_complex = d['openid_complex']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


