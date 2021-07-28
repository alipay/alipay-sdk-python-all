#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransEntrustCloseModel(object):

    def __init__(self):
        self._biz_scene = None
        self._entrust_order_id = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def entrust_order_id(self):
        return self._entrust_order_id

    @entrust_order_id.setter
    def entrust_order_id(self, value):
        self._entrust_order_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.entrust_order_id:
            if hasattr(self.entrust_order_id, 'to_alipay_dict'):
                params['entrust_order_id'] = self.entrust_order_id.to_alipay_dict()
            else:
                params['entrust_order_id'] = self.entrust_order_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransEntrustCloseModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'entrust_order_id' in d:
            o.entrust_order_id = d['entrust_order_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


