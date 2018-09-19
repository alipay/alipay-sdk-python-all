#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccTransDetail import AccTransDetail


class AlipayFundBatchTransferModel(object):

    def __init__(self):
        self._acc_detail_list = None
        self._batch_no = None
        self._billing_address = None
        self._biz_code = None
        self._biz_scene = None
        self._extend_params = None
        self._pay_retry = None
        self._payer_account = None
        self._payer_account_type = None
        self._payment_currency = None
        self._product_code = None
        self._request_value_time = None
        self._sign_principal = None
        self._total_count = None
        self._total_trans_amount = None
        self._total_trans_currency = None

    @property
    def acc_detail_list(self):
        return self._acc_detail_list

    @acc_detail_list.setter
    def acc_detail_list(self, value):
        if isinstance(value, list):
            self._acc_detail_list = list()
            for i in value:
                if isinstance(i, AccTransDetail):
                    self._acc_detail_list.append(i)
                else:
                    self._acc_detail_list.append(AccTransDetail.from_alipay_dict(i))
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def billing_address(self):
        return self._billing_address

    @billing_address.setter
    def billing_address(self, value):
        self._billing_address = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def pay_retry(self):
        return self._pay_retry

    @pay_retry.setter
    def pay_retry(self, value):
        self._pay_retry = value
    @property
    def payer_account(self):
        return self._payer_account

    @payer_account.setter
    def payer_account(self, value):
        self._payer_account = value
    @property
    def payer_account_type(self):
        return self._payer_account_type

    @payer_account_type.setter
    def payer_account_type(self, value):
        self._payer_account_type = value
    @property
    def payment_currency(self):
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, value):
        self._payment_currency = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_value_time(self):
        return self._request_value_time

    @request_value_time.setter
    def request_value_time(self, value):
        self._request_value_time = value
    @property
    def sign_principal(self):
        return self._sign_principal

    @sign_principal.setter
    def sign_principal(self, value):
        self._sign_principal = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_trans_amount(self):
        return self._total_trans_amount

    @total_trans_amount.setter
    def total_trans_amount(self, value):
        self._total_trans_amount = value
    @property
    def total_trans_currency(self):
        return self._total_trans_currency

    @total_trans_currency.setter
    def total_trans_currency(self, value):
        self._total_trans_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_detail_list:
            if isinstance(self.acc_detail_list, list):
                for i in range(0, len(self.acc_detail_list)):
                    element = self.acc_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.acc_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.acc_detail_list, 'to_alipay_dict'):
                params['acc_detail_list'] = self.acc_detail_list.to_alipay_dict()
            else:
                params['acc_detail_list'] = self.acc_detail_list
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.billing_address:
            if hasattr(self.billing_address, 'to_alipay_dict'):
                params['billing_address'] = self.billing_address.to_alipay_dict()
            else:
                params['billing_address'] = self.billing_address
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.pay_retry:
            if hasattr(self.pay_retry, 'to_alipay_dict'):
                params['pay_retry'] = self.pay_retry.to_alipay_dict()
            else:
                params['pay_retry'] = self.pay_retry
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = self.payer_account.to_alipay_dict()
            else:
                params['payer_account'] = self.payer_account
        if self.payer_account_type:
            if hasattr(self.payer_account_type, 'to_alipay_dict'):
                params['payer_account_type'] = self.payer_account_type.to_alipay_dict()
            else:
                params['payer_account_type'] = self.payer_account_type
        if self.payment_currency:
            if hasattr(self.payment_currency, 'to_alipay_dict'):
                params['payment_currency'] = self.payment_currency.to_alipay_dict()
            else:
                params['payment_currency'] = self.payment_currency
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_value_time:
            if hasattr(self.request_value_time, 'to_alipay_dict'):
                params['request_value_time'] = self.request_value_time.to_alipay_dict()
            else:
                params['request_value_time'] = self.request_value_time
        if self.sign_principal:
            if hasattr(self.sign_principal, 'to_alipay_dict'):
                params['sign_principal'] = self.sign_principal.to_alipay_dict()
            else:
                params['sign_principal'] = self.sign_principal
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.total_trans_amount:
            if hasattr(self.total_trans_amount, 'to_alipay_dict'):
                params['total_trans_amount'] = self.total_trans_amount.to_alipay_dict()
            else:
                params['total_trans_amount'] = self.total_trans_amount
        if self.total_trans_currency:
            if hasattr(self.total_trans_currency, 'to_alipay_dict'):
                params['total_trans_currency'] = self.total_trans_currency.to_alipay_dict()
            else:
                params['total_trans_currency'] = self.total_trans_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBatchTransferModel()
        if 'acc_detail_list' in d:
            o.acc_detail_list = d['acc_detail_list']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'billing_address' in d:
            o.billing_address = d['billing_address']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'pay_retry' in d:
            o.pay_retry = d['pay_retry']
        if 'payer_account' in d:
            o.payer_account = d['payer_account']
        if 'payer_account_type' in d:
            o.payer_account_type = d['payer_account_type']
        if 'payment_currency' in d:
            o.payment_currency = d['payment_currency']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_value_time' in d:
            o.request_value_time = d['request_value_time']
        if 'sign_principal' in d:
            o.sign_principal = d['sign_principal']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'total_trans_amount' in d:
            o.total_trans_amount = d['total_trans_amount']
        if 'total_trans_currency' in d:
            o.total_trans_currency = d['total_trans_currency']
        return o


