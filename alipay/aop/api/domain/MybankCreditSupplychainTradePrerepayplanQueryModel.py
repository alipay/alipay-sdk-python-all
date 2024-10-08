#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainTradePrerepayplanQueryModel(object):

    def __init__(self):
        self._buyer = None
        self._channel = None
        self._ext_data = None
        self._has_bill_detail = None
        self._out_order_no = None
        self._sale_pd_code = None

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
    def has_bill_detail(self):
        return self._has_bill_detail

    @has_bill_detail.setter
    def has_bill_detail(self, value):
        self._has_bill_detail = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value


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
        if self.has_bill_detail:
            if hasattr(self.has_bill_detail, 'to_alipay_dict'):
                params['has_bill_detail'] = self.has_bill_detail.to_alipay_dict()
            else:
                params['has_bill_detail'] = self.has_bill_detail
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.sale_pd_code:
            if hasattr(self.sale_pd_code, 'to_alipay_dict'):
                params['sale_pd_code'] = self.sale_pd_code.to_alipay_dict()
            else:
                params['sale_pd_code'] = self.sale_pd_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainTradePrerepayplanQueryModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'has_bill_detail' in d:
            o.has_bill_detail = d['has_bill_detail']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        return o


