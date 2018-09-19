#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbOrderFundsVoucherModel(object):

    def __init__(self):
        self._account = None
        self._amount = None
        self._funds_voucher_no = None
        self._gmt_create = None
        self._shop_id = None
        self._store_id = None
        self._trans_type = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def funds_voucher_no(self):
        return self._funds_voucher_no

    @funds_voucher_no.setter
    def funds_voucher_no(self, value):
        self._funds_voucher_no = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.funds_voucher_no:
            if hasattr(self.funds_voucher_no, 'to_alipay_dict'):
                params['funds_voucher_no'] = self.funds_voucher_no.to_alipay_dict()
            else:
                params['funds_voucher_no'] = self.funds_voucher_no
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.trans_type:
            if hasattr(self.trans_type, 'to_alipay_dict'):
                params['trans_type'] = self.trans_type.to_alipay_dict()
            else:
                params['trans_type'] = self.trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbOrderFundsVoucherModel()
        if 'account' in d:
            o.account = d['account']
        if 'amount' in d:
            o.amount = d['amount']
        if 'funds_voucher_no' in d:
            o.funds_voucher_no = d['funds_voucher_no']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'trans_type' in d:
            o.trans_type = d['trans_type']
        return o


