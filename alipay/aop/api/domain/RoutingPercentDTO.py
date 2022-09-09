#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferAmount import TransferAmount


class RoutingPercentDTO(object):

    def __init__(self):
        self._end_bps_val = None
        self._onshore_abs_amount = None
        self._onshore_percent = None
        self._start_bps_val = None

    @property
    def end_bps_val(self):
        return self._end_bps_val

    @end_bps_val.setter
    def end_bps_val(self, value):
        self._end_bps_val = value
    @property
    def onshore_abs_amount(self):
        return self._onshore_abs_amount

    @onshore_abs_amount.setter
    def onshore_abs_amount(self, value):
        if isinstance(value, TransferAmount):
            self._onshore_abs_amount = value
        else:
            self._onshore_abs_amount = TransferAmount.from_alipay_dict(value)
    @property
    def onshore_percent(self):
        return self._onshore_percent

    @onshore_percent.setter
    def onshore_percent(self, value):
        self._onshore_percent = value
    @property
    def start_bps_val(self):
        return self._start_bps_val

    @start_bps_val.setter
    def start_bps_val(self, value):
        self._start_bps_val = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_bps_val:
            if hasattr(self.end_bps_val, 'to_alipay_dict'):
                params['end_bps_val'] = self.end_bps_val.to_alipay_dict()
            else:
                params['end_bps_val'] = self.end_bps_val
        if self.onshore_abs_amount:
            if hasattr(self.onshore_abs_amount, 'to_alipay_dict'):
                params['onshore_abs_amount'] = self.onshore_abs_amount.to_alipay_dict()
            else:
                params['onshore_abs_amount'] = self.onshore_abs_amount
        if self.onshore_percent:
            if hasattr(self.onshore_percent, 'to_alipay_dict'):
                params['onshore_percent'] = self.onshore_percent.to_alipay_dict()
            else:
                params['onshore_percent'] = self.onshore_percent
        if self.start_bps_val:
            if hasattr(self.start_bps_val, 'to_alipay_dict'):
                params['start_bps_val'] = self.start_bps_val.to_alipay_dict()
            else:
                params['start_bps_val'] = self.start_bps_val
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoutingPercentDTO()
        if 'end_bps_val' in d:
            o.end_bps_val = d['end_bps_val']
        if 'onshore_abs_amount' in d:
            o.onshore_abs_amount = d['onshore_abs_amount']
        if 'onshore_percent' in d:
            o.onshore_percent = d['onshore_percent']
        if 'start_bps_val' in d:
            o.start_bps_val = d['start_bps_val']
        return o


