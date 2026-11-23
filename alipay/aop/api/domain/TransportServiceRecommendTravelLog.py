#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransportServiceRecommendTravelLog(object):

    def __init__(self):
        self._amount = None
        self._biz_time = None
        self._biz_type = None
        self._log_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def log_id(self):
        return self._log_id

    @log_id.setter
    def log_id(self, value):
        self._log_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.log_id:
            if hasattr(self.log_id, 'to_alipay_dict'):
                params['log_id'] = self.log_id.to_alipay_dict()
            else:
                params['log_id'] = self.log_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransportServiceRecommendTravelLog()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'log_id' in d:
            o.log_id = d['log_id']
        return o


