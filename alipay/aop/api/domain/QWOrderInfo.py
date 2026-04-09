#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QWOrderInfo(object):

    def __init__(self):
        self._alipay_user_id = None
        self._open_id = None
        self._qianwen_mutex_asset_type = None
        self._qianwen_order_category = None
        self._qianwen_order_pay_amount = None
        self._qianwen_order_type = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def qianwen_mutex_asset_type(self):
        return self._qianwen_mutex_asset_type

    @qianwen_mutex_asset_type.setter
    def qianwen_mutex_asset_type(self, value):
        self._qianwen_mutex_asset_type = value
    @property
    def qianwen_order_category(self):
        return self._qianwen_order_category

    @qianwen_order_category.setter
    def qianwen_order_category(self, value):
        self._qianwen_order_category = value
    @property
    def qianwen_order_pay_amount(self):
        return self._qianwen_order_pay_amount

    @qianwen_order_pay_amount.setter
    def qianwen_order_pay_amount(self, value):
        self._qianwen_order_pay_amount = value
    @property
    def qianwen_order_type(self):
        return self._qianwen_order_type

    @qianwen_order_type.setter
    def qianwen_order_type(self, value):
        self._qianwen_order_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.qianwen_mutex_asset_type:
            if hasattr(self.qianwen_mutex_asset_type, 'to_alipay_dict'):
                params['qianwen_mutex_asset_type'] = self.qianwen_mutex_asset_type.to_alipay_dict()
            else:
                params['qianwen_mutex_asset_type'] = self.qianwen_mutex_asset_type
        if self.qianwen_order_category:
            if hasattr(self.qianwen_order_category, 'to_alipay_dict'):
                params['qianwen_order_category'] = self.qianwen_order_category.to_alipay_dict()
            else:
                params['qianwen_order_category'] = self.qianwen_order_category
        if self.qianwen_order_pay_amount:
            if hasattr(self.qianwen_order_pay_amount, 'to_alipay_dict'):
                params['qianwen_order_pay_amount'] = self.qianwen_order_pay_amount.to_alipay_dict()
            else:
                params['qianwen_order_pay_amount'] = self.qianwen_order_pay_amount
        if self.qianwen_order_type:
            if hasattr(self.qianwen_order_type, 'to_alipay_dict'):
                params['qianwen_order_type'] = self.qianwen_order_type.to_alipay_dict()
            else:
                params['qianwen_order_type'] = self.qianwen_order_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QWOrderInfo()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'qianwen_mutex_asset_type' in d:
            o.qianwen_mutex_asset_type = d['qianwen_mutex_asset_type']
        if 'qianwen_order_category' in d:
            o.qianwen_order_category = d['qianwen_order_category']
        if 'qianwen_order_pay_amount' in d:
            o.qianwen_order_pay_amount = d['qianwen_order_pay_amount']
        if 'qianwen_order_type' in d:
            o.qianwen_order_type = d['qianwen_order_type']
        return o


