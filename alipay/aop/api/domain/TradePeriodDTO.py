#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradePeriodDTO(object):

    def __init__(self):
        self._belong_day = None
        self._state_desc = None
        self._trading_day = None

    @property
    def belong_day(self):
        return self._belong_day

    @belong_day.setter
    def belong_day(self, value):
        self._belong_day = value
    @property
    def state_desc(self):
        return self._state_desc

    @state_desc.setter
    def state_desc(self, value):
        self._state_desc = value
    @property
    def trading_day(self):
        return self._trading_day

    @trading_day.setter
    def trading_day(self, value):
        self._trading_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.belong_day:
            if hasattr(self.belong_day, 'to_alipay_dict'):
                params['belong_day'] = self.belong_day.to_alipay_dict()
            else:
                params['belong_day'] = self.belong_day
        if self.state_desc:
            if hasattr(self.state_desc, 'to_alipay_dict'):
                params['state_desc'] = self.state_desc.to_alipay_dict()
            else:
                params['state_desc'] = self.state_desc
        if self.trading_day:
            if hasattr(self.trading_day, 'to_alipay_dict'):
                params['trading_day'] = self.trading_day.to_alipay_dict()
            else:
                params['trading_day'] = self.trading_day
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradePeriodDTO()
        if 'belong_day' in d:
            o.belong_day = d['belong_day']
        if 'state_desc' in d:
            o.state_desc = d['state_desc']
        if 'trading_day' in d:
            o.trading_day = d['trading_day']
        return o


