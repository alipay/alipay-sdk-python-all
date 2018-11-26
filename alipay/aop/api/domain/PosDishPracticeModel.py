#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosDishPracticeModel(object):

    def __init__(self):
        self._increase_mode = None
        self._increase_price = None
        self._practice_id = None
        self._practice_name = None
        self._sort = None

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
    def practice_id(self):
        return self._practice_id

    @practice_id.setter
    def practice_id(self, value):
        self._practice_id = value
    @property
    def practice_name(self):
        return self._practice_name

    @practice_name.setter
    def practice_name(self, value):
        self._practice_name = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.practice_id:
            if hasattr(self.practice_id, 'to_alipay_dict'):
                params['practice_id'] = self.practice_id.to_alipay_dict()
            else:
                params['practice_id'] = self.practice_id
        if self.practice_name:
            if hasattr(self.practice_name, 'to_alipay_dict'):
                params['practice_name'] = self.practice_name.to_alipay_dict()
            else:
                params['practice_name'] = self.practice_name
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosDishPracticeModel()
        if 'increase_mode' in d:
            o.increase_mode = d['increase_mode']
        if 'increase_price' in d:
            o.increase_price = d['increase_price']
        if 'practice_id' in d:
            o.practice_id = d['practice_id']
        if 'practice_name' in d:
            o.practice_name = d['practice_name']
        if 'sort' in d:
            o.sort = d['sort']
        return o


