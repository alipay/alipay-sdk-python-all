#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandShopReceiptaccountSaveModel(object):

    def __init__(self):
        self._promise = None
        self._receipt_account_id = None
        self._shop_id = None

    @property
    def promise(self):
        return self._promise

    @promise.setter
    def promise(self, value):
        self._promise = value
    @property
    def receipt_account_id(self):
        return self._receipt_account_id

    @receipt_account_id.setter
    def receipt_account_id(self, value):
        self._receipt_account_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.promise:
            if hasattr(self.promise, 'to_alipay_dict'):
                params['promise'] = self.promise.to_alipay_dict()
            else:
                params['promise'] = self.promise
        if self.receipt_account_id:
            if hasattr(self.receipt_account_id, 'to_alipay_dict'):
                params['receipt_account_id'] = self.receipt_account_id.to_alipay_dict()
            else:
                params['receipt_account_id'] = self.receipt_account_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandShopReceiptaccountSaveModel()
        if 'promise' in d:
            o.promise = d['promise']
        if 'receipt_account_id' in d:
            o.receipt_account_id = d['receipt_account_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


