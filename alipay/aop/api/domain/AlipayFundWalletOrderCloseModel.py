#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletOrderCloseModel(object):

    def __init__(self):
        self._biz_scene = None
        self._close_reason = None
        self._fund_order_id = None
        self._product_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def close_reason(self):
        return self._close_reason

    @close_reason.setter
    def close_reason(self, value):
        self._close_reason = value
    @property
    def fund_order_id(self):
        return self._fund_order_id

    @fund_order_id.setter
    def fund_order_id(self, value):
        self._fund_order_id = value
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
        if self.close_reason:
            if hasattr(self.close_reason, 'to_alipay_dict'):
                params['close_reason'] = self.close_reason.to_alipay_dict()
            else:
                params['close_reason'] = self.close_reason
        if self.fund_order_id:
            if hasattr(self.fund_order_id, 'to_alipay_dict'):
                params['fund_order_id'] = self.fund_order_id.to_alipay_dict()
            else:
                params['fund_order_id'] = self.fund_order_id
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
        o = AlipayFundWalletOrderCloseModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'close_reason' in d:
            o.close_reason = d['close_reason']
        if 'fund_order_id' in d:
            o.fund_order_id = d['fund_order_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


