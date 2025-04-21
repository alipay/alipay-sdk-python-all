#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundJointaccountTokenGenerateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._expire_time = None
        self._product_code = None
        self._token_key = None
        self._token_value = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def token_key(self):
        return self._token_key

    @token_key.setter
    def token_key(self, value):
        self._token_key = value
    @property
    def token_value(self):
        return self._token_value

    @token_value.setter
    def token_value(self, value):
        self._token_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.token_key:
            if hasattr(self.token_key, 'to_alipay_dict'):
                params['token_key'] = self.token_key.to_alipay_dict()
            else:
                params['token_key'] = self.token_key
        if self.token_value:
            if hasattr(self.token_value, 'to_alipay_dict'):
                params['token_value'] = self.token_value.to_alipay_dict()
            else:
                params['token_value'] = self.token_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountTokenGenerateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'token_key' in d:
            o.token_key = d['token_key']
        if 'token_value' in d:
            o.token_value = d['token_value']
        return o


