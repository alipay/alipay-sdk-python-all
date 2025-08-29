#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentRoyaltyEarlyBuyModel(object):

    def __init__(self):
        self._execute_scene = None
        self._invest_id = None
        self._operator = None
        self._order_list = None
        self._seller_id = None

    @property
    def execute_scene(self):
        return self._execute_scene

    @execute_scene.setter
    def execute_scene(self, value):
        self._execute_scene = value
    @property
    def invest_id(self):
        return self._invest_id

    @invest_id.setter
    def invest_id(self, value):
        self._invest_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                self._order_list.append(i)
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.execute_scene:
            if hasattr(self.execute_scene, 'to_alipay_dict'):
                params['execute_scene'] = self.execute_scene.to_alipay_dict()
            else:
                params['execute_scene'] = self.execute_scene
        if self.invest_id:
            if hasattr(self.invest_id, 'to_alipay_dict'):
                params['invest_id'] = self.invest_id.to_alipay_dict()
            else:
                params['invest_id'] = self.invest_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.order_list:
            if isinstance(self.order_list, list):
                for i in range(0, len(self.order_list)):
                    element = self.order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_list[i] = element.to_alipay_dict()
            if hasattr(self.order_list, 'to_alipay_dict'):
                params['order_list'] = self.order_list.to_alipay_dict()
            else:
                params['order_list'] = self.order_list
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentRoyaltyEarlyBuyModel()
        if 'execute_scene' in d:
            o.execute_scene = d['execute_scene']
        if 'invest_id' in d:
            o.invest_id = d['invest_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'order_list' in d:
            o.order_list = d['order_list']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        return o


