#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeFundBillDetail(object):

    def __init__(self):
        self._amount = None
        self._asset_type_code = None
        self._asset_user_id = None
        self._biz_pay_type = None
        self._create_time = None
        self._payment_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def asset_user_id(self):
        return self._asset_user_id

    @asset_user_id.setter
    def asset_user_id(self, value):
        self._asset_user_id = value
    @property
    def biz_pay_type(self):
        return self._biz_pay_type

    @biz_pay_type.setter
    def biz_pay_type(self, value):
        self._biz_pay_type = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def payment_no(self):
        return self._payment_no

    @payment_no.setter
    def payment_no(self, value):
        self._payment_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.asset_user_id:
            if hasattr(self.asset_user_id, 'to_alipay_dict'):
                params['asset_user_id'] = self.asset_user_id.to_alipay_dict()
            else:
                params['asset_user_id'] = self.asset_user_id
        if self.biz_pay_type:
            if hasattr(self.biz_pay_type, 'to_alipay_dict'):
                params['biz_pay_type'] = self.biz_pay_type.to_alipay_dict()
            else:
                params['biz_pay_type'] = self.biz_pay_type
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.payment_no:
            if hasattr(self.payment_no, 'to_alipay_dict'):
                params['payment_no'] = self.payment_no.to_alipay_dict()
            else:
                params['payment_no'] = self.payment_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeFundBillDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'asset_user_id' in d:
            o.asset_user_id = d['asset_user_id']
        if 'biz_pay_type' in d:
            o.biz_pay_type = d['biz_pay_type']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'payment_no' in d:
            o.payment_no = d['payment_no']
        return o


