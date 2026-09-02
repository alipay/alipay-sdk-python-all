#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepositQueryOpenResult(object):

    def __init__(self):
        self._deposit_account_name = None
        self._deposit_account_no = None
        self._deposit_bank_name = None
        self._order_amount = None
        self._order_id = None
        self._outer_order_id = None
        self._seller_name = None

    @property
    def deposit_account_name(self):
        return self._deposit_account_name

    @deposit_account_name.setter
    def deposit_account_name(self, value):
        self._deposit_account_name = value
    @property
    def deposit_account_no(self):
        return self._deposit_account_no

    @deposit_account_no.setter
    def deposit_account_no(self, value):
        self._deposit_account_no = value
    @property
    def deposit_bank_name(self):
        return self._deposit_bank_name

    @deposit_bank_name.setter
    def deposit_bank_name(self, value):
        self._deposit_bank_name = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_account_name:
            if hasattr(self.deposit_account_name, 'to_alipay_dict'):
                params['deposit_account_name'] = self.deposit_account_name.to_alipay_dict()
            else:
                params['deposit_account_name'] = self.deposit_account_name
        if self.deposit_account_no:
            if hasattr(self.deposit_account_no, 'to_alipay_dict'):
                params['deposit_account_no'] = self.deposit_account_no.to_alipay_dict()
            else:
                params['deposit_account_no'] = self.deposit_account_no
        if self.deposit_bank_name:
            if hasattr(self.deposit_bank_name, 'to_alipay_dict'):
                params['deposit_bank_name'] = self.deposit_bank_name.to_alipay_dict()
            else:
                params['deposit_bank_name'] = self.deposit_bank_name
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepositQueryOpenResult()
        if 'deposit_account_name' in d:
            o.deposit_account_name = d['deposit_account_name']
        if 'deposit_account_no' in d:
            o.deposit_account_no = d['deposit_account_no']
        if 'deposit_bank_name' in d:
            o.deposit_bank_name = d['deposit_bank_name']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        return o


