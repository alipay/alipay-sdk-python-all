#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeAwardDetail(object):

    def __init__(self):
        self._award_amount = None
        self._leads_id = None
        self._poi_mid = None
        self._trade_amount = None
        self._trade_no = None
        self._trade_time = None

    @property
    def award_amount(self):
        return self._award_amount

    @award_amount.setter
    def award_amount(self, value):
        self._award_amount = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def poi_mid(self):
        return self._poi_mid

    @poi_mid.setter
    def poi_mid(self, value):
        self._poi_mid = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_amount:
            if hasattr(self.award_amount, 'to_alipay_dict'):
                params['award_amount'] = self.award_amount.to_alipay_dict()
            else:
                params['award_amount'] = self.award_amount
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.poi_mid:
            if hasattr(self.poi_mid, 'to_alipay_dict'):
                params['poi_mid'] = self.poi_mid.to_alipay_dict()
            else:
                params['poi_mid'] = self.poi_mid
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeAwardDetail()
        if 'award_amount' in d:
            o.award_amount = d['award_amount']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'poi_mid' in d:
            o.poi_mid = d['poi_mid']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


