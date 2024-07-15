#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayInfoDTO(object):

    def __init__(self):
        self._disable_pay_channels = None
        self._enable_pay_channels = None
        self._payment_biz_type = None
        self._payment_method = None

    @property
    def disable_pay_channels(self):
        return self._disable_pay_channels

    @disable_pay_channels.setter
    def disable_pay_channels(self, value):
        self._disable_pay_channels = value
    @property
    def enable_pay_channels(self):
        return self._enable_pay_channels

    @enable_pay_channels.setter
    def enable_pay_channels(self, value):
        self._enable_pay_channels = value
    @property
    def payment_biz_type(self):
        return self._payment_biz_type

    @payment_biz_type.setter
    def payment_biz_type(self, value):
        self._payment_biz_type = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.disable_pay_channels:
            if hasattr(self.disable_pay_channels, 'to_alipay_dict'):
                params['disable_pay_channels'] = self.disable_pay_channels.to_alipay_dict()
            else:
                params['disable_pay_channels'] = self.disable_pay_channels
        if self.enable_pay_channels:
            if hasattr(self.enable_pay_channels, 'to_alipay_dict'):
                params['enable_pay_channels'] = self.enable_pay_channels.to_alipay_dict()
            else:
                params['enable_pay_channels'] = self.enable_pay_channels
        if self.payment_biz_type:
            if hasattr(self.payment_biz_type, 'to_alipay_dict'):
                params['payment_biz_type'] = self.payment_biz_type.to_alipay_dict()
            else:
                params['payment_biz_type'] = self.payment_biz_type
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayInfoDTO()
        if 'disable_pay_channels' in d:
            o.disable_pay_channels = d['disable_pay_channels']
        if 'enable_pay_channels' in d:
            o.enable_pay_channels = d['enable_pay_channels']
        if 'payment_biz_type' in d:
            o.payment_biz_type = d['payment_biz_type']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        return o


