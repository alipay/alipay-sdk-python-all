#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HelloBikeVoucherInfo(object):

    def __init__(self):
        self._prize_id = None
        self._total_amount = None
        self._valid_time = None
        self._voucher_desc = None
        self._voucher_id = None
        self._voucher_status = None

    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HelloBikeVoucherInfo()
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        return o


