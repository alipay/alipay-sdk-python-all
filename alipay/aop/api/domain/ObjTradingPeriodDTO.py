#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradingPeriodDTO import TradingPeriodDTO


class ObjTradingPeriodDTO(object):

    def __init__(self):
        self._periods = None
        self._symbol = None
        self._time_zone = None

    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, value):
        if isinstance(value, list):
            self._periods = list()
            for i in value:
                if isinstance(i, TradingPeriodDTO):
                    self._periods.append(i)
                else:
                    self._periods.append(TradingPeriodDTO.from_alipay_dict(i))
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value


    def to_alipay_dict(self):
        params = dict()
        if self.periods:
            if isinstance(self.periods, list):
                for i in range(0, len(self.periods)):
                    element = self.periods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.periods[i] = element.to_alipay_dict()
            if hasattr(self.periods, 'to_alipay_dict'):
                params['periods'] = self.periods.to_alipay_dict()
            else:
                params['periods'] = self.periods
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjTradingPeriodDTO()
        if 'periods' in d:
            o.periods = d['periods']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        return o


