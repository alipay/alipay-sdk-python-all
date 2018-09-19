#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainTradePayModel(object):

    def __init__(self):
        self._buyer = None
        self._channel = None
        self._ext_data = None
        self._out_order_no = None
        self._pay_amount = None
        self._request_id = None
        self._sale_pd_code = None
        self._trade_type = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainTradePayModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


