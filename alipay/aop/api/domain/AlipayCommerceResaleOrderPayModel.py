#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ResalePayInfoVO import ResalePayInfoVO


class AlipayCommerceResaleOrderPayModel(object):

    def __init__(self):
        self._open_id = None
        self._out_order_id = None
        self._out_pay_id = None
        self._pay_amount = None
        self._pay_amount_type = None
        self._pay_memo = None
        self._pay_scene_items = None
        self._pay_tool = None
        self._pay_type = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_pay_id(self):
        return self._out_pay_id

    @out_pay_id.setter
    def out_pay_id(self, value):
        self._out_pay_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_amount_type(self):
        return self._pay_amount_type

    @pay_amount_type.setter
    def pay_amount_type(self, value):
        self._pay_amount_type = value
    @property
    def pay_memo(self):
        return self._pay_memo

    @pay_memo.setter
    def pay_memo(self, value):
        self._pay_memo = value
    @property
    def pay_scene_items(self):
        return self._pay_scene_items

    @pay_scene_items.setter
    def pay_scene_items(self, value):
        if isinstance(value, list):
            self._pay_scene_items = list()
            for i in value:
                if isinstance(i, ResalePayInfoVO):
                    self._pay_scene_items.append(i)
                else:
                    self._pay_scene_items.append(ResalePayInfoVO.from_alipay_dict(i))
    @property
    def pay_tool(self):
        return self._pay_tool

    @pay_tool.setter
    def pay_tool(self, value):
        self._pay_tool = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_pay_id:
            if hasattr(self.out_pay_id, 'to_alipay_dict'):
                params['out_pay_id'] = self.out_pay_id.to_alipay_dict()
            else:
                params['out_pay_id'] = self.out_pay_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_amount_type:
            if hasattr(self.pay_amount_type, 'to_alipay_dict'):
                params['pay_amount_type'] = self.pay_amount_type.to_alipay_dict()
            else:
                params['pay_amount_type'] = self.pay_amount_type
        if self.pay_memo:
            if hasattr(self.pay_memo, 'to_alipay_dict'):
                params['pay_memo'] = self.pay_memo.to_alipay_dict()
            else:
                params['pay_memo'] = self.pay_memo
        if self.pay_scene_items:
            if isinstance(self.pay_scene_items, list):
                for i in range(0, len(self.pay_scene_items)):
                    element = self.pay_scene_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_scene_items[i] = element.to_alipay_dict()
            if hasattr(self.pay_scene_items, 'to_alipay_dict'):
                params['pay_scene_items'] = self.pay_scene_items.to_alipay_dict()
            else:
                params['pay_scene_items'] = self.pay_scene_items
        if self.pay_tool:
            if hasattr(self.pay_tool, 'to_alipay_dict'):
                params['pay_tool'] = self.pay_tool.to_alipay_dict()
            else:
                params['pay_tool'] = self.pay_tool
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
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
        o = AlipayCommerceResaleOrderPayModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_pay_id' in d:
            o.out_pay_id = d['out_pay_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_amount_type' in d:
            o.pay_amount_type = d['pay_amount_type']
        if 'pay_memo' in d:
            o.pay_memo = d['pay_memo']
        if 'pay_scene_items' in d:
            o.pay_scene_items = d['pay_scene_items']
        if 'pay_tool' in d:
            o.pay_tool = d['pay_tool']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


