#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceResaleOrderSignModel(object):

    def __init__(self):
        self._callback_url = None
        self._open_id = None
        self._out_order_id = None
        self._sign_pay_type = None
        self._user_id = None

    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
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
    def sign_pay_type(self):
        return self._sign_pay_type

    @sign_pay_type.setter
    def sign_pay_type(self, value):
        self._sign_pay_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
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
        if self.sign_pay_type:
            if hasattr(self.sign_pay_type, 'to_alipay_dict'):
                params['sign_pay_type'] = self.sign_pay_type.to_alipay_dict()
            else:
                params['sign_pay_type'] = self.sign_pay_type
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
        o = AlipayCommerceResaleOrderSignModel()
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'sign_pay_type' in d:
            o.sign_pay_type = d['sign_pay_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


