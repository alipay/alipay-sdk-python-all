#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DishRecommend(object):

    def __init__(self):
        self._buy_posibility = None
        self._dish_id = None
        self._dish_name = None
        self._dish_num = None
        self._dish_skuid = None
        self._info_code = None

    @property
    def buy_posibility(self):
        return self._buy_posibility

    @buy_posibility.setter
    def buy_posibility(self, value):
        self._buy_posibility = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def dish_num(self):
        return self._dish_num

    @dish_num.setter
    def dish_num(self, value):
        self._dish_num = value
    @property
    def dish_skuid(self):
        return self._dish_skuid

    @dish_skuid.setter
    def dish_skuid(self, value):
        self._dish_skuid = value
    @property
    def info_code(self):
        return self._info_code

    @info_code.setter
    def info_code(self, value):
        self._info_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_posibility:
            if hasattr(self.buy_posibility, 'to_alipay_dict'):
                params['buy_posibility'] = self.buy_posibility.to_alipay_dict()
            else:
                params['buy_posibility'] = self.buy_posibility
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.dish_num:
            if hasattr(self.dish_num, 'to_alipay_dict'):
                params['dish_num'] = self.dish_num.to_alipay_dict()
            else:
                params['dish_num'] = self.dish_num
        if self.dish_skuid:
            if hasattr(self.dish_skuid, 'to_alipay_dict'):
                params['dish_skuid'] = self.dish_skuid.to_alipay_dict()
            else:
                params['dish_skuid'] = self.dish_skuid
        if self.info_code:
            if hasattr(self.info_code, 'to_alipay_dict'):
                params['info_code'] = self.info_code.to_alipay_dict()
            else:
                params['info_code'] = self.info_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DishRecommend()
        if 'buy_posibility' in d:
            o.buy_posibility = d['buy_posibility']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'dish_num' in d:
            o.dish_num = d['dish_num']
        if 'dish_skuid' in d:
            o.dish_skuid = d['dish_skuid']
        if 'info_code' in d:
            o.info_code = d['info_code']
        return o


