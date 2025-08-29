#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuotaInfoDTO(object):

    def __init__(self):
        self._limit_money = None
        self._limit_times = None
        self._remain_money = None
        self._remain_times = None
        self._trade_no = None

    @property
    def limit_money(self):
        return self._limit_money

    @limit_money.setter
    def limit_money(self, value):
        self._limit_money = value
    @property
    def limit_times(self):
        return self._limit_times

    @limit_times.setter
    def limit_times(self, value):
        self._limit_times = value
    @property
    def remain_money(self):
        return self._remain_money

    @remain_money.setter
    def remain_money(self, value):
        self._remain_money = value
    @property
    def remain_times(self):
        return self._remain_times

    @remain_times.setter
    def remain_times(self, value):
        self._remain_times = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit_money:
            if hasattr(self.limit_money, 'to_alipay_dict'):
                params['limit_money'] = self.limit_money.to_alipay_dict()
            else:
                params['limit_money'] = self.limit_money
        if self.limit_times:
            if hasattr(self.limit_times, 'to_alipay_dict'):
                params['limit_times'] = self.limit_times.to_alipay_dict()
            else:
                params['limit_times'] = self.limit_times
        if self.remain_money:
            if hasattr(self.remain_money, 'to_alipay_dict'):
                params['remain_money'] = self.remain_money.to_alipay_dict()
            else:
                params['remain_money'] = self.remain_money
        if self.remain_times:
            if hasattr(self.remain_times, 'to_alipay_dict'):
                params['remain_times'] = self.remain_times.to_alipay_dict()
            else:
                params['remain_times'] = self.remain_times
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuotaInfoDTO()
        if 'limit_money' in d:
            o.limit_money = d['limit_money']
        if 'limit_times' in d:
            o.limit_times = d['limit_times']
        if 'remain_money' in d:
            o.remain_money = d['remain_money']
        if 'remain_times' in d:
            o.remain_times = d['remain_times']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


