#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelUserRateQueryRequest(object):

    def __init__(self):
        self._bill_period = None
        self._passport_id = None
        self._sell_channel_code = None

    @property
    def bill_period(self):
        return self._bill_period

    @bill_period.setter
    def bill_period(self, value):
        self._bill_period = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def sell_channel_code(self):
        return self._sell_channel_code

    @sell_channel_code.setter
    def sell_channel_code(self, value):
        self._sell_channel_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_period:
            if hasattr(self.bill_period, 'to_alipay_dict'):
                params['bill_period'] = self.bill_period.to_alipay_dict()
            else:
                params['bill_period'] = self.bill_period
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.sell_channel_code:
            if hasattr(self.sell_channel_code, 'to_alipay_dict'):
                params['sell_channel_code'] = self.sell_channel_code.to_alipay_dict()
            else:
                params['sell_channel_code'] = self.sell_channel_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelUserRateQueryRequest()
        if 'bill_period' in d:
            o.bill_period = d['bill_period']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'sell_channel_code' in d:
            o.sell_channel_code = d['sell_channel_code']
        return o


