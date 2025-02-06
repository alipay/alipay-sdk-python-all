#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockPortfolioDeleteModel(object):

    def __init__(self):
        self._open_id = None
        self._symbol_list = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def symbol_list(self):
        return self._symbol_list

    @symbol_list.setter
    def symbol_list(self, value):
        if isinstance(value, list):
            self._symbol_list = list()
            for i in value:
                self._symbol_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.symbol_list:
            if isinstance(self.symbol_list, list):
                for i in range(0, len(self.symbol_list)):
                    element = self.symbol_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symbol_list[i] = element.to_alipay_dict()
            if hasattr(self.symbol_list, 'to_alipay_dict'):
                params['symbol_list'] = self.symbol_list.to_alipay_dict()
            else:
                params['symbol_list'] = self.symbol_list
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
        o = AntfortuneStockPortfolioDeleteModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'symbol_list' in d:
            o.symbol_list = d['symbol_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


