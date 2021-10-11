#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DriverTradeInfo(object):

    def __init__(self):
        self._create_date = None
        self._driver_user_id = None
        self._trade_no = None
        self._trade_total_amount = None

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_total_amount(self):
        return self._trade_total_amount

    @trade_total_amount.setter
    def trade_total_amount(self, value):
        self._trade_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.driver_user_id:
            if hasattr(self.driver_user_id, 'to_alipay_dict'):
                params['driver_user_id'] = self.driver_user_id.to_alipay_dict()
            else:
                params['driver_user_id'] = self.driver_user_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_total_amount:
            if hasattr(self.trade_total_amount, 'to_alipay_dict'):
                params['trade_total_amount'] = self.trade_total_amount.to_alipay_dict()
            else:
                params['trade_total_amount'] = self.trade_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DriverTradeInfo()
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'driver_user_id' in d:
            o.driver_user_id = d['driver_user_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_total_amount' in d:
            o.trade_total_amount = d['trade_total_amount']
        return o


