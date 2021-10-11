#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemConsultRequest import ItemConsultRequest


class AlipayCommerceVoucherResultConsultModel(object):

    def __init__(self):
        self._isv_pid = None
        self._item_consult_list = None
        self._merchant_pid = None
        self._order_amount = None
        self._scene_code = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def item_consult_list(self):
        return self._item_consult_list

    @item_consult_list.setter
    def item_consult_list(self, value):
        if isinstance(value, ItemConsultRequest):
            self._item_consult_list = value
        else:
            self._item_consult_list = ItemConsultRequest.from_alipay_dict(value)
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.item_consult_list:
            if hasattr(self.item_consult_list, 'to_alipay_dict'):
                params['item_consult_list'] = self.item_consult_list.to_alipay_dict()
            else:
                params['item_consult_list'] = self.item_consult_list
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceVoucherResultConsultModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'item_consult_list' in d:
            o.item_consult_list = d['item_consult_list']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


