#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeCustomDisplayInfo import PrizeCustomDisplayInfo


class SignInPrizeConfig(object):

    def __init__(self):
        self._frequency_count = None
        self._frequency_type = None
        self._price = None
        self._prize_custom_display_info = None
        self._prize_end_time = None
        self._prize_id = None
        self._prize_name = None
        self._prize_start_time = None
        self._prize_type = None

    @property
    def frequency_count(self):
        return self._frequency_count

    @frequency_count.setter
    def frequency_count(self, value):
        self._frequency_count = value
    @property
    def frequency_type(self):
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, value):
        self._frequency_type = value
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
    def prize_end_time(self):
        return self._prize_end_time

    @prize_end_time.setter
    def prize_end_time(self, value):
        self._prize_end_time = value
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
    def prize_start_time(self):
        return self._prize_start_time

    @prize_start_time.setter
    def prize_start_time(self, value):
        self._prize_start_time = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.frequency_count:
            if hasattr(self.frequency_count, 'to_alipay_dict'):
                params['frequency_count'] = self.frequency_count.to_alipay_dict()
            else:
                params['frequency_count'] = self.frequency_count
        if self.frequency_type:
            if hasattr(self.frequency_type, 'to_alipay_dict'):
                params['frequency_type'] = self.frequency_type.to_alipay_dict()
            else:
                params['frequency_type'] = self.frequency_type
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
        if self.prize_end_time:
            if hasattr(self.prize_end_time, 'to_alipay_dict'):
                params['prize_end_time'] = self.prize_end_time.to_alipay_dict()
            else:
                params['prize_end_time'] = self.prize_end_time
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
        if self.prize_start_time:
            if hasattr(self.prize_start_time, 'to_alipay_dict'):
                params['prize_start_time'] = self.prize_start_time.to_alipay_dict()
            else:
                params['prize_start_time'] = self.prize_start_time
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignInPrizeConfig()
        if 'frequency_count' in d:
            o.frequency_count = d['frequency_count']
        if 'frequency_type' in d:
            o.frequency_type = d['frequency_type']
        if 'price' in d:
            o.price = d['price']
        if 'prize_custom_display_info' in d:
            o.prize_custom_display_info = d['prize_custom_display_info']
        if 'prize_end_time' in d:
            o.prize_end_time = d['prize_end_time']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_start_time' in d:
            o.prize_start_time = d['prize_start_time']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        return o


