#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrendDTO import TrendDTO


class ObjTrendDTO(object):

    def __init__(self):
        self._symbol = None
        self._trend_list = None

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    @property
    def trend_list(self):
        return self._trend_list

    @trend_list.setter
    def trend_list(self, value):
        if isinstance(value, list):
            self._trend_list = list()
            for i in value:
                if isinstance(i, TrendDTO):
                    self._trend_list.append(i)
                else:
                    self._trend_list.append(TrendDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        if self.trend_list:
            if isinstance(self.trend_list, list):
                for i in range(0, len(self.trend_list)):
                    element = self.trend_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trend_list[i] = element.to_alipay_dict()
            if hasattr(self.trend_list, 'to_alipay_dict'):
                params['trend_list'] = self.trend_list.to_alipay_dict()
            else:
                params['trend_list'] = self.trend_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjTrendDTO()
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'trend_list' in d:
            o.trend_list = d['trend_list']
        return o


