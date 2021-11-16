#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAuthOrderVoucherCreateModel(object):

    def __init__(self):
        self._amount = None
        self._disable_pay_channels = None
        self._enable_pay_channels = None
        self._extra_param = None
        self._identity_params = None
        self._order_title = None
        self._out_order_no = None
        self._out_request_no = None
        self._pay_timeout = None
        self._payee_logon_id = None
        self._payee_user_id = None
        self._product_code = None
        self._settle_currency = None
        self._timeout_express = None
        self._trans_currency = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def disable_pay_channels(self):
        return self._disable_pay_channels

    @disable_pay_channels.setter
    def disable_pay_channels(self, value):
        self._disable_pay_channels = value
    @property
    def enable_pay_channels(self):
        return self._enable_pay_channels

    @enable_pay_channels.setter
    def enable_pay_channels(self, value):
        self._enable_pay_channels = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def identity_params(self):
        return self._identity_params

    @identity_params.setter
    def identity_params(self, value):
        self._identity_params = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_timeout(self):
        return self._pay_timeout

    @pay_timeout.setter
    def pay_timeout(self, value):
        self._pay_timeout = value
    @property
    def payee_logon_id(self):
        return self._payee_logon_id

    @payee_logon_id.setter
    def payee_logon_id(self, value):
        self._payee_logon_id = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def settle_currency(self):
        return self._settle_currency

    @settle_currency.setter
    def settle_currency(self, value):
        self._settle_currency = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.disable_pay_channels:
            if hasattr(self.disable_pay_channels, 'to_alipay_dict'):
                params['disable_pay_channels'] = self.disable_pay_channels.to_alipay_dict()
            else:
                params['disable_pay_channels'] = self.disable_pay_channels
        if self.enable_pay_channels:
            if hasattr(self.enable_pay_channels, 'to_alipay_dict'):
                params['enable_pay_channels'] = self.enable_pay_channels.to_alipay_dict()
            else:
                params['enable_pay_channels'] = self.enable_pay_channels
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.identity_params:
            if hasattr(self.identity_params, 'to_alipay_dict'):
                params['identity_params'] = self.identity_params.to_alipay_dict()
            else:
                params['identity_params'] = self.identity_params
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_timeout:
            if hasattr(self.pay_timeout, 'to_alipay_dict'):
                params['pay_timeout'] = self.pay_timeout.to_alipay_dict()
            else:
                params['pay_timeout'] = self.pay_timeout
        if self.payee_logon_id:
            if hasattr(self.payee_logon_id, 'to_alipay_dict'):
                params['payee_logon_id'] = self.payee_logon_id.to_alipay_dict()
            else:
                params['payee_logon_id'] = self.payee_logon_id
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.settle_currency:
            if hasattr(self.settle_currency, 'to_alipay_dict'):
                params['settle_currency'] = self.settle_currency.to_alipay_dict()
            else:
                params['settle_currency'] = self.settle_currency
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAuthOrderVoucherCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'disable_pay_channels' in d:
            o.disable_pay_channels = d['disable_pay_channels']
        if 'enable_pay_channels' in d:
            o.enable_pay_channels = d['enable_pay_channels']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'identity_params' in d:
            o.identity_params = d['identity_params']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_timeout' in d:
            o.pay_timeout = d['pay_timeout']
        if 'payee_logon_id' in d:
            o.payee_logon_id = d['payee_logon_id']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'settle_currency' in d:
            o.settle_currency = d['settle_currency']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        return o


