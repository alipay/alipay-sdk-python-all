#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterPaytradenoQueryModel(object):

    def __init__(self):
        self._channel = None
        self._currency = None
        self._isv_code = None
        self._nonce_str = None
        self._open_id = None
        self._out_order_id = None
        self._pay_prop = None
        self._pay_type = None
        self._platform_code = None
        self._scene_code = None
        self._time_stamp = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def nonce_str(self):
        return self._nonce_str

    @nonce_str.setter
    def nonce_str(self, value):
        self._nonce_str = value
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
    def pay_prop(self):
        return self._pay_prop

    @pay_prop.setter
    def pay_prop(self, value):
        self._pay_prop = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.nonce_str:
            if hasattr(self.nonce_str, 'to_alipay_dict'):
                params['nonce_str'] = self.nonce_str.to_alipay_dict()
            else:
                params['nonce_str'] = self.nonce_str
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
        if self.pay_prop:
            if hasattr(self.pay_prop, 'to_alipay_dict'):
                params['pay_prop'] = self.pay_prop.to_alipay_dict()
            else:
                params['pay_prop'] = self.pay_prop
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
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
        o = AlipayCommerceMedicalRegisterPaytradenoQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'currency' in d:
            o.currency = d['currency']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'nonce_str' in d:
            o.nonce_str = d['nonce_str']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'pay_prop' in d:
            o.pay_prop = d['pay_prop']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


