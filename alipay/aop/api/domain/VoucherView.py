#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherView(object):

    def __init__(self):
        self._amount = None
        self._ceiling_amount = None
        self._discount_ratio = None
        self._threshold_amount = None
        self._valid_end = None
        self._valid_start = None
        self._voucher_name = None
        self._voucher_status = None
        self._voucher_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def discount_ratio(self):
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, value):
        self._discount_ratio = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def valid_end(self):
        return self._valid_end

    @valid_end.setter
    def valid_end(self, value):
        self._valid_end = value
    @property
    def valid_start(self):
        return self._valid_start

    @valid_start.setter
    def valid_start(self, value):
        self._valid_start = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.discount_ratio:
            if hasattr(self.discount_ratio, 'to_alipay_dict'):
                params['discount_ratio'] = self.discount_ratio.to_alipay_dict()
            else:
                params['discount_ratio'] = self.discount_ratio
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.valid_end:
            if hasattr(self.valid_end, 'to_alipay_dict'):
                params['valid_end'] = self.valid_end.to_alipay_dict()
            else:
                params['valid_end'] = self.valid_end
        if self.valid_start:
            if hasattr(self.valid_start, 'to_alipay_dict'):
                params['valid_start'] = self.valid_start.to_alipay_dict()
            else:
                params['valid_start'] = self.valid_start
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherView()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'discount_ratio' in d:
            o.discount_ratio = d['discount_ratio']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'valid_end' in d:
            o.valid_end = d['valid_end']
        if 'valid_start' in d:
            o.valid_start = d['valid_start']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


