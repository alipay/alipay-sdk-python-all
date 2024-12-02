#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillNotifyInfo(object):

    def __init__(self):
        self._address = None
        self._bill_amount = None
        self._bill_date = None
        self._billkey_type = None
        self._cipher_billkey = None
        self._notify_threshold_amount = None
        self._out_biz_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def billkey_type(self):
        return self._billkey_type

    @billkey_type.setter
    def billkey_type(self, value):
        self._billkey_type = value
    @property
    def cipher_billkey(self):
        return self._cipher_billkey

    @cipher_billkey.setter
    def cipher_billkey(self, value):
        self._cipher_billkey = value
    @property
    def notify_threshold_amount(self):
        return self._notify_threshold_amount

    @notify_threshold_amount.setter
    def notify_threshold_amount(self, value):
        self._notify_threshold_amount = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.billkey_type:
            if hasattr(self.billkey_type, 'to_alipay_dict'):
                params['billkey_type'] = self.billkey_type.to_alipay_dict()
            else:
                params['billkey_type'] = self.billkey_type
        if self.cipher_billkey:
            if hasattr(self.cipher_billkey, 'to_alipay_dict'):
                params['cipher_billkey'] = self.cipher_billkey.to_alipay_dict()
            else:
                params['cipher_billkey'] = self.cipher_billkey
        if self.notify_threshold_amount:
            if hasattr(self.notify_threshold_amount, 'to_alipay_dict'):
                params['notify_threshold_amount'] = self.notify_threshold_amount.to_alipay_dict()
            else:
                params['notify_threshold_amount'] = self.notify_threshold_amount
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillNotifyInfo()
        if 'address' in d:
            o.address = d['address']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'billkey_type' in d:
            o.billkey_type = d['billkey_type']
        if 'cipher_billkey' in d:
            o.cipher_billkey = d['cipher_billkey']
        if 'notify_threshold_amount' in d:
            o.notify_threshold_amount = d['notify_threshold_amount']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        return o


