#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainTradeNettingRefundModel(object):

    def __init__(self):
        self._buyer = None
        self._channel = None
        self._out_order_no = None
        self._out_refund_no = None
        self._refund_amount = None
        self._request_id = None
        self._sale_pd_code = None
        self._seller = None
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
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
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
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, Member):
            self._seller = value
        else:
            self._seller = Member.from_alipay_dict(value)
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
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_refund_no:
            if hasattr(self.out_refund_no, 'to_alipay_dict'):
                params['out_refund_no'] = self.out_refund_no.to_alipay_dict()
            else:
                params['out_refund_no'] = self.out_refund_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
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
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
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
        o = MybankCreditSupplychainTradeNettingRefundModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'channel' in d:
            o.channel = d['channel']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_refund_no' in d:
            o.out_refund_no = d['out_refund_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'seller' in d:
            o.seller = d['seller']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


