#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeCustomDisplayInfo import PrizeCustomDisplayInfo


class PrizeSendInfo(object):

    def __init__(self):
        self._gmt_create = None
        self._gmt_modified = None
        self._modulus = None
        self._open_id = None
        self._price = None
        self._prize_custom_display_info = None
        self._prize_id = None
        self._prize_name = None
        self._prize_type = None
        self._send_order_id = None
        self._user_id = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, value):
        self._modulus = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def prize_custom_display_info(self):
        return self._prize_custom_display_info

    @prize_custom_display_info.setter
    def prize_custom_display_info(self, value):
        if isinstance(value, PrizeCustomDisplayInfo):
            self._prize_custom_display_info = value
        else:
            self._prize_custom_display_info = PrizeCustomDisplayInfo.from_alipay_dict(value)
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.modulus:
            if hasattr(self.modulus, 'to_alipay_dict'):
                params['modulus'] = self.modulus.to_alipay_dict()
            else:
                params['modulus'] = self.modulus
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.prize_custom_display_info:
            if hasattr(self.prize_custom_display_info, 'to_alipay_dict'):
                params['prize_custom_display_info'] = self.prize_custom_display_info.to_alipay_dict()
            else:
                params['prize_custom_display_info'] = self.prize_custom_display_info
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
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
        o = PrizeSendInfo()
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'modulus' in d:
            o.modulus = d['modulus']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'price' in d:
            o.price = d['price']
        if 'prize_custom_display_info' in d:
            o.prize_custom_display_info = d['prize_custom_display_info']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


