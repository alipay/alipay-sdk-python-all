#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishPracticeInfo(object):

    def __init__(self):
        self._dish_id = None
        self._increase_mode = None
        self._increase_price = None
        self._practice_name = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def increase_mode(self):
        return self._increase_mode

    @increase_mode.setter
    def increase_mode(self, value):
        self._increase_mode = value
    @property
    def increase_price(self):
        return self._increase_price

    @increase_price.setter
    def increase_price(self, value):
        self._increase_price = value
    @property
    def practice_name(self):
        return self._practice_name

    @practice_name.setter
    def practice_name(self, value):
        self._practice_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.increase_mode:
            if hasattr(self.increase_mode, 'to_alipay_dict'):
                params['increase_mode'] = self.increase_mode.to_alipay_dict()
            else:
                params['increase_mode'] = self.increase_mode
        if self.increase_price:
            if hasattr(self.increase_price, 'to_alipay_dict'):
                params['increase_price'] = self.increase_price.to_alipay_dict()
            else:
                params['increase_price'] = self.increase_price
        if self.practice_name:
            if hasattr(self.practice_name, 'to_alipay_dict'):
                params['practice_name'] = self.practice_name.to_alipay_dict()
            else:
                params['practice_name'] = self.practice_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishPracticeInfo()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'increase_mode' in d:
            o.increase_mode = d['increase_mode']
        if 'increase_price' in d:
            o.increase_price = d['increase_price']
        if 'practice_name' in d:
            o.practice_name = d['practice_name']
        return o


