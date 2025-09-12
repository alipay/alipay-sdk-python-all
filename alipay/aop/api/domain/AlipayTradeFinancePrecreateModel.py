#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeFinancePrecreateModel(object):

    def __init__(self):
        self._alipay_account = None
        self._alipay_account_type = None
        self._amount = None
        self._biz_date = None
        self._ext_info = None
        self._out_order_no = None
        self._out_request_no = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def alipay_account_type(self):
        return self._alipay_account_type

    @alipay_account_type.setter
    def alipay_account_type(self, value):
        self._alipay_account_type = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.alipay_account_type:
            if hasattr(self.alipay_account_type, 'to_alipay_dict'):
                params['alipay_account_type'] = self.alipay_account_type.to_alipay_dict()
            else:
                params['alipay_account_type'] = self.alipay_account_type
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeFinancePrecreateModel()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'alipay_account_type' in d:
            o.alipay_account_type = d['alipay_account_type']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


