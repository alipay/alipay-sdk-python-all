#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiserviceSmartpriceGetModel(object):

    def __init__(self):
        self._base_price_cent = None
        self._channel = None
        self._city_code = None
        self._default_promo_price_cent = None
        self._from = None
        self._high_price_cent = None
        self._lower_price_cent = None
        self._trace_id = None
        self._user_id = None

    @property
    def base_price_cent(self):
        return self._base_price_cent

    @base_price_cent.setter
    def base_price_cent(self, value):
        self._base_price_cent = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def default_promo_price_cent(self):
        return self._default_promo_price_cent

    @default_promo_price_cent.setter
    def default_promo_price_cent(self, value):
        self._default_promo_price_cent = value
    @property
    def from(self):
        return self._from

    @from.setter
    def from(self, value):
        self._from = value
    @property
    def high_price_cent(self):
        return self._high_price_cent

    @high_price_cent.setter
    def high_price_cent(self, value):
        self._high_price_cent = value
    @property
    def lower_price_cent(self):
        return self._lower_price_cent

    @lower_price_cent.setter
    def lower_price_cent(self, value):
        self._lower_price_cent = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_price_cent:
            if hasattr(self.base_price_cent, 'to_alipay_dict'):
                params['base_price_cent'] = self.base_price_cent.to_alipay_dict()
            else:
                params['base_price_cent'] = self.base_price_cent
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.default_promo_price_cent:
            if hasattr(self.default_promo_price_cent, 'to_alipay_dict'):
                params['default_promo_price_cent'] = self.default_promo_price_cent.to_alipay_dict()
            else:
                params['default_promo_price_cent'] = self.default_promo_price_cent
        if self.from:
            if hasattr(self.from, 'to_alipay_dict'):
                params['from'] = self.from.to_alipay_dict()
            else:
                params['from'] = self.from
        if self.high_price_cent:
            if hasattr(self.high_price_cent, 'to_alipay_dict'):
                params['high_price_cent'] = self.high_price_cent.to_alipay_dict()
            else:
                params['high_price_cent'] = self.high_price_cent
        if self.lower_price_cent:
            if hasattr(self.lower_price_cent, 'to_alipay_dict'):
                params['lower_price_cent'] = self.lower_price_cent.to_alipay_dict()
            else:
                params['lower_price_cent'] = self.lower_price_cent
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
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
        o = AlipayDataAiserviceSmartpriceGetModel()
        if 'base_price_cent' in d:
            o.base_price_cent = d['base_price_cent']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'default_promo_price_cent' in d:
            o.default_promo_price_cent = d['default_promo_price_cent']
        if 'from' in d:
            o.from = d['from']
        if 'high_price_cent' in d:
            o.high_price_cent = d['high_price_cent']
        if 'lower_price_cent' in d:
            o.lower_price_cent = d['lower_price_cent']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


