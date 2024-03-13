#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniOrderExtInfoDTO(object):

    def __init__(self):
        self._addition_rebate_base_price = None
        self._deduct_sign_scene = None
        self._door_time = None
        self._order_str = None
        self._order_trade_type = None
        self._trade_no = None

    @property
    def addition_rebate_base_price(self):
        return self._addition_rebate_base_price

    @addition_rebate_base_price.setter
    def addition_rebate_base_price(self, value):
        self._addition_rebate_base_price = value
    @property
    def deduct_sign_scene(self):
        return self._deduct_sign_scene

    @deduct_sign_scene.setter
    def deduct_sign_scene(self, value):
        self._deduct_sign_scene = value
    @property
    def door_time(self):
        return self._door_time

    @door_time.setter
    def door_time(self, value):
        self._door_time = value
    @property
    def order_str(self):
        return self._order_str

    @order_str.setter
    def order_str(self, value):
        self._order_str = value
    @property
    def order_trade_type(self):
        return self._order_trade_type

    @order_trade_type.setter
    def order_trade_type(self, value):
        self._order_trade_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.addition_rebate_base_price:
            if hasattr(self.addition_rebate_base_price, 'to_alipay_dict'):
                params['addition_rebate_base_price'] = self.addition_rebate_base_price.to_alipay_dict()
            else:
                params['addition_rebate_base_price'] = self.addition_rebate_base_price
        if self.deduct_sign_scene:
            if hasattr(self.deduct_sign_scene, 'to_alipay_dict'):
                params['deduct_sign_scene'] = self.deduct_sign_scene.to_alipay_dict()
            else:
                params['deduct_sign_scene'] = self.deduct_sign_scene
        if self.door_time:
            if hasattr(self.door_time, 'to_alipay_dict'):
                params['door_time'] = self.door_time.to_alipay_dict()
            else:
                params['door_time'] = self.door_time
        if self.order_str:
            if hasattr(self.order_str, 'to_alipay_dict'):
                params['order_str'] = self.order_str.to_alipay_dict()
            else:
                params['order_str'] = self.order_str
        if self.order_trade_type:
            if hasattr(self.order_trade_type, 'to_alipay_dict'):
                params['order_trade_type'] = self.order_trade_type.to_alipay_dict()
            else:
                params['order_trade_type'] = self.order_trade_type
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniOrderExtInfoDTO()
        if 'addition_rebate_base_price' in d:
            o.addition_rebate_base_price = d['addition_rebate_base_price']
        if 'deduct_sign_scene' in d:
            o.deduct_sign_scene = d['deduct_sign_scene']
        if 'door_time' in d:
            o.door_time = d['door_time']
        if 'order_str' in d:
            o.order_str = d['order_str']
        if 'order_trade_type' in d:
            o.order_trade_type = d['order_trade_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


