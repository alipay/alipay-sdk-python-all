#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KLineListDTO import KLineListDTO


class ObjKLineDTO(object):

    def __init__(self):
        self._list = None
        self._period = None
        self._split = None
        self._symbol = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, KLineListDTO):
                    self._list.append(i)
                else:
                    self._list.append(KLineListDTO.from_alipay_dict(i))
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def split(self):
        return self._split

    @split.setter
    def split(self, value):
        self._split = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value


    def to_alipay_dict(self):
        params = dict()
        if self.list:
            if isinstance(self.list, list):
                for i in range(0, len(self.list)):
                    element = self.list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list[i] = element.to_alipay_dict()
            if hasattr(self.list, 'to_alipay_dict'):
                params['list'] = self.list.to_alipay_dict()
            else:
                params['list'] = self.list
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.split:
            if hasattr(self.split, 'to_alipay_dict'):
                params['split'] = self.split.to_alipay_dict()
            else:
                params['split'] = self.split
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjKLineDTO()
        if 'list' in d:
            o.list = d['list']
        if 'period' in d:
            o.period = d['period']
        if 'split' in d:
            o.split = d['split']
        if 'symbol' in d:
            o.symbol = d['symbol']
        return o


