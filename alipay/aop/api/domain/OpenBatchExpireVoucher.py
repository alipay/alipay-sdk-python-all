#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenBatchExpireVoucher(object):

    def __init__(self):
        self._available_aount = None
        self._available_count = None
        self._expire_amount = None
        self._voucher_id = None

    @property
    def available_aount(self):
        return self._available_aount

    @available_aount.setter
    def available_aount(self, value):
        self._available_aount = value
    @property
    def available_count(self):
        return self._available_count

    @available_count.setter
    def available_count(self, value):
        self._available_count = value
    @property
    def expire_amount(self):
        return self._expire_amount

    @expire_amount.setter
    def expire_amount(self, value):
        self._expire_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_aount:
            if hasattr(self.available_aount, 'to_alipay_dict'):
                params['available_aount'] = self.available_aount.to_alipay_dict()
            else:
                params['available_aount'] = self.available_aount
        if self.available_count:
            if hasattr(self.available_count, 'to_alipay_dict'):
                params['available_count'] = self.available_count.to_alipay_dict()
            else:
                params['available_count'] = self.available_count
        if self.expire_amount:
            if hasattr(self.expire_amount, 'to_alipay_dict'):
                params['expire_amount'] = self.expire_amount.to_alipay_dict()
            else:
                params['expire_amount'] = self.expire_amount
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenBatchExpireVoucher()
        if 'available_aount' in d:
            o.available_aount = d['available_aount']
        if 'available_count' in d:
            o.available_count = d['available_count']
        if 'expire_amount' in d:
            o.expire_amount = d['expire_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


