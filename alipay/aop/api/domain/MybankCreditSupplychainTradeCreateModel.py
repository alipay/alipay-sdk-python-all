#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member
from alipay.aop.api.domain.Account import Account
from alipay.aop.api.domain.Account import Account
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainTradeCreateModel(object):

    def __init__(self):
        self._buyer = None
        self._channel = None
        self._expire_date = None
        self._ext_data = None
        self._out_order_no = None
        self._out_order_title = None
        self._pay_account = None
        self._rcv_account = None
        self._request_id = None
        self._sale_pd_code = None
        self._seller = None
        self._trade_amount = None
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
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
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
    def out_order_title(self):
        return self._out_order_title

    @out_order_title.setter
    def out_order_title(self, value):
        self._out_order_title = value
    @property
    def pay_account(self):
        return self._pay_account

    @pay_account.setter
    def pay_account(self, value):
        if isinstance(value, Account):
            self._pay_account = value
        else:
            self._pay_account = Account.from_alipay_dict(value)
    @property
    def rcv_account(self):
        return self._rcv_account

    @rcv_account.setter
    def rcv_account(self, value):
        if isinstance(value, Account):
            self._rcv_account = value
        else:
            self._rcv_account = Account.from_alipay_dict(value)
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
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
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
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
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
        if self.out_order_title:
            if hasattr(self.out_order_title, 'to_alipay_dict'):
                params['out_order_title'] = self.out_order_title.to_alipay_dict()
            else:
                params['out_order_title'] = self.out_order_title
        if self.pay_account:
            if hasattr(self.pay_account, 'to_alipay_dict'):
                params['pay_account'] = self.pay_account.to_alipay_dict()
            else:
                params['pay_account'] = self.pay_account
        if self.rcv_account:
            if hasattr(self.rcv_account, 'to_alipay_dict'):
                params['rcv_account'] = self.rcv_account.to_alipay_dict()
            else:
                params['rcv_account'] = self.rcv_account
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
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
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
        o = MybankCreditSupplychainTradeCreateModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'channel' in d:
            o.channel = d['channel']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_order_title' in d:
            o.out_order_title = d['out_order_title']
        if 'pay_account' in d:
            o.pay_account = d['pay_account']
        if 'rcv_account' in d:
            o.rcv_account = d['rcv_account']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sale_pd_code' in d:
            o.sale_pd_code = d['sale_pd_code']
        if 'seller' in d:
            o.seller = d['seller']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


