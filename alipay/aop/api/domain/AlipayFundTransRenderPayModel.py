#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransRenderPayModel(object):

    def __init__(self):
        self._biz_scene = None
        self._expire_time = None
        self._initialize_code_type = None
        self._order_id = None
        self._product_code = None
        self._target_terminal_type = None

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
    def initialize_code_type(self):
        return self._initialize_code_type

    @initialize_code_type.setter
    def initialize_code_type(self, value):
        self._initialize_code_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def target_terminal_type(self):
        return self._target_terminal_type

    @target_terminal_type.setter
    def target_terminal_type(self, value):
        self._target_terminal_type = value


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
        if self.initialize_code_type:
            if hasattr(self.initialize_code_type, 'to_alipay_dict'):
                params['initialize_code_type'] = self.initialize_code_type.to_alipay_dict()
            else:
                params['initialize_code_type'] = self.initialize_code_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.target_terminal_type:
            if hasattr(self.target_terminal_type, 'to_alipay_dict'):
                params['target_terminal_type'] = self.target_terminal_type.to_alipay_dict()
            else:
                params['target_terminal_type'] = self.target_terminal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransRenderPayModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'initialize_code_type' in d:
            o.initialize_code_type = d['initialize_code_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'target_terminal_type' in d:
            o.target_terminal_type = d['target_terminal_type']
        return o


