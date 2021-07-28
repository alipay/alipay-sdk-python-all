#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeItemResult(object):

    def __init__(self):
        self._alipay_order_no = None
        self._gmt_create = None
        self._gmt_pay = None
        self._gmt_refund = None
        self._goods_memo = None
        self._goods_title = None
        self._merchant_order_no = None
        self._net_mdiscount = None
        self._other_account = None
        self._refund_amount = None
        self._service_fee = None
        self._store_name = None
        self._store_no = None
        self._total_amount = None
        self._trade_status = None
        self._trade_type = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def goods_memo(self):
        return self._goods_memo

    @goods_memo.setter
    def goods_memo(self, value):
        self._goods_memo = value
    @property
    def goods_title(self):
        return self._goods_title

    @goods_title.setter
    def goods_title(self, value):
        self._goods_title = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def net_mdiscount(self):
        return self._net_mdiscount

    @net_mdiscount.setter
    def net_mdiscount(self, value):
        self._net_mdiscount = value
    @property
    def other_account(self):
        return self._other_account

    @other_account.setter
    def other_account(self, value):
        self._other_account = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, value):
        self._service_fee = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_no(self):
        return self._store_no

    @store_no.setter
    def store_no(self, value):
        self._store_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.goods_memo:
            if hasattr(self.goods_memo, 'to_alipay_dict'):
                params['goods_memo'] = self.goods_memo.to_alipay_dict()
            else:
                params['goods_memo'] = self.goods_memo
        if self.goods_title:
            if hasattr(self.goods_title, 'to_alipay_dict'):
                params['goods_title'] = self.goods_title.to_alipay_dict()
            else:
                params['goods_title'] = self.goods_title
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.net_mdiscount:
            if hasattr(self.net_mdiscount, 'to_alipay_dict'):
                params['net_mdiscount'] = self.net_mdiscount.to_alipay_dict()
            else:
                params['net_mdiscount'] = self.net_mdiscount
        if self.other_account:
            if hasattr(self.other_account, 'to_alipay_dict'):
                params['other_account'] = self.other_account.to_alipay_dict()
            else:
                params['other_account'] = self.other_account
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.service_fee:
            if hasattr(self.service_fee, 'to_alipay_dict'):
                params['service_fee'] = self.service_fee.to_alipay_dict()
            else:
                params['service_fee'] = self.service_fee
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_no:
            if hasattr(self.store_no, 'to_alipay_dict'):
                params['store_no'] = self.store_no.to_alipay_dict()
            else:
                params['store_no'] = self.store_no
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
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
        o = TradeItemResult()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'goods_memo' in d:
            o.goods_memo = d['goods_memo']
        if 'goods_title' in d:
            o.goods_title = d['goods_title']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'net_mdiscount' in d:
            o.net_mdiscount = d['net_mdiscount']
        if 'other_account' in d:
            o.other_account = d['other_account']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'service_fee' in d:
            o.service_fee = d['service_fee']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_no' in d:
            o.store_no = d['store_no']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


