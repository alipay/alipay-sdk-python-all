#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherList(object):

    def __init__(self):
        self._camp_id = None
        self._prize_id = None
        self._status = None
        self._voucher_amount = None
        self._voucher_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher_amount(self):
        return self._voucher_amount

    @voucher_amount.setter
    def voucher_amount(self, value):
        self._voucher_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voucher_amount:
            if hasattr(self.voucher_amount, 'to_alipay_dict'):
                params['voucher_amount'] = self.voucher_amount.to_alipay_dict()
            else:
                params['voucher_amount'] = self.voucher_amount
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
        o = VoucherList()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'status' in d:
            o.status = d['status']
        if 'voucher_amount' in d:
            o.voucher_amount = d['voucher_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


