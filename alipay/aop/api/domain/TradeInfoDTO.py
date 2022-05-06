#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeFundBillDetail import TradeFundBillDetail


class TradeInfoDTO(object):

    def __init__(self):
        self._buyer_id = None
        self._create_time = None
        self._platform_order_id = None
        self._total_amount = None
        self._trade_amount = None
        self._trade_fund_bill_list = None
        self._trade_no = None
        self._trade_status = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def platform_order_id(self):
        return self._platform_order_id

    @platform_order_id.setter
    def platform_order_id(self, value):
        self._platform_order_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_fund_bill_list(self):
        return self._trade_fund_bill_list

    @trade_fund_bill_list.setter
    def trade_fund_bill_list(self, value):
        if isinstance(value, list):
            self._trade_fund_bill_list = list()
            for i in value:
                if isinstance(i, TradeFundBillDetail):
                    self._trade_fund_bill_list.append(i)
                else:
                    self._trade_fund_bill_list.append(TradeFundBillDetail.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.platform_order_id:
            if hasattr(self.platform_order_id, 'to_alipay_dict'):
                params['platform_order_id'] = self.platform_order_id.to_alipay_dict()
            else:
                params['platform_order_id'] = self.platform_order_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_fund_bill_list:
            if isinstance(self.trade_fund_bill_list, list):
                for i in range(0, len(self.trade_fund_bill_list)):
                    element = self.trade_fund_bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_fund_bill_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_fund_bill_list, 'to_alipay_dict'):
                params['trade_fund_bill_list'] = self.trade_fund_bill_list.to_alipay_dict()
            else:
                params['trade_fund_bill_list'] = self.trade_fund_bill_list
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeInfoDTO()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'platform_order_id' in d:
            o.platform_order_id = d['platform_order_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_fund_bill_list' in d:
            o.trade_fund_bill_list = d['trade_fund_bill_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        return o


